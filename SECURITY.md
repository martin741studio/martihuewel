# Security & Safety — Praxis Hüwel

Project-specific status against 741's standard checklist (master version: `00_project/website-security-checklist.md` in the 741 studio repo). Update the checkboxes as items land; don't remove items just because they're not done yet.

## Current status (MVP / homepage-only stage)

- [x] Static site, no server-side app code to exploit.
- [x] Honeypot field on the contact form (`index.html` / `home-improved.html`).
- [x] `.gitignore` covers `.env*`, `node_modules/`, `.DS_Store`.
- [x] Repo public — acceptable at this stage (no secrets, no backend keys in-repo).
- [x] HWG disclaimer present wherever methods/treatments are described.
- [x] No cure/healing-guarantee claims; testimonials reviewed for HWG §11.
- [x] Consent checkbox (unchecked by default) on the contact form, linked to Datenschutzerklärung.
- [ ] **HTTPS + HSTS + security headers** — pending real hosting choice (Cloudflare Pages / Netlify).
- [ ] **Cloudflare Turnstile on the contact form** — add once form has a real backend (see below).
- [ ] **Form backend (Supabase Edge Function + Resend)** — form currently has `action="#"`, no live submit target yet. Needs: RLS-protected table, server-side validation, rate limiting.
- [ ] **SPF/DKIM/DMARC** — set up once the sending domain/email (Resend) is configured.
- [ ] **Cookie/consent banner + Consent Mode v2** — needed before GA4 or any tracking script is added.
- [ ] **AV-Verträge** (Supabase, Resend, Cal.com, host) — needed before any personal data actually flows through them.
- [ ] Uptime monitoring — set up once this is the production domain.

## Before go-live (production domain cutover)
Do **not** point praxis-huewel.de at this repo until every unchecked item above is done — see the full checklist's "Fast-track MVP" section for the non-negotiable minimum.
