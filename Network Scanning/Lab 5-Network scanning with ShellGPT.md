# Lab 5: Netzwerkscan mit ShellGPT (SGPT)

## Lab-Details

- **Lab-Name:** Netzwerkscan mit ShellGPT (SGPT)
- **Lab-Umgebung:** EC-Council iLabs
- **Lab-Ziel:** Durchführung von ICMP-Scans, Host Discovery, XMAS-Scans und Firewall-/Betriebssystem-Scans zur Identifikation von Schwachstellen und Systeminformationen.
- **Verwendete Ressourcen:**
  - **Angreifermaschine:** Parrot Security OS
  - **Zielmaschine:** Windows 11 (IP-Adresse: 10.10.1.11, Subnetz: 10.10.1.0/24)
  - **Tools:**
    - **ShellGPT:** KI-gestütztes Netzwerkscanning-Tool
    - **Nmap:** Tool für spezifische Netzwerkscans wie XMAS- und Firewall-Scans
- **Vorbereitung:** Die ShellGPT-API muss integriert sein. Befolge dazu die Anleitung in "Integrate ShellGPT in Parrot Security Machine".

## Einleitung

Dieses Lab demonstriert den Einsatz von ShellGPT für Netzwerkscans. Der Fokus liegt auf der Erreichbarkeit der Zielmaschine mittels ICMP-Scans, der Identifikation aktiver Hosts und der Durchführung von XMAS-Scans, Firewall-Scans und Betriebssystem-Scans, um Schwachstellen sowie System- und Firewall-Informationen zu identifizieren.

---

## Task 1: ICMP-Scan

- **Command**:  
`sgpt --chat scan --shell "Use hping3 to perform ICMP scanning on the target IP address 10.10.1.11 and stop after 10 iterations"´

      ![Results](https://i.imgur.com/Dieq4AT.png)
  
- **Beschreibung:** Hping3 ist ein flexibles Netzwerktool, das benutzerdefinierte Pakete generieren und senden kann. Es unterstützt uns dabei, spezifische ICMP-Pakete an die Ziel-IP 10.10.1.11 zu senden, um deren Erreichbarkeit zu überprüfen und Antwortzeiten zu messen.
- **Ergebnisse:** Alle 10 ICMP-Pakete wurden erfolgreich beantwortet. Die durchschnittliche Antwortzeit betrug 1,2 ms.

---

## Task 2: Host Discovery

- **Command**: 
`sgpt --chat scan --shell "Perform an XMAS scan on the first two targets from the file scan1.txt"´

      ![Results](https://i.imgur.com/RysfcYI.png)
  
- **Beschreibung:** Identifiziert aktive Hosts im Subnetz 10.10.1.0/24. Die IP-Adressen der Hosts werden in `scan1.txt` gespeichert.
- **Ergebnisse:** Es wurden 5 aktive Hosts identifiziert: 10.10.1.11, 10.10.1.12, 10.10.1.13, 10.10.1.14, 10.10.1.15.

---

## Task 3: XMAS-Scan

- **Command**: 
`sgpt --chat scan --shell "Perform an XMAS scan on the first two targets from the file scan1.txt"`

      ![Results](https://i.imgur.com/GM9lepL.png)
      
- **Beschreibung:** Der XMAS-Scan sendet spezielle TCP-Pakete mit den Flags FIN, PSH, und URG, um Schwachstellen wie nicht blockierte Ports oder offene Firewalls zu identifizieren. Obwohl der Befehl angibt, die ersten zwei Ziele aus `scan1.txt` zu scannen, wurden in diesem Fall drei IP-Adressen gescannt.
- **Ergebnisse:** Auf 10.10.1.9 und 10.10.1.10 wurden keine auffälligen Ports identifiziert. Auf 10.10.1.11 wurden zwei Schwachstellen auf den Ports 80 (HTTP) und 443 (HTTPS) gefunden.

---

## Task 4: Firewall- und Betriebssystem-Scan

- **Command**: 
`sgpt --chat scan --shell "Discover if there is any Firewall active on the subnet 10.10.1.0/24 and then find the list of the IP addresses of the firewalls and operating systems"´

      ![Results](https://i.imgur.com/gaxro3n.png)

- **Beschreibung:** Mithilfe von ShellGPT und Nmap wurde geprüft, ob Firewalls aktiv sind, und gleichzeitig versucht, Betriebssysteme zu identifizieren. Die Ergebnisse wurden in zwei Dateien gespeichert: `firewalls.txt` und `os_info.txt`.
- **Ergebnisse:** Firewall-Aktivität wurde bei folgenden Hosts festgestellt: 10.10.1.14 (Microsoft Windows 10 mit aktiver Stateful Firewall), 10.10.1.19 (FreeBSD 11.X). Betriebssysteme wurden für die folgenden Hosts identifiziert: 10.10.1.11 (Linux 4.X/5.X), 10.10.1.14 (Microsoft Windows 10).

---

## Zusammenfassung

- **Schritte:**
  1. ICMP-Scan zur Überprüfung der Erreichbarkeit der Zielmaschine.
  2. Identifikation von aktiven Hosts im Subnetz und Speicherung in `scan1.txt`.
  3. Durchführung eines XMAS-Scans auf die ersten beiden Ziel-IPs aus `scan1.txt`.
  4. Durchführung eines Firewall- und Betriebssystem-Scans, Erkennung von Firewalls und Systemdetails.

- **Ergebnisse der Scans:**
  - Der ICMP-Scan bestätigte die Erreichbarkeit der Zielmaschine.
  - Der XMAS-Scan zeigte Schwachstellen auf den Ports 80 und 443 bei 10.10.1.11.
  - Der Firewall-Scan zeigte aktive Stateful Firewalls, insbesondere bei Windows-Hosts.
  - Die Betriebssystemanalyse deckte verschiedene Systeme wie Linux und Windows auf.

- **Empfehlungen:**
Regelmäßige Netzwerkscans durchführen, um Schwachstellen frühzeitig zu erkennen. Firewall- und Sicherheitskonfigurationen verbessern in dem die OS und offene Ports nicht aufgedeckt werden.
