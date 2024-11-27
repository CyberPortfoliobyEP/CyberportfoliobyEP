
# Lab-Bericht: Footprinting mit Social-Media-Recherche-Tools

## Einleitung

Das Ziel dieses Labs war es, persönliche und berufliche Informationen über Mitarbeiter eines Zielunternehmens zu sammeln. Mithilfe von Social-Media-Plattformen wurden öffentlich zugängliche Daten extrahiert, die potenziell für Angriffe wie Social Engineering oder andere gezielte Maßnahmen genutzt werden könnten. Dieses Lab zeigt, wie ein ethical Hacker solche Informationen strukturiert sammelt, analysiert und sicher speichert.

---

## Technische Umgebung und Tools

### Virtuelle Maschine: Kali Linux

- **Name:** E. Popal LAB – Debian Kali
- **Betriebssystem:** Debian 12.x (64-Bit ARM)
- **Prozessor:** 2 Prozessorkerne
- **Arbeitsspeicher:** 2048 MB (2 GB RAM)
- **Festplattenplatz:** 15 GB
- **Snapshots:** 2 GB

### Verwendete Tools

1. **Sherlock:** Ein Python-basiertes Open-Source-Framework zur Social-Media-Recherche.
2. **Zusätzliches Tool:** Social Searcher – ein Online-Dienst zur Analyse und Suche von Social-Media-Inhalten.

---

## Über Sherlock im Kontext von Ethical Hacking

Sherlock ist ein leistungsstarkes Tool, das Ethical Hackern erlaubt, gezielt nach öffentlich zugänglichen Social-Media-Profilen eines Zielbenutzers zu suchen. Es durchsucht hunderte Plattformen und liefert die Ergebnisse in Form von URLs. Diese können genutzt werden, um persönliche Informationen wie Namen, Positionen, Arbeitgeber oder Kontaktinformationen zu extrahieren. Dies ist essenziell für die Reconnaissance-Phase eines Ethical Hackers.

---

## Schritte und Ergebnisse

### Vorbereitung der Umgebung

Die Kali-Linux-VM wurde gestartet, um eine isolierte und sichere Arbeitsumgebung bereitzustellen. Alle Befehle wurden im Root-Terminal ausgeführt, um die benötigten Rechte zu gewährleisten.

**Command zur Aktivierung von Root-Rechten:**

```bash
sudo su
```

### Installation von Sherlock

Sherlock wurde über den Paketmanager `apt` installiert. Dieser Schritt ist notwendig, bevor das Tool verwendet werden kann.

**Command zur Installation:**

```bash
apt install sherlock
```

Hinweis: Der Befehl muss im Root-Terminal ausgeführt werden, um die entsprechenden Systemrechte zu besitzen.

**Command zur Überprüfung:**

```bash
sherlock --help
```

### Ausführung von Sherlock

Das Tool wurde verwendet, um gezielt Social-Media-Profile eines Zielbenutzers zu suchen. Für dieses Lab wurde “Thomas Müller” als Ziel ausgewählt.

**Command zur Ausführung:**

```bash
sherlock "Thomas Müller"
```

**Ergebnisse:**

- Sherlock durchsuchte zahlreiche Plattformen und lieferte eine Liste mit URLs zu Profilen, die „Thomas Müller“ enthalten.
- Beispiele für Plattformen:
  - **Twitter:** Ein Profil mit Tweets über persönliche oder berufliche Aktivitäten.
  - **Instagram:** Bilder und Videos von öffentlichen Ereignissen.
  - **YouTube:** Kanäle und Videos mit Bezug zu “Thomas Müller”.

![Screenshot Placeholder](URL_DES_SCREENSHOTS)

---

### Speichern der Ergebnisse

Um die Analyse übersichtlich zu gestalten, wurden die Ergebnisse von Sherlock in einer zuvor erstellten Textdatei gespeichert. 

**Command zur Erstellung der Datei:**

```bash
touch ~/Desktop/results_thomas_mueller.txt
```

**Command zur Speicherung der Ergebnisse:**

```bash
sherlock "Thomas Müller" --output ~/Desktop/results_thomas_mueller.txt
```

**Command zur Überprüfung des Datei-Inhalts:**

```bash
cat ~/Desktop/results_thomas_mueller.txt
```

Die gespeicherte Datei enthält folgende Informationen:
- Plattformnamen
- URLs der gefundenen Profile
- Status der Profile (z. B. aktiv oder inaktiv)

![Screenshot Placeholder](URL_DES_SCREENSHOTS)

---

### Ergänzende Suche mit Social Searcher

Zusätzlich wurde der Online-Dienst Social Searcher verwendet, um weitere Details über das Ziel zu sammeln.

**Schritte:**

1. Zugriff auf die Webseite Social Searcher.
2. Eingabe des Namens „Thomas Müller“ als Keyword.
3. Anwendung von Filtern für Plattformen (z. B. Twitter, Instagram) und Zeiträume (z. B. letzte 30 Tage).

**Ergebnisse:**

- **Twitter:** Tweets, die Thomas Müller erwähnen, inklusive Links zu beruflichen Projekten.
- **Instagram:** Beiträge mit Hashtags wie #ThomasMüller und #Projekte.
- **YouTube:** Videos über aktuelle Aktivitäten oder Projekte.

---

## Key Learnings

1. **Effektive Nutzung von Sherlock:**
   - Sherlock ist ein effizientes Tool zur Suche nach Social-Media-Profilen und erleichtert die strukturierte Informationsbeschaffung.

2. **Wichtigkeit der Speicherung:**
   - Die Speicherung der Ergebnisse in einer Textdatei ermöglicht eine einfache Dokumentation und spätere Analyse.

3. **Ergänzung durch Social Searcher:**
   - Social Searcher bietet zusätzliche Einblicke in Aktivitäten und Trends auf Social-Media-Plattformen.

4. **Technische Vorbereitung:**
   - Das Arbeiten in einer isolierten virtuellen Umgebung mit Kali Linux schützt vor ungewollten Datenlecks und gewährleistet die Integrität des Systems.

---

## Fazit

Dieses Lab demonstrierte, wie öffentlich zugängliche Daten von Social-Media-Plattformen gesammelt, analysiert und sicher gespeichert werden können. Die Kombination von Sherlock und Social Searcher bietet eine umfassende Möglichkeit, Zielinformationen zu extrahieren und zu dokumentieren. Diese Erkenntnisse unterstreichen die Bedeutung strukturierter Datenspeicherung und sicherer Workflows in der Reconnaissance-Phase.
