
# Lab-Bericht: Whois-Footprinting mit DNS Recon

## Host-System
- **Gerät:** MacBook Air (M1, 2020)
- **Prozessor:** Apple M1
- **RAM:** 8 GB
- **Betriebssystem:** macOS Sequoia 15.1.1
- **Browser:** Mozilla Firefox

## Virtuelle Maschine
- **Software:** UTM (QEMU-basiert)
- **Gast-Betriebssystem:** Parrot Security OS

## Lab-Ziel
Das Ziel dieses Labs ist die Sammlung von Informationen über Ziel-Domains durch die Nutzung von Whois und DNS Recon. Diese Tools unterstützen die Analyse von Netzwerken, Domain-Registrierungen und DNS-Daten. Die gesammelten Informationen liefern Ansätze für weitere Tests und Sicherheitsmaßnahmen.

## Task 1: Whois-Lookup

### Durchführung mit dem Terminal
```bash
whois www.certifiedhacker.com
```
**Ergebnisse:**  
Die Abfrage lieferte keine Daten. Der Befehl zeigte die Nachricht „No match for 'WWW.CERTIFIEDHACKER.COM'“. Dies deutet darauf hin, dass keine Informationen über diese Domain in der standardmäßigen Whois-Datenbank gefunden wurden.

![Screenshot Placeholder](URL_TO_SCREENSHOTS)

### Durchführung im Webbrowser
Über den Webbrowser wurde ein Whois-Lookup mit DomainTools durchgeführt:
[https://whois.domaintools.com](https://whois.domaintools.com)

**Screenshots:**  
1. **Eingabemaske**:  
   ![Screenshot Placeholder](URL_TO_SCREENSHOTS)  
   **Beschreibung:** Zeigt die Suchoberfläche von DomainTools, wo die Domain eingegeben wurde. Optionen wie „Monitor Domain Properties“ und „Reverse IP Address Lookup“ bieten Möglichkeiten für Reverse Engineering.

2. **Detailansicht**:  
   ![Screenshot Placeholder](URL_TO_SCREENSHOTS)  
   **Beschreibung:** Zusätzliche Informationen wie Admin-E-Mails und technische Ansprechpartner sind sichtbar.

---

## Task 2: DNS Recon

### Vorbereitung
Falls das Tool nicht installiert war, wurde es mit den folgenden Befehlen installiert:
```bash
sudo apt update
sudo apt install dnsrecon
```

### Durchführung
DNS Recon wurde mit dem folgenden Befehl ausgeführt:
```bash
dnsrecon -d certifiedhacker.com
```

**Ergebnisse:**  
- **DNSSEC**: Nicht konfiguriert für die Domain. Dies bedeutet, dass keine zusätzlichen Sicherheitsmaßnahmen für DNS-Einträge eingerichtet sind.  
- **Nameserver (NS)**: `ns1.bluehost.com` und `ns2.bluehost.com`.  
- **MX-Records**: Mailserver `mail.certifiedhacker.com`.  
- **SRV-Records**: 12 SRV-Einträge wurden gefunden, darunter Dienste wie `_autodiscover._tcp` und `_caldav._tcp`.

![Screenshot Placeholder](URL_TO_SCREENSHOTS)  
**Beschreibung:**  
Der Screenshot zeigt die Ausgabe des Befehls. Die identifizierten SRV-Records geben Hinweise auf verwendete Anwendungen oder Konfigurationen, die für weitere Tests genutzt werden könnten.

---

## Key Learnings

1. **Unterschiedliche Tools ergänzen sich**  
   Whois bietet grundlegende Registrierungsinformationen, während DNS Recon tiefere technische Details liefert.

2. **Potenzielle Schwachstellen identifizieren**  
   Die Analyse von SRV-Records und DNSSEC-Konfigurationen kann Angriffsvektoren aufzeigen.

3. **Datenquellen verstehen**  
   Webtools wie DomainTools bieten erweiterten Zugang zu Informationen.

---

## Fazit
Dieses Lab hat die Wichtigkeit der Nutzung unterschiedlicher Tools wie Whois und DNS Recon gezeigt. Während Whois grundlegende Informationen liefert, erweitert DNS Recon die Analyse durch technische DNS-Daten. Die Kombination dieser Tools ermöglicht eine tiefgehende Sicherheitsbewertung.
