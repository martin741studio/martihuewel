# Security & Safety — Praxis Hüwel

Project-specific status against 741's standard checklist (master version: `00_project/website-security-checklist.md` in the 741 studio repo). Update the checkboxes as items land; don't remove items just because they're not done yet.

**Re-audited 2026-09-14** against the actual current repo state (24+ pages, 4 forms, real embeds) — the previous version of this file was written at the 2-page MVP stage and had drifted out of date. Two real gaps were found and fixed during this re-audit (see below).

## Current status

- [x] Static site, no server-side app code to exploit.
- [x] Repo public — acceptable at this stage (no secrets, no backend keys in-repo; verified via `git log --all -- .env*` — never committed).
- [x] GitHub secret scanning + push protection: **enabled** (verified via `gh api .../security_and_analysis`).
- [x] HTTPS enforced + **HSTS active** (`strict-transport-security: max-age=31556952`, confirmed via live response headers) — GitHub Pages provides this automatically, no action needed.
- [x] Honeypot field on **all 4** public forms (`index.html`, `home-improved.html`, `kontakt.html`, `der-wartezeit-vermeider.html`) — **found `index.html`'s form was missing it during this re-audit; fixed.**
- [x] `.gitignore` covers `node_modules/`, `.DS_Store`, **and now `.env*`** — **found `.env*` was missing during this re-audit despite this file previously claiming otherwise; fixed.** No `.env` file has ever actually been committed, so this was a latent gap, not an active leak.
- [x] Consent checkbox (unchecked by default, `required`, linked to Datenschutzerklärung) on all 4 forms — verified present and correctly wired on every form.
- [x] `Impressum` and `Datenschutzerklärung` pages present, linked in every page's footer (built this session — not yet true when this file was last updated).
- [x] HWG disclaimer box present on every method/treatment/condition page (verified across all 24 pages this session).
- [ ] **HWG §11 testimonial risk — flag to client, don't silently ship.** The 5 real patient testimonials (ported verbatim from the live site) include phrasing like *"seitdem sind meine Beschwerden verschwunden"* and *"hat meinen Heilungsprozess drastisch abgekürzt"* — this reads as an implied cure/effectiveness claim attributed to a patient, which is exactly what HWG §11 restricts for health-service advertising. This is a **pre-existing risk already live on praxis-huewel.de today**, not something introduced by this rebuild — but porting it verbatim carries it forward. Needs a legal/compliance call from Martin before go-live: keep as-is (matches current live site), soften the wording, or drop the two riskiest lines.
- [ ] **Security headers (CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy) — structurally blocked on GitHub Pages.** Confirmed via live header check: none of these are sent and GitHub Pages has no `_headers`-file or custom-header mechanism (unlike Netlify/Cloudflare Pages). **Action needed before production cutover:** put Cloudflare (free tier, proxy/orange-cloud mode) in front of the domain — Cloudflare can inject all of these via Transform Rules even with GitHub Pages as the origin. Don't skip this; it's the one "Must" item this hosting choice can't satisfy on its own.
- [ ] **Cloudflare Turnstile on all forms** — add once a form has a real backend (see below). Same Cloudflare account as the headers fix above can serve both purposes.
- [ ] **Form backend (Supabase Edge Function + Resend)** — all 4 forms currently have `action="#"` / `data-endpoint="TODO"`, no live submit target. Needs: RLS-protected table, server-side validation, rate limiting, sanitization of free-text fields (the "Fragen/Wünsche" field is the main stored-XSS surface once a backend exists).
- [ ] **SPF/DKIM/DMARC** — pending, set up once the sending domain/email (Resend) is configured.
- [ ] **Cookie/consent banner + Consent Mode v2** — every page's footer has a "Cookie-Einstellungen" link, but it currently points to `#` (placeholder, not wired to an actual consent tool yet). Needed before GA4 or any tracking script is added — not urgent yet since no tracking is live.
- [ ] **AV-Verträge** (Supabase, Resend, Cal.com, host, Calendly) — needed before any personal data actually flows through them. Note: the real Calendly widget is already embedded and live-functional on `index.html`/`home-improved.html` — Calendly itself should be added to this list now, not just deferred to "once backend exists."
- [ ] Uptime monitoring — set up once this is the production domain.
- [ ] Right-to-erasure process — not yet documented (depends on the Supabase backend existing first).

## Third-party embeds currently live on this site (§7 of the master checklist)
All loaded only from their real vendor domains — verified, no proxy/mirror risk:
- Calendly (`calendly.com`, `assets.calendly.com`) — booking widget, `index.html` + `home-improved.html`
- Google Maps (`maps.google.com` iframe embed) — every page with a Standort section
- YouTube (`youtube-nocookie.com`, click-to-play facade, real thumbnail from `i.ytimg.com`) — `home-improved.html`
- Google Fonts (`fonts.googleapis.com`, `fonts.gstatic.com`)

## Before go-live (production domain cutover)
Do **not** point praxis-huewel.de at this repo until every unchecked item above is done — see the full checklist's "Fast-track MVP" section for the non-negotiable minimum. The two items most likely to be missed because GitHub Pages hides them (no error, just silent absence) are the **security headers** (needs Cloudflare in front) and the **HWG §11 testimonial review** (needs a human legal call, not a technical fix).
