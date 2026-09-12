# Gesundheitspraxis im Nürbanum – Martin Hüwel (Website)

Owned, custom rebuild of praxis-huewel.de — static, fast, editable via the 741 chat workflow.
Replaces the rented ONLY INSIDE CMS. This repo IS the site (he owns the code).

## Homepage
`index.html` — recreation of the current homepage (same content, images, header, footer),
rebuilt in the **improved brand system** (not pixel-perfect, improved per 741 recommendations).

---

## 1. Branding tech setup (design system)

All brand decisions live as tokens in `assets/css/styles.css` (`:root`). Change once → whole site updates.

### Colours (primary green kept from the live site)
| Token | Value | Use |
|---|---|---|
| `--green` | `#426C00` | Primary (buttons, links, accents) |
| `--green-dark` | `#2E4B00` | Hover, headings-on-light, CTA band |
| `--green-soft` | `#5C8A12` | Focus ring, light accent |
| `--green-bg` | `#EEF3E4` | Tint surfaces |
| `--sand` | `#F6F2E9` | Section ground |
| `--cream` | `#FBF9F3` | Page ground |
| `--taupe` | `#B9B3A5` | Muted (kept from live palette) |
| `--gold` | `#C0872E` | Small accent (stars) |
| `--ink` `--soft` `--line` | `#26291F` `#5c5f54` `#E7E2D4` | Text / secondary / borders |

**Improvement vs. live:** the old site had only green + taupe + greys and no CTA/hover/ground tokens.
This adds a documented, consistent token set.

### Typography (improvement — old site was generic Helvetica)
- **Headings:** `Fraunces` (warm humanist serif → trust + experience)
- **Body:** `Inter` (clean, highly legible)
- Loaded via Google Fonts in `index.html` (swap the `<link>` + `--font-*` tokens to change).

### Other brand assets to finish (GAPs from the branding audit)
- Logo as **SVG + transparent PNG** (currently a 480×480 JPG), favicon, theme-color.
- Replace remaining **stock imagery** with real practice photos; descriptive alt-texts (done on homepage).
- Branded OG/social image.

---

## 2. Recommended stack (owned, 741-style)

| Layer | Choice |
|---|---|
| Front-end | Static HTML/CSS (this repo). Can grow into Vite/Handlebars partials for shared header/footer. |
| Editing / deploy | Claude (chat) → git → auto-deploy |
| Hosting / CDN / SSL | Cloudflare Pages or Netlify (domain praxis-huewel.de) |
| Forms → leads | Serverless function → **Supabase** + auto-reply via **Resend** *(contact form action = TODO)* |
| CRM / contacts | Supabase (contacts, notes, source, birthday, consent) |
| Email + automation | Resend + Supabase scheduled functions (newsletter, appointment, birthday) |
| Booking | Cal.com embed on /termine |
| Consent / DSGVO | Consent-Mode-v2 banner + Impressum/Datenschutz |
| SEO / GEO | JSON-LD (MedicalBusiness/Person, Service, FAQPage), sitemap.xml, canonicals, OG |
| Analytics | GA4 + GSC |

---

## 3. Structure
```
index.html              # homepage (improved)
assets/css/styles.css   # design tokens + components + page styles
```
Next pages reuse the same header/footer + tokens: `was-ist-ihr-anliegen.html`,
`methoden-als-werkzeuge*.html`, `der-wartezeit-vermeider.html`, `ueber-mich.html`,
`blog.html`, `termine.html`, `kontakt.html`, `impressum.html`, `datenschutz.html`.

## 4. Run locally
```bash
python3 -m http.server 8799
# open http://localhost:8799/index.html
```

## 5. TODO before go-live
- Wire the contact form to Supabase + Resend (currently `action="#"`, honeypot in place).
- Logo SVG + favicon; branded OG image.
- Real photos where stock remains; keep alt-texts descriptive.
- Build remaining pages; generate a correct sitemap.xml (the live one is stale).
- Consent banner + GA4; Cal.com on /termine.
