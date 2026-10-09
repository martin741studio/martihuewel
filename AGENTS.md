# Arbeitsregeln für KI-Assistenten – Website Praxis Hüwel

Diese Datei gilt für jede KI, die in diesem Repository arbeitet (Claude, ChatGPT, Copilot, Cursor und andere).
Lies sie ganz, **bevor** du etwas änderst. Es sind feste Regeln, keine Vorschläge.

## 1. Wer arbeitet hier?

- **Martin Hüwel** ist Heilpraktiker in Nürnberg und der Inhaber der Praxis. Er ist **kein Entwickler**.
  Er ändert Texte, Bilder und Seiten im Chat mit dir.
- **741 Studio (Martin Drendel)** hat die Seite gebaut, besitzt das Repository und prüft jede Änderung, bevor sie live geht.
- Sprich mit Martin Hüwel in **einfachem Deutsch**. Keine Fachbegriffe wie „Branch“, „Commit“, „Merge“, ohne sie kurz zu erklären.
  Erkläre nach jeder Aufgabe in zwei bis vier Sätzen, was du getan hast.
- Die Website selbst spricht Besucher mit **Sie** an.

## 2. Das Wichtigste in einem Absatz

Die Seite ist statisches HTML auf GitHub Pages. Jede Änderung auf dem Zweig `main` ist nach 1–2 Minuten **öffentlich live**.
Darum arbeitest du **nie direkt auf `main`**. Du arbeitest auf einem eigenen Zweig, startest die Prüfung, öffnest einen Pull Request und wartest auf die Freigabe von 741 Studio.
Jeder Stand bleibt in Git gespeichert. Du kannst jede Änderung zurückholen (siehe Abschnitt 8).

## 3. Arbeitsablauf – immer in dieser Reihenfolge

### Schritt 1: Verstehen (frag genug nach)

Bevor du eine Datei änderst, stelle Fragen, bis du die Aufgabe sicher verstanden hast. Rate nie.
Stelle höchstens drei Fragen auf einmal und warte auf die Antworten.
Wenn Martin „mach einfach“ sagt, nenne trotzdem die offenen Punkte und lass sie von ihm bestätigen.

**Fragen je nach Aufgabe:**

*Text ändern*
- Auf welcher Seite und in welchem Abschnitt? (Zeige ihm den aktuellen Text.)
- Welcher Text soll genau dort stehen? Woher stammt er?
- Enthält er Aussagen zu Wirkung, Heilung, Krankheiten oder Studien? (Dann prüfe Abschnitt 5.)

*Neue Seite*
- Worum geht es, und wen soll die Seite ansprechen?
- Nach welchem Suchbegriff sollen Patienten suchen (zum Beispiel „Ondamed Nürnberg“)?
- Wo soll sie im Menü stehen? Welche bestehenden Seiten sollen auf sie verlinken?
- Auf welche bestehenden Seiten soll sie verlinken?
- Gibt es ein passendes Bild? Wer hat es gemacht, und darf die Praxis es nutzen?
- Schreibt Martin den Text, oder soll die KI einen Entwurf machen? (Entwurf immer von Martin prüfen lassen.)
- Kommen Preise, Zeiten oder Kontaktwege vor? Sind sie aktuell?

*Bild hinzufügen*
- Was zeigt das Bild genau? (Sieh es dir an, bevor du etwas darüber schreibst.)
- Wer hat es aufgenommen oder erstellt? Gibt es das Recht zur Nutzung?
- Sind Personen zu sehen? Dann ist eine **schriftliche Einwilligung** nötig.
- Auf welche Seite und an welche Stelle kommt es?

*Blogartikel*
- Titel, Datum, Autor, Titelbild und Quelle des Textes.
- Soll der Artikel in der Liste `blog.html` und bei „Weitere Beiträge“ erscheinen?

*Preis oder Paket ändern*
- Woher stammt die Zahl, und ab wann gilt sie? Auf welchen Seiten steht der Preis? (Suche nach allen Stellen.)

*Seite offline nehmen*
- Warum? Auf welche Seite sollen Besucher stattdessen kommen? (Siehe Abschnitt 7.)

### Schritt 2: Plan nennen und Bestätigung holen

Schreibe in einfachen Worten: „Ich ändere diese Dateien. Das ändert sich. Das bleibt gleich.“
Warte auf ein klares „Ja“. Ein „Ja“ gilt nur für diesen einen Plan.

### Hinweis für Cloud-Werkzeuge (zum Beispiel ChatGPT Codex)

- Das Werkzeug legt den Arbeitszweig oft selbst an. Benutze ihn. Speichere nie auf `main`.
- Du hast evtl. kein Internet und keinen Browser. Dann prüfst du nur mit den beiden Skripten (Schritt 4). Sage Martin klar: „Ich konnte die Seite nicht im Browser ansehen. 741 Studio prüft die Vorschau.“
- Du erstellst den Pull Request nicht selbst. Sage Martin: „Klicke jetzt auf ‚Pull Request erstellen‘.“ Danach prüft 741 Studio.
- Lies zuerst `DESIGN.md`. Dieses Werkzeug lädt nur `AGENTS.md` automatisch.

### Schritt 3: Auf einem eigenen Zweig umsetzen

```bash
git pull
git checkout -b aenderung/JJJJ-MM-TT-kurzes-thema
```

- Ändere nur, was im Plan steht.
- Vor jedem Commit: `git status --short`. **Steht dort ein `D` (gelöscht), das nicht im Plan steht, stoppe und frage.**
  Am 07.10.2026 sind durch einen unbemerkten Löschvorgang alle Bilder von der Seite verschwunden.
- Arbeite nie in `/tmp` oder in einem temporären Ordner.

### Schritt 4: Prüfen

```bash
python3 -m http.server 8765 &
SITE=http://localhost:8765/ python3 scripts/audit.py
python3 scripts/check_repo.py --base origin/main
```

Beide Befehle müssen „alles in Ordnung“ melden. Sieh dir die Seite danach **im Browser an** (Desktop und Handybreite).
Prüfe jedes neue Bild mit eigenen Augen: Ist es scharf, passt es zum Thema, passt der Alt-Text?
**Ändere nie die Prüfskripte, um eine rote Prüfung grün zu machen.** Behebe stattdessen die Ursache oder frage 741 Studio.

### Schritt 5: Pull Request öffnen

Öffne einen Pull Request nach `main` und fülle die Vorlage aus. Merge ihn **nicht selbst**.
Sage Martin: „Ich habe die Änderung eingereicht. 741 Studio prüft sie. Danach geht sie live.“

### Schritt 6: Erklären

Schreibe Martin, was sich geändert hat, welche Seiten betroffen sind und wie er es zurückholen kann.

## 4. Was du ändern darfst – und was nicht

**Erlaubt (nach Plan und Bestätigung):**
- Texte in vorhandenen Seiten (nur im Inhaltsbereich).
- Neue Bilder in `assets/images/` und deren Einbau.
- Neue Seiten und neue Blogartikel nach dem Muster einer bestehenden Seite (Abschnitt 6).
- Titel und Beschreibung (Meta) einer Seite, wenn Martin es will.

**Gesperrt – nur mit ausdrücklicher Anweisung von 741 Studio:**
- `assets/css/styles.css` (Design). Siehe `DESIGN.md`.
- `assets/js/` (Formulare, Einbettungen, Teilen-Buttons).
- Aufbau von Kopfzeile, Menü und Fußzeile (die Links dürfen bei neuen Seiten ergänzt werden, der Aufbau bleibt).
- Die Formulare: Feld `data-form`, Adresse des Formulars, Einwilligungstext.
- `CNAME`, `robots.txt`, `.github/`, `scripts/`, `AGENTS.md`, `CLAUDE.md`, `DESIGN.md`.
- Die Weiterleitungsseiten für alte Adressen (siehe Abschnitt 7).
- Domain, DNS und E-Mail: Das liegt bei ONLY INSIDE. Niemals anfassen oder dazu raten.

Eigene Farben, Schriften, Abstände oder neue CSS-Klassen sind **nicht erlaubt**. Nutze die vorhandenen Klassen aus `DESIGN.md`.
Wenn etwas nicht mit den vorhandenen Bausteinen geht, sage es Martin und bitte 741 Studio um einen neuen Baustein.

## 5. Inhaltsregeln (Heilmittelwerbegesetz, HWG)

Die Seite einer Heilpraxis unterliegt dem HWG. Ein Verstoß kann abgemahnt werden. Darum gilt:

1. **Keine Heilversprechen.** Nicht „heilt“, „garantiert“, „sicher“, „nachweislich“. Schreibe „kann unterstützen“, „Ziel ist“, „viele Patienten berichten“.
2. **Keine Aussagen zu Krebs, Tumoren oder anderen meldepflichtigen Krankheiten.** Auch nicht indirekt.
3. **Keine Erfolgsgarantie und kein Vorher-Nachher** zu Krankheiten.
4. **Erfahrungsberichte und Fotos von Patienten** nur mit **schriftlicher Einwilligung** der Person. Prüfe, ob eine vorliegt, bevor du sie einbaust. Frage im Zweifel nach.
5. **Naturheilkunde ersetzt keine ärztliche Diagnose oder Behandlung.** Wo Gesundheitsthemen stehen, bleibt der Hinweiskasten (`hwgnote`) stehen.
6. **Nichts erfinden.** Keine Sternebewertungen, Zahlen („30 Jahre“, „über 1000 Patienten“) oder Studien ohne belegbare Quelle. Wenn eine Angabe fehlt, schreibe `[von Martin bestätigen]` und frage.
7. Namen von Ärzten, Marken oder Studien nur nennen, wenn Martin eine Quelle liefert. Der Hinweis auf Dr. Banerji steht bewusst noch aus und wird nur neutral und ohne Krankheitsaussage formuliert, nach Freigabe durch Martin.

Die Prüfung `scripts/check_repo.py` markiert Risikowörter in neuen Zeilen. Sie ersetzt keine Rechtsprüfung.

## 6. Eine neue Seite anlegen – Checkliste

Kopiere eine ähnliche bestehende Seite als Vorlage (Methode: `methoden-als-werkzeuge/ondamed-therapie.html`; Blogartikel: `artikel/homoeopathie-ist-guenstig.html`).

- [ ] Dateiname klein, mit Bindestrichen, ohne Leerzeichen und Sonderzeichen (`ondamed-therapie.html`).
- [ ] `<title>`: 25–62 Zeichen, Endung `| Praxis Hüwel`. Jeder Titel nur einmal auf der Seite.
- [ ] `<meta name="description">`: 90–160 Zeichen, nicht doppelt.
- [ ] `<link rel="canonical">` mit der vollen Adresse `https://www.praxis-huewel.de/...`.
- [ ] Open-Graph- und Twitter-Angaben (`og:title`, `og:description`, `og:image`, `twitter:card`) ausfüllen.
- [ ] JSON-LD-Block (Artikel oder Seite mit Brotkrumen) anpassen.
- [ ] **Genau eine H1.** Danach H2, H3 in dieser Reihenfolge, **keine Sprünge** (kein H2 direkt zu H4).
- [ ] Mindestens 250 Wörter Text (ausgenommen Kontakt, Impressum, Datenschutz, Termine).
- [ ] Mindestens ein Bild mit `alt`, `width` und `height`. `loading="lazy"` bei allen Bildern, die nicht gleich oben im ersten Bildschirm stehen (das große Bild ganz oben nicht).
- [ ] Pfade stimmen: in Unterordnern beginnen Links und Bilder mit `../`.
- [ ] Neue Seite in **das Menü aller Seiten** eintragen (Kopfzeile und Fußzeile), mit dem richtigen Pfad je Ordnertiefe.
- [ ] Neue Seite in `sitemap.xml` eintragen (`<loc>` mit voller Adresse, `<lastmod>` mit dem heutigen Datum).
- [ ] Mindestens **zwei** bestehende Seiten verlinken auf die neue Seite. Die neue Seite verlinkt auf passende bestehende Seiten.
- [ ] Bei Blogartikeln: Eintrag in `blog.html` und Teilen-Buttons wie bei den anderen Artikeln.
- [ ] Hinweiskasten `hwgnote`, wenn Gesundheitsthemen vorkommen.
- [ ] `scripts/audit.py` meldet keine Probleme.

## 7. Seiten umbenennen oder offline nehmen

Alte Adressen dürfen **nie** verschwinden. Auf ihnen liegen Rankings und Links von außen.

- Eine Seite wird nicht gelöscht. Sie wird eine **Weiterleitungsseite** (Muster: `schmerzen/index.html`, mit `http-equiv="refresh"`, `canonical` auf die neue Seite und ohne Menü).
- Entferne die Seite dann aus Menü, Fußzeile, internen Links und `sitemap.xml`.
- Das Löschen von Dateien ist nur erlaubt, wenn der Pull-Request-Titel `[löschen erlaubt]` enthält. Das entscheidet 741 Studio.

## 8. Wie man eine Änderung zurückholt

Alles ist in Git gespeichert. Es geht nichts verloren, solange du die Regeln befolgst.

- **Eine eingereichte Änderung rückgängig machen:** Auf GitHub den Pull Request öffnen und auf **„Revert“** klicken. Das erzeugt einen neuen Pull Request, der alles zurücksetzt.
- **Per Befehl:** `git revert <commit>` macht eine einzelne Änderung rückgängig und behält die Geschichte.
- **Eine einzelne Datei auf einen früheren Stand setzen:** `git checkout <commit-oder-tag> -- pfad/zur/datei`.
- **Fester Rückkehrpunkt:** Das Tag `stand-2026-10-09-uebergabe` ist der geprüfte Zustand bei der Übergabe. Jeder Stand danach hat ein eigenes Datum im Zweignamen.
- **Verboten:** `git push --force`, `git reset --hard` auf `main`, `git add -A` ohne vorherigen Blick auf `git status`, das Löschen und Neuanlegen des Repositories.

## 9. Datenschutz (DSGVO) – feste Regeln

- **Nichts von Dritten laden, bevor der Besucher klickt.** Keine Google Fonts, keine Skripte oder Iframes von YouTube, Google Maps, Calendly, Facebook usw. im Seitentext.
  Einbettungen laufen nur über den Klick-Baustein (`embed-gate` mit `data-embed`, Code in `assets/js/embeds.js`). Das Video auf der Startseite nutzt `youtube-nocookie.com` erst nach dem Klick.
- Schriften sind die Systemschrift „Helvetica Neue“/Arial. Keine Web-Schriften einbinden.
- **Bilder liegen im Repository** (`assets/images/`), nicht bei Fremdanbietern.
- **Keine Tracking- oder Analyse-Skripte** ohne ausdrückliche Anweisung von 741 Studio (dann mit Einwilligungsbanner).
- **Formulare** laufen nur über `assets/js/forms.js` (Funktion `site-form`). Neue Formulartypen braucht das Backend von 741 Studio. Baue keine eigenen Formulare mit fremdem Ziel.
- Keine personenbezogenen Daten (Namen, Mails, Anfragen von Patienten) in das Repository schreiben.

## 10. Bilder

- Format: `.jpg` oder `.webp`. Größe möglichst unter **220 KB** (Breite meist 1200–1600 px).
- Dateiname klein, beschreibend, mit Bindestrichen (`ondamed-behandlung-liegend.jpg`), **kein** „IMG_“, „ChatGPT“, „Screenshot“.
- `alt` beschreibt, was **wirklich** zu sehen ist. Beispiel: „Therapeut stellt das Ondamed-Gerät ein“. Nicht „Bild 1“.
- Immer `width` und `height` setzen, damit die Seite nicht springt.
- Standort-Daten (EXIF) vor dem Einbau entfernen.
- Schau jedes Bild an. Prüfe auf unleserliche Schrift, falsche Gerätenamen und Bilder, die dem Text widersprechen.
- Jede Seite braucht ein inhaltliches Bild, nicht nur das Logo.

## 11. Feste Stammdaten (nicht variieren)

Gesundheitspraxis im Nürbanum – Martin Hüwel · Heilpraktiker
Allersberger Straße 185, Gebäude A7, 3. OG · 90461 Nürnberg
Telefon 0911 6007651 · E-Mail info@praxis-huewel.de

Termine/Erreichbarkeit stehen auf den Methodenseiten so: „Termine Mo–Sa 8–20 Uhr, So 10–22 Uhr“. Übernimm genau diese Form. Ändere sie nur, wenn Martin neue Zeiten nennt, und dann auf **allen** Seiten (Suche nach „Mo–Sa“).

## 12. Technischer Überblick

- Statisches HTML/CSS/JS ohne Build. Jede Seite enthält ihre eigene Kopfzeile, ihr Menü und ihre Fußzeile. Eine Menüänderung muss darum in **allen** Seiten erfolgen.
- Hosting: GitHub Pages, Adresse `https://www.praxis-huewel.de`, Veröffentlichung automatisch nach dem Merge auf `main`.
- Formulare: `assets/js/forms.js` sendet an die Funktion `site-form` im Portal von 741 Studio (Speicherung plus E-Mail an die Praxis).
- Einbettungen: `assets/js/embeds.js` (Karte, Calendly). Teilen-Buttons: `assets/js/share.js`.
- Alte Adressen: rund 85 Weiterleitungsseiten (`http-equiv="refresh"`). Nicht löschen.
- `assets/css/exact.css` und `branding.json` sind Altlasten aus der Bauphase. Nicht verwenden.
- Die englische Version gibt es noch nicht. Lege keine englischen Seiten an, bevor 741 Studio es sagt.

## 13. Wenn du unsicher bist

Stoppe und frage Martin. Wenn es um Technik, Recht oder Design geht, schreibe an **Martin Drendel, 741 Studio** (martin@741.studio).
Eine gestellte Frage kostet eine Minute. Eine falsche Änderung auf der Live-Seite kann einen Tag kosten.
