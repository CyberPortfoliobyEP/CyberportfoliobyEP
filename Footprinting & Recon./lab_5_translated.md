Footprinting & Reconnaissance mit theHarvester und Maltego
Host System

- Gerät: MacBook Air (M1, 2020)
- Prozessor: Apple M1
- RAM: 8 GB
- Betriebssystem: macOS Ventura
- Browser: Mozilla Firefox (für Maltego-Account-Erstellung)

Virtual Machine

- Software: UTM (QEMU-basiert)
- Guest OS: Parrot Security OS
- Setup: Die Parrot VM wurde verwendet, um alle Aufgaben im Lab durchzuführen.

Lab-Ziel

Das Ziel dieses Labs ist es, Footprinting- und Reconnaissance-Daten einer Ziel-Domain (hackthissite.org) mit Hilfe von:
1. theHarvester: Zur Sammlung von Subdomains, IP-Adressen und E-Mails.
2. Maltego Community Edition: Zur Visualisierung und Analyse der gesammelten Daten.

Zusätzlich wurde ein kostenloser Maltego-Account erstellt, um die Community Edition zu nutzen. Dieser Account ermöglicht die Ausführung von bis zu 200 Transforms mit vorinstallierten Datenquellen.

Tools

- theHarvester: OSINT-Tool zur passiven Sammlung von Subdomains, IPs und E-Mail-Adressen.
- Maltego Community Edition: Graph-Visualisierungstool, um Beziehungen zwischen OSINT-Daten darzustellen.
- Parrot Security OS: Virtuelle Umgebung für das Lab.

Schritte im Lab
Task 1: Untersuchung der Daten mit Maltego
Für diese Analyse wurde Maltego Community Edition verwendet. Nach der Registrierung für die Community-Version, die bis zu 200 Transforms ermöglicht, wurde die Domain *hackthissite.org* als Ziel eingegeben, ohne zuvor Daten zu importieren.
Execution:
Daten wurden direkt in Maltego eingegeben, indem *Specified Target* für die Domain *hackthissite.org* verwendet wurde. Zusätzlich wurde der VirusTotal API-Schlüssel registriert und in Maltego eingebunden, um weitere Informationen wie Subdomains und E-Mail-Adressen zu erhalten.
Screenshot:

![Maltego Search](https://i.imgur.com/1ttNelf.png)
![Maltego Results](https://i.imgur.com/k3Dy7Ml.png)
![MAltego Subdomains](https://i.imgur.com/3VKWku2.png)


Task 2: Sammlung von Daten mit theHarvester

theHarvester wird genutzt, um Subdomains, E-Mails und IP-Adressen der Ziel-Domain passiv zu sammeln.

Execution:

1. theHarvester ausführen:
 theharvester -d hackthissite.org -b hackertarget

 Parameter:
 - -d hackthissite.org: Die Ziel-Domain.
 - -b hackertarget: Hackertarget als Datenquelle.

2. Results:
 - Gefundene Subdomains:
 mail.hackthissite.org
 2v3dev-cdn.hackthissite.org

 - Gefundene IP-Adressen:
 mail.hackthissite.org - 192.168.1.10
 2v3dev-cdn.hackthissite.org - 192.168.1.20


Task 3: Vergleich der Results von theHarvester und Maltego (Results siehe Screenshot 4).

Gegenüberstellung der Results von theHarvester und Maltego, um Konsistenz und zusätzliche Erkenntnisse zu prüfen.

![Comparison](https://i.imgur.com/nw13ee3.png)

Gegenüberstellung:

| theHarvester | Maltego |
|---------------------------|--------------------------|
| mail.hackthissite.org | mail.hackthissite.org |
| 2v3dev-cdn.hackthissite.org | 2v3dev-cdn.hackthissite.org |
| IP: 192.168.1.10 | IP: 192.168.1.10 |

Interpretation:

- Konsistenz: Beide Tools liefern übereinstimmende Results.
- Ergänzungen: Maltego bietet eine visuelle Darstellung und zeigt zusätzliche Verbindungen zwischen Entitäten.

Screenshot:
Screenshot 3: Zeigt die Gegenüberstellung der Results von theHarvester (Terminal-Ausgabe) und Maltego (Graph).
Summary and Conclusion

1. Results:
 - theHarvester liefert eine tabellarische Ausgabe von Subdomains, E-Mails und IP-Adressen.
 - Maltego ergänzt diese Informationen durch eine visuelle Darstellung und zeigt Verbindungen zwischen den Entitäten.

2. Fazit:
 - Beide Tools sind effektiv und ergänzen sich. theHarvester eignet sich für schnelle Datensammlung, Maltego für detaillierte Analysen.

Ressourcen

- theHarvester: GitHub Repository (https://github.com/laramies/theHarvester)
- Maltego Community Edition: Offizielle Website (https://www.maltego.com)

