# Website Praxis Hüwel – www.praxis-huewel.de

Gesundheitspraxis im Nürbanum · Martin Hüwel · Heilpraktiker · Nürnberg

Dies ist der gesamte Code der Website. Die Seite gehört dir. 741 Studio verwaltet das Repository und betreut die Technik.
Du kannst Texte, Bilder und neue Seiten im Chat mit einer KI ändern. Die Regeln dafür stehen in dieser Datei und in `AGENTS.md`.

## So arbeitest du mit der KI

**1. Öffne das Repository mit deinem KI-Werkzeug.** Zum Beispiel Claude Code, Cursor oder Copilot. 741 Studio zeigt dir die Einrichtung einmal.

**2. Beginne jede Sitzung mit diesem Satz:**

> Lies zuerst `AGENTS.md` und `DESIGN.md`. Ich bin Martin Hüwel, Heilpraktiker, und kein Entwickler. Erkläre alles einfach. Stelle mir Fragen, bis du die Aufgabe sicher verstanden hast, und sage mir den Plan, bevor du etwas änderst.

**3. Sage, was du willst.** Zum Beispiel:
- „Auf der Seite Homöopathie soll im ersten Absatz stehen: …“
- „Lege eine neue Seite zu Bioresonanz bei Allergien an.“
- „Ich habe ein neues Foto vom Behandlungsraum. Baue es auf der Seite Über mich ein.“
- „Nimm die Seite Vitalstoffanalyse aus dem Menü.“

**4. Beantworte die Fragen der KI.** Sie fragt nach Seite, Text, Bildrechten und Einwilligungen. Das schützt dich vor Fehlern und vor Abmahnungen.

**5. Bestätige den Plan.** Die KI nennt, was sie ändert. Antworte mit „Ja“ oder sage, was anders sein soll.

**6. Die KI reicht die Änderung ein.** Sie arbeitet auf einer Kopie und prüft sie automatisch (kaputte Links, Bilder, Titel, Überschriften). Danach prüft 741 Studio sie.

**7. Nach der Freigabe ist die Änderung nach 1–2 Minuten auf der Seite.**

## Was die KI nicht ändert

Das Design (Farben, Schrift, Abstände), die Formulare, die Technik, die Domain und die E-Mail.
Das schützt die Seite. Wenn du eine Design-Änderung willst, schreibe an 741 Studio.

## Wenn etwas schiefgeht – zurückholen

Nichts geht verloren. Jede Änderung bleibt gespeichert.

- **Nach dem Live-Gang:** Öffne die Änderung auf GitHub (Reiter „Pull requests“, Filter „Closed“) und klicke **Revert**. 741 Studio gibt das Zurücksetzen frei, dann ist die alte Version in 1–2 Minuten wieder da.
- **Vorher abbrechen:** Sage der KI „Verwirf diese Änderung“. Solange nichts freigegeben ist, ist die Live-Seite nicht betroffen.
- **Fester Rückkehrpunkt:** Der geprüfte Stand bei der Übergabe heißt `stand-2026-10-09-uebergabe`. Auf ihn kann 741 Studio jederzeit zurückgehen.
- **Dringend und niemand erreichbar:** Schreibe an martin@741.studio.

## Was gesperrt ist (Schutz der Seite)

| Bereich | Wer ändert |
|---|---|
| Texte, Bilder, neue Seiten, Blogartikel | Du mit der KI, mit Freigabe durch 741 Studio |
| Design (`assets/css/`), Skripte (`assets/js/`), Formulare | nur 741 Studio |
| Domain, DNS, E-Mail | ONLY INSIDE / 741 Studio |
| Prüfungen (`scripts/`, `.github/`) | nur 741 Studio |

Auf dem Hauptzweig `main` darf niemand direkt speichern. Jede Änderung läuft über einen Pull Request mit Prüfung.

## Wichtige Regeln in Kurzform

1. **Keine Heilversprechen**, keine Aussagen zu Krebs, keine Garantien (Heilmittelwerbegesetz).
2. **Patientenfotos und Erfahrungsberichte** nur mit schriftlicher Einwilligung.
3. **Keine erfundenen Zahlen** oder Bewertungen.
4. **Alte Adressen bleiben** (Weiterleitung statt Löschen).
5. **Nichts von Dritten laden** (Google Fonts, YouTube, Karten) ohne Klick des Besuchers.

## Für Entwickler und 741 Studio

| Datei | Inhalt |
|---|---|
| `AGENTS.md` | Regeln und Arbeitsablauf für KI-Assistenten (`CLAUDE.md` verweist darauf) |
| `DESIGN.md` | Design-Werte, erlaubte Bausteine, Prüfgrenzen |
| `scripts/audit.py` | Vollständiger Seitentest: Links, Bilder, SEO, Überschriften |
| `scripts/check_repo.py` | Repo-Regeln: Löschschutz, Fremd-Skripte, Bildnamen, Sitemap, Risikowörter |
| `.github/workflows/pruefung.yml` | Führt beide Prüfungen bei jedem Pull Request aus |
| `.github/CODEOWNERS` | Jede Änderung braucht die Freigabe von 741 Studio |
| `SECURITY.md` | Sicherheits- und Datenschutzstand (Stand der Bauphase, wird noch aktualisiert) |

**Lokal ansehen und prüfen:**

```bash
python3 -m http.server 8765
SITE=http://localhost:8765/ python3 scripts/audit.py
python3 scripts/check_repo.py --base origin/main
```

**Technik:** Statisches HTML/CSS/JS ohne Build, gehostet auf GitHub Pages (`CNAME`: `www.praxis-huewel.de`).
Formulare senden an die Funktion `site-form` im Portal von 741 Studio (Speicherung und E-Mail über Resend, Absender `info@praxis-huewel.de`).
Domain und E-Mail liegen bei ONLY INSIDE.
