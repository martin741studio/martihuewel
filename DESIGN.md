# Design-Richtlinie – Website Praxis Hüwel

Das Design ist **gesperrt**. Martin Hüwel und seine KI ändern Inhalte (Text, Bilder, Seiten), aber nicht das Aussehen.
Änderungen am Design macht nur 741 Studio, und zwar an einer Stelle: `assets/css/styles.css`.
Diese Datei beschreibt, was erlaubt ist und welche Bausteine du benutzen darfst.

## 1. Grundsatz

- **Nur vorhandene Bausteine.** Jede Seite wird aus den Klassen in `assets/css/styles.css` gebaut.
- **Keine eigenen Stile.** Kein `style="color:..."`, kein neues `<style>`, keine neue CSS-Datei, keine neue Schrift.
  Die wenigen vorhandenen `style="margin-top:..."`-Abstände in bestehenden Seiten bleiben, neue kommen nicht dazu.
- **Farben nur über Variablen** (`var(--green)` usw.). Keine Farbcodes im Seitentext.
- Fehlt ein Baustein, sagt die KI das Martin. 741 Studio baut ihn dann einmal, und danach steht er für alle Seiten bereit.

## 2. Design-Werte (Tokens)

Sie stehen in `assets/css/styles.css` im Block `:root`.

| Variable | Wert | Verwendung |
|---|---|---|
| `--green` | `#426C00` | Hauptfarbe (Buttons, Links, Akzente) |
| `--green-dark` | `#2E4B00` | Hover, dunkle Flächen |
| `--green-soft` | `#5C8A12` | Fokus, helle Akzente |
| `--green-bg` | `#EEF3E4` | helle grüne Fläche |
| `--sand` | `#F6F2E9` | Abschnittshintergrund |
| `--cream` | `#FBF9F3` | Seitenhintergrund |
| `--taupe` | `#B9B3A5` | gedämpfte Linien und Beschriftungen |
| `--gold` | `#C0872E` | kleiner Akzent (Sterne) |
| `--ink` | `#26291F` | Text und Überschriften |
| `--soft` | `#5c5f54` | zweiter Text |
| `--line` | `#E7E2D4` | Rahmen |
| `--ok` `--warn` `--err` | grün / orange / rot | Meldungen im Formular |

- **Schrift:** „Helvetica Neue“, Helvetica, Arial (Systemschrift, nichts wird nachgeladen).
- **Breite des Inhalts:** 1120 px (`.wrap`). **Rundung:** 14 px. Basisschrift 17 px.
- **Logo:** `assets/images/praxis-huewel-logo.jpg`. Nicht verändern, nicht ersetzen.

## 3. Seitenaufbau (Reihenfolge fest)

1. `<head>` mit Titel, Beschreibung, Canonical, Open Graph, Icons, `styles.css`, JSON-LD.
2. `.topbar` (Name, Telefon, E-Mail).
3. `<header class="site-header">` mit Logo und Menü.
4. Inhalt: Hero, dann Abschnitte (`<section>`), dann Abschluss-CTA.
5. `<footer>`.
6. `.sticky` (Anruf- und Termin-Knopf für Handys) und Jahres-Skript.

Kopf, Menü, Fußzeile und Sticky-Leiste kopierst du **unverändert** aus einer bestehenden Seite derselben Ordnertiefe.
Nur die Links und Bilder müssen zu `../` passen, wenn die Seite in einem Unterordner liegt.

## 4. Erlaubte Bausteine

Jeder Baustein steht schon in einer bestehenden Seite. Kopiere ihn von dort.

| Baustein | Klassen | Beispiel zum Kopieren |
|---|---|---|
| Hero mit H1, Text, Knöpfen, Bild | `.hero`, `.eyebrow`, `.hero-cta`, `.hero-img`, `.btn`, `.btn-ghost`, `.btn-lg` | `methoden-als-werkzeuge/ondamed-therapie.html` |
| Normaler Abschnitt | `<section><div class="wrap">…`, `section.sand` für hellen Hintergrund | jede Seite |
| Einleitungstext | `.lead` | `methoden-als-werkzeuge/ondamed-therapie.html` |
| Definitionsbox | `.defbox` | `methoden-als-werkzeuge/ondamed-therapie.html` |
| Karten (2 oder 3 Spalten) | `.grid .g2`, `.grid .g3`, `.card` | `index.html` |
| Haken-Liste | `.check` | `nebennierenschwäche.html` |
| Schritte 1-2-3 | `.steps`, `.step`, `.n` | `index.html` |
| Häufige Fragen | `.faq`, `<details>`, `.a` | `nebennierenschwäche.html` |
| Behandlungspakete | `.pkgs`, `.card.pkg`, `.pkg-list`, `.price`, `.pkg-note` | `index.html` (`#pakete`) |
| Erfahrungsbericht | `.quote`, `.who`, `.av`, `.stars` | `index.html` (nur mit schriftlicher Einwilligung) |
| Video mit Klick-Vorschau | `.video`, `.play`, `.video-note` | `index.html` (`#yt-video`) |
| Karte / Kalender mit Klick | `.embed-gate` mit `data-embed="map"` oder `"calendly"` | Karte: `kontakt.html`; Kalender: `index.html` |
| Hinweis (Heilmittelwerbegesetz) | `.hwgnote` | jede Methodenseite |
| Abschluss-Aufruf | `section.sand#kontakt` mit `.center`, `.eyebrow`, `.btn-lg` | jede Methodenseite |
| Artikeltext | `.article-body`, `.article-img`, `.share`, `.related` | `artikel/homoeopathie-ist-guenstig.html` |
| Formular | `.form` mit `data-form="home"`, `"kontakt"` oder `"wartezeit"` | `kontakt.html` – **nur mit 741 Studio ändern** |

**Überschriften:** Genau eine `<h1>` je Seite. Für die Optik einer kleineren Überschrift mit richtiger Reihenfolge gibt es `.as-h1` bis `.as-h4`
(zum Beispiel `<h2 class="as-h3">`). Keine Sprünge in der Reihenfolge.

**Knöpfe:** `.btn` (grün, Hauptaktion), `.btn-ghost` (Umriss, zweite Aktion), `.btn-white` (auf dunklem Grund), `.btn-lg` (groß).
Pro Bildschirm höchstens ein Hauptknopf.

## 5. Bilder im Design

- Hero-Bild: `fetchpriority="high"`, mit `width` und `height`, kein `loading="lazy"`.
- Alle anderen Bilder: `loading="lazy"`, mit `width`, `height` und beschreibendem `alt`.
- Seitenverhältnis: Hero 16:9 oder 3:2. Avatare quadratisch (300 × 300 px).
- Freigestellte Personenfotos und Patientenbilder nur mit schriftlicher Einwilligung.

## 6. Ton und Sprache

- Besucher-Ansprache: **Sie**. Der Ton ist ruhig, klar und warm. Keine Ausrufezeichen-Ketten, kein Fachjargon ohne Erklärung.
- Absätze kurz (höchstens fünf Sätze). Zwischenüberschriften alle 150–250 Wörter.
- Gesundheitsaussagen: „kann unterstützen“, „Ziel ist“, nie „heilt“ oder „garantiert“ (siehe `AGENTS.md`, Abschnitt 5).
- Die Praxis heißt „Gesundheitspraxis im Nürbanum“, der Inhaber „Martin Hüwel“. Schreibweise nicht variieren.

## 7. Prüfwerte

Diese Grenzen prüft `scripts/audit.py` bei jedem Pull Request:

| Prüfung | Grenze |
|---|---|
| Titel | 25–62 Zeichen, nicht doppelt |
| Beschreibung | 90–160 Zeichen, nicht doppelt |
| H1 | genau eine |
| Überschriften | keine Sprünge |
| Bilder | `alt`, `width`, `height` vorhanden, unter 220 KB |
| Links und Dateien | keine toten Adressen |
| Text | mindestens 250 Wörter (außer Kontakt, Impressum, Datenschutz, Termine, Blog-Übersicht) |
| Interne Links | mindestens zwei Links von anderen Seiten auf jede Seite |
| Metadaten | Canonical, Open Graph, Twitter-Karte, JSON-LD |

## 8. Was 741 Studio ändert

Neue Bausteine, Farben, Schriften, das Menü-Konzept, neue Formulartypen, Tracking, die englische Version
und alles in `assets/css/styles.css` und `assets/js/`.

