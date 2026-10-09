#!/usr/bin/env python3
"""Repo-Regeln für die Website Praxis Hüwel (läuft bei jedem Pull Request und lokal).

Aufruf:  python3 scripts/check_repo.py --base origin/main
Endet mit Exit-Code 1, wenn eine Regel verletzt ist. Die Regeln stehen in AGENTS.md und DESIGN.md.
"""
import argparse, os, re, subprocess, sys, html

ap = argparse.ArgumentParser()
ap.add_argument("--base", default="origin/main", help="Vergleichsstand (Standard: origin/main)")
args = ap.parse_args()

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
errors, warnings = [], []


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True).stdout


def all_html():
    out = []
    for d, dirs, files in os.walk("."):
        dirs[:] = [x for x in dirs if x not in (".git", "node_modules", ".github")]
        for f in files:
            if f.endswith(".html"):
                out.append(os.path.join(d, f)[2:])
    return sorted(out)


def read(p):
    return open(p, encoding="utf-8", errors="replace").read()


# ---- 1. Jede echte Seite steht in der sitemap.xml und umgekehrt -------------------------------
LIVE = "https://www.praxis-huewel.de/"
sm = read("sitemap.xml")
sm_paths = {html.unescape(u).replace(LIVE, "") or "index.html" for u in re.findall(r"<loc>([^<]+)</loc>", sm)}
from urllib.parse import unquote
sm_paths = {unquote(p) for p in sm_paths}
for p in all_html():
    b = read(p)
    if 'http-equiv="refresh"' in b or p == "404.html":
        continue  # Weiterleitung oder Fehlerseite
    if p not in sm_paths:
        errors.append(f"Seite fehlt in sitemap.xml: {p}")
for p in sm_paths:
    if not os.path.exists(p):
        errors.append(f"sitemap.xml nennt eine Seite, die es nicht gibt: {p}")

# ---- 2. Keine Fremd-Ladungen im Seitencode ----------------------------------------------------
FORBIDDEN = [
    (r"fonts\.(googleapis|gstatic)\.com", "Google Fonts (Datenschutz): Systemschrift nutzen"),
    (r"<script[^>]+src=[\"']https?://", "Fremdes Skript im Seitencode (Datenschutz)"),
    (r"<iframe[^>]+src=[\"']https?://", "Direktes iframe von Fremdanbieter: embed-gate nutzen"),
    (r"<link[^>]+rel=[\"']stylesheet[\"'][^>]+href=[\"']https?://", "Fremdes Stylesheet (Datenschutz)"),
    (r"googletagmanager\.com|google-analytics\.com|connect\.facebook\.net|hotjar", "Tracking-Skript ohne Freigabe von 741 Studio"),
]
for p in all_html():
    b = read(p)
    for rx, msg in FORBIDDEN:
        if re.search(rx, b, re.I):
            errors.append(f"{p}: {msg}")
    if re.search(r"<style\b", b, re.I):
        errors.append(f"{p}: eigener <style>-Block ist nicht erlaubt (DESIGN.md)")

# ---- 3. Löschungen (Schutz vor Datenverlust) --------------------------------------------------
deleted = [x for x in git("diff", "--diff-filter=D", "--name-only", f"{args.base}...HEAD").splitlines() if x]
if deleted and os.environ.get("ALLOW_DELETE") != "1":
    errors.append("Dateien gelöscht (nur mit [löschen erlaubt] im Titel): " + ", ".join(deleted[:15]) + (" …" if len(deleted) > 15 else ""))

# ---- 4. Geschützte Dateien (Hinweis, kein Fehler: 741 Studio prüft per Code-Owner) -------------
PROTECTED = ("assets/css/", "assets/js/", "CNAME", "robots.txt", ".github/", "scripts/", "AGENTS.md", "CLAUDE.md", "DESIGN.md")
changed = [x for x in git("diff", "--name-only", f"{args.base}...HEAD").splitlines() if x]
touched = [x for x in changed if x.startswith(PROTECTED) or x in PROTECTED]
if touched:
    warnings.append("Geschützte Dateien geändert (nur 741 Studio): " + ", ".join(touched[:15]))

# ---- 5. Neue Bilder: Name und Größe -----------------------------------------------------------
added = [x for x in git("diff", "--diff-filter=A", "--name-only", f"{args.base}...HEAD").splitlines() if x]
for f in added:
    if f.startswith("assets/images/") and re.search(r"\.(jpe?g|png|webp)$", f, re.I):
        name = os.path.basename(f)
        if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", name):
            errors.append(f"Bildname nicht erlaubt (klein, Bindestriche, keine Leerzeichen): {f}")
        if re.search(r"(img_|chatgpt|screenshot|dsc_|image\d)", name, re.I):
            errors.append(f"Bildname nicht beschreibend: {f}")
        if os.path.exists(f) and os.path.getsize(f) > 220_000:
            errors.append(f"Bild größer als 220 KB: {f} ({os.path.getsize(f)//1024} KB)")

# ---- 6. Risikowörter (HWG) nur in NEUEN Zeilen ------------------------------------------------
RISK = [
    (r"\bkrebs\w*", "Krebs (HWG: keine Aussagen zu meldepflichtigen Krankheiten)"),
    (r"\btumor\w*", "Tumor (HWG)"),
    (r"\bheilt\b|\bheilen sie\b|\bheilung (garantiert|von|bei)\b", "Heilversprechen (HWG)"),
    (r"\bgarantier\w*", "Garantie (HWG)"),
    (r"\bsicher(e|er|en)? (erfolg|heilung|wirkung)\b", "Erfolgsversprechen (HWG)"),
    (r"\b(wissenschaftlich|nachweislich|klinisch) (bewiesen|belegt|erwiesen)\b", "Wirksamkeitsbeleg ohne Quelle (HWG)"),
    (r"\bohne nebenwirkungen\b|\bnebenwirkungsfrei\b", "Nebenwirkungsfrei (HWG)"),
    (r"\bwunder\w*", "Wunder (HWG)"),
    (r"\b100 ?%", "100 % (HWG/Irreführung)"),
]
diff = git("diff", "--unified=0", f"{args.base}...HEAD", "--", "*.html", "*.md")
cur = None
for line in diff.splitlines():
    if line.startswith("+++ b/"):
        cur = line[6:]
        continue
    if not line.startswith("+") or line.startswith("+++") or cur is None:
        continue
    if cur in ("AGENTS.md", "DESIGN.md", "README.md", "CLAUDE.md", "SECURITY.md", "ANLEITUNG.md"):
        continue
    text = re.sub(r"<[^>]+>", " ", line[1:])
    for rx, msg in RISK:
        m = re.search(rx, text, re.I)
        if m:
            errors.append(f"{cur}: Risikowort „{m.group(0)}“ – {msg}. 741 Studio und Martin Hüwel müssen das prüfen.")

for w in warnings:
    print("HINWEIS:", w)
for e in errors:
    print("FEHLER: ", e)
if errors:
    print(f"\nERGEBNIS: {len(errors)} Regel(n) verletzt")
    sys.exit(1)
print("ERGEBNIS: alle Repo-Regeln erfüllt")
