# Praxis Hüwel Website — Agent Instructions

Read this file and `branding.json` **before** writing or changing any page. These are hard
constraints, not suggestions.

## What this repo is
Owned, static rebuild of praxis-huewel.de (Heilpraktiker Martin Hüwel, Nürnberg), replacing
a rented CMS. Edited by AI agents via chat/git, deployed as plain HTML/CSS. No page builder,
no CMS backend for the front-end.

## Files to read first
1. `branding.json` — the full brand audit: current colors, typography, logo, imagery,
   voice, NAP, SEO meta. Every missing/undefined item is flagged `"GAP"` — those are open
   decisions, not facts to invent.
2. `README.md` — recommended stack (hosting, forms/CRM, email, booking, SEO, consent) and
   file structure.
3. `SECURITY.md` — security/safety checklist status for this project (forms, backend,
   DSGVO, headers). Check it before adding any form, backend call, or third-party script;
   don't ship a form with a live submit target until its backend items are done.
4. `assets/css/styles.css` — design tokens (`:root`) for the **improved** brand system.
   `assets/css/exact.css` — tokens for the **exact/current**-brand rebuild. Do not mix them.

## Non-negotiable rules (violating these caused real client complaints — do not repeat)

1. **Two distinct deliverables exist. Never blur them.**
   - `index.html` = **exact rebuild**: current live copy, verbatim, current brand only
     (Helvetica, `#426C00` green, `#B9B3A5` taupe). No new fonts, no new sections, no
     rewritten wording.
   - `home-improved.html` = **improved version**: same real content, upgraded design
     system (tokens in `styles.css`). Improve layout/spacing/hierarchy — never rewrite,
     shorten, or paraphrase the client's copy, and never invent supporting claims.
   - When asked for "exact," deliver exact. When asked for "improved," deliver improved.
     When asked for both, deliver both as separate files — never only one.

2. **Content must be verbatim when sourced from the client's site or an approved doc.**
   No paraphrasing "to improve flow." If content needs to change, that's a separate,
   explicit request — pull the *new* approved text from its actual source (the website
   tree/Seitenbaum report or the linked Google Doc), don't reword the old text yourself.

3. **No fabricated trust signals or claims.** No star ratings, review counts, "30+ years"
   badges, or stats unless they come from a verified source. If a number isn't confirmed,
   mark it `GAP` / `[von Kunde bestätigen]` — never invent one to fill a design slot.

4. **Never swap brand identity elements without an explicit request.** Typography, color
   palette, logo, tone — these are locked to what's in `branding.json` unless the task
   explicitly asks for a brand change. "Improve the design" means better use of the
   existing brand, not a new one.

5. **Image ↔ caption/alt-text must match the real image content.** Never caption or
   alt-text an image as something it isn't (e.g. a product graphic is not a "video
   preview of Martin"). If unsure what an image shows, describe it generically or ask —
   don't guess and assert.

6. **Health/medical content (HWG, Germany):** no healing promises, no guaranteed results.
   Use "kann / Ziel ist / unterstützt." Every page needs an HWG disclaimer where health
   claims appear. Naturheilkunde never replaces ärztliche Diagnose/Behandlung — say so.

7. **Before delivering any page or block, verify it against its source and the explicit
   ask** — diff the actual text/images used against the source, and check each requirement
   in the request was met, before committing. Do this per block, not only at the end.

8. **Every page needs a real, client-sourced content image — never ship a page with only
   the shared header logo.** Before writing a new page, check both: (a) images already
   live on the current site (`branding.json` → note URLs are on `static.only-inside.de`,
   confirm each still resolves), and (b) the client's Drive `Assets` folder for newer
   photos. **Open and visually inspect every candidate image before using it** — do not
   trust a filename. A file named like an AI-tool export (e.g. "ChatGPT Image ...") is a
   red flag; open it and check for tells (garbled text on diplomas/signage/book spines,
   an office that doesn't match the client's real one) before ruling it in or out. Never
   use an AI-generated image as if it were a real photo of the practice, practitioner, or
   a patient. If a photo shows a detail that contradicts existing site copy (e.g. a
   different device brand than what the text names), don't silently pick a side — use a
   neutral image instead and flag the discrepancy for the client to resolve.

## NAP (locked, from `branding.json`)
Gesundheitspraxis im Nürbanum – Martin Hüwel · Allersberger Straße 185, Gebäude A7, 3. OG,
90461 Nürnberg · 0911 6007651 · info@praxis-huewel.de · Mo–Sa 08:00–20:00, So 10:00–22:00.
Use exactly this — never a variant.

## Current task queue
- New homepage version: start from `home-improved.html` (design system, header, footer
  unchanged), replace the copy with the finalized Startseite text from the website-tree/
  Seitenbaum report (not the old live copy).
- Reuse real images already live on the current homepage where they genuinely fit the
  new content (see `branding.json` → note real image URLs are on `static.only-inside.de`,
  confirm each one still resolves before using it).
