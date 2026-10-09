#!/usr/bin/env python3
"""Vollständiger Check für www.praxis-huewel.de: Funktion + technisches SEO.
Live prüfen:    python3 scripts/audit.py
Lokal prüfen:   python3 -m http.server 8765   (in einem zweiten Fenster)
                SITE=http://localhost:8765/ python3 scripts/audit.py
Prüft alle URLs aus sitemap.xml. Endet mit Exit-Code 1, wenn etwas nicht stimmt."""
import re, sys, json, html, urllib.request, urllib.parse, concurrent.futures as cf, collections
import os, socket
socket.setdefaulttimeout(15)  # nie länger als 15 s auf eine Antwort warten
LIVE = "https://www.praxis-huewel.de/"
BASE = os.environ.get("SITE", LIVE)
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"}
def q(u): return urllib.parse.quote(u, safe=":/?#[]@!$&'()*+,;=%")
def get(u, method="GET", t=25):
    try:
        r = urllib.request.Request(q(u), headers=UA, method=method)
        with urllib.request.urlopen(r, timeout=t) as f:
            return f.status, dict(f.headers), (f.read() if method == "GET" else b"")
    except urllib.error.HTTPError as e: return e.code, {}, b""
    except Exception as e: return 0, {"err": str(e)}, b""
sm = get(BASE + "sitemap.xml")[2].decode()
urls = [html.unescape(x).replace(LIVE, BASE) for x in re.findall(r"<loc>([^<]+)</loc>", sm)]
pages = {}
def fetch(u):
    s, h, b = get(u); return u, s, b.decode("utf-8", "replace")
with cf.ThreadPoolExecutor(8) as ex:
    for u, s, b in ex.map(fetch, urls): pages[u] = (s, b)
issues = collections.defaultdict(list); info = {}
assets = {}; inbound = collections.Counter(); titles = collections.defaultdict(list); descs = collections.defaultdict(list)
for u, (s, b) in pages.items():
    p = "/" + u.replace(BASE, "")
    if s != 200: issues[p].append(("FEHLER", f"HTTP {s}")); continue
    t = re.search(r"<title>(.*?)</title>", b, re.S); t = html.unescape(t.group(1).strip()) if t else ""
    d = re.search(r'<meta name="description" content="([^"]*)"', b); d = html.unescape(d.group(1)) if d else ""
    titles[t].append(p); descs[d].append(p)
    if not t: issues[p].append(("SEO", "kein Title"))
    elif len(t) > 62: issues[p].append(("SEO", f"Title zu lang ({len(t)})"))
    elif len(t) < 25: issues[p].append(("SEO", f"Title sehr kurz ({len(t)})"))
    if not d: issues[p].append(("SEO", "keine Meta-Description"))
    elif len(d) > 160: issues[p].append(("SEO", f"Description zu lang ({len(d)})"))
    elif len(d) < 90: issues[p].append(("SEO", f"Description zu kurz ({len(d)})"))
    c = re.search(r'<link rel="canonical" href="([^"]*)"', b)
    if not c: issues[p].append(("SEO", "kein Canonical"))
    elif urllib.parse.unquote(c.group(1).replace(LIVE, BASE)) != urllib.parse.unquote(u): issues[p].append(("SEO", f"Canonical weicht ab: {c.group(1)}"))
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", b, flags=re.S)
    hs = [(int(m.group(1)), re.sub(r"<[^>]+>", "", m.group(2)).strip()) for m in re.finditer(r"<h([1-6])[^>]*>(.*?)</h\1>", body, re.S)]
    if sum(1 for l, _ in hs if l == 1) != 1: issues[p].append(("SEO", f"{sum(1 for l,_ in hs if l==1)} H1"))
    last = 0
    for l, tx in hs:
        if last and l > last + 1: issues[p].append(("SEO", f"Überschriften-Sprung h{last}→h{l}: {tx[:40]}")); break
        last = l
    text = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body)))
    wc = len(text.split()); info[p] = dict(words=wc, h2=sum(1 for l, _ in hs if l == 2))
    if wc < 250 and not any(k in p for k in ("impressum", "datenschutz", "kontakt", "blog.html", "termine")): issues[p].append(("SEO", f"dünner Inhalt ({wc} Wörter)"))
    for k in ("og:title", "og:description", "og:image", "twitter:card"):
        if k not in b: issues[p].append(("SEO", f"fehlt {k}"))
    if "application/ld+json" not in b and not any(k in p for k in ("impressum", "datenschutz")): issues[p].append(("SEO", "kein JSON-LD"))
    if "noindex" in b and not any(k in p for k in ("impressum", "datenschutz")): issues[p].append(("SEO", "NOINDEX"))
    if re.search(r"\b(TODO|Platzhalter|lorem ipsum|Video folgt)\b", text, re.I): issues[p].append(("FEHLER", "Platzhaltertext"))
    for m in re.finditer(r"<img\b[^>]*>", b):
        tag = m.group(0); sm_ = re.search(r'\bsrc="([^"]+)"', tag)
        if not sm_: continue
        src = urllib.parse.urljoin(u, html.unescape(sm_.group(1))); assets.setdefault(src, set()).add(p)
        alt = re.search(r'\balt="([^"]*)"', tag)
        if alt is None: issues[p].append(("SEO", f"Bild ohne alt: {src.split('/')[-1]}"))
        elif alt.group(1).strip() == "" and "avatar" not in src: issues[p].append(("SEO", f"leeres alt: {src.split('/')[-1]}"))
        if not (re.search(r'\bwidth="', tag) and re.search(r'\bheight="', tag)): issues[p].append(("PERF", f"Bild ohne width/height: {src.split('/')[-1]}"))
    for m in re.finditer(r'<(?:a|link|script|source)\b[^>]*?(?:href|src)="([^"#]+)', b):
        h = html.unescape(m.group(1))
        if h.startswith(("mailto:", "tel:", "javascript:", "data:", "whatsapp:")): continue
        full = urllib.parse.urljoin(u, h).split("?")[0]
        assets.setdefault(full, set()).add(p)
        if full.startswith(BASE) and full.endswith((".html", "/")) and full.rstrip("/") != u.rstrip("/"): inbound[urllib.parse.unquote(full)] += 1
def chk(u):
    s, h, bd = get(u, "HEAD", 20)
    if s in (0, 400, 403, 405, 501): s, h, bd = get(u, "GET", 20)
    size = int(h.get("Content-Length", 0) or 0) if h else 0
    return u, s, size
broken = []; big = []
with cf.ThreadPoolExecutor(12) as ex:
    for u, s, size in ex.map(chk, sorted(assets)):
        if s != 200 and not (300 <= s < 400): broken.append((u, s, sorted(assets[u])[:3]))
        if u.startswith(BASE) and re.search(r"\.(jpg|jpeg|png|webp)$", u, re.I) and size > 220_000: big.append((u.replace(BASE, ""), size // 1024))
for t, ps in titles.items():
    if len(ps) > 1: [issues[x].append(("SEO", f"doppelter Title: {t[:40]}")) for x in ps]
for d, ps in descs.items():
    if d and len(ps) > 1: [issues[x].append(("SEO", "doppelte Description")) for x in ps]
for u in urls:
    if u.rstrip("/") != BASE.rstrip("/") and inbound[urllib.parse.unquote(u)] < 2: issues["/" + u.replace(BASE, "")].append(("SEO", f"nur {inbound[urllib.parse.unquote(u)]} interne Links auf diese Seite"))
print(f"Seiten geprüft: {len(urls)} | URLs/Assets geprüft: {len(assets)}")
print("\n== KAPUTTE LINKS / BILDER / DATEIEN"); [print(" ", b) for b in broken] or None
if not broken: print("  keine")
print("\n== GROSSE BILDER (>220 KB)"); [print(" ", b) for b in big] or None
if not big: print("  keine")
cnt = collections.Counter(k for v in issues.values() for k, _ in v)
print("\n== PROBLEME PRO SEITE", dict(cnt))
for p in sorted(issues):
    for k, m in issues[p]: print(f"  [{k}] {p}: {m}")
for p, i in sorted(info.items()): pass
# Externe Adressen (z. B. wa.me, Facebook) antworten Prüfprogrammen oft mit 400 – das ist nur eine Warnung.
broken_intern = [b for b in broken if b[0].startswith(BASE)]
if len(broken) != len(broken_intern): print(f"\nHinweis: {len(broken) - len(broken_intern)} externe Adressen antworten nicht mit 200 (nur Warnung).")
if broken_intern or issues:
    print("\nERGEBNIS: FEHLER GEFUNDEN"); sys.exit(1)
print("\nERGEBNIS: alles in Ordnung")
