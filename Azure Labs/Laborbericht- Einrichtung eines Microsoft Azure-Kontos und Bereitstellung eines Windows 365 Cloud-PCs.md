# Laborbericht: Einrichtung eines Microsoft Azure-Kontos und Bereitstellung eines Windows 365 Cloud-PCs

## Inhaltsverzeichnis
1. [Erstellung eines Microsoft Azure-Kontos und Subscription](#1-erstellung-eines-microsoft-azure-kontos-und-subscription)
2. [Vergleich zwischen Azure Virtual Desktop, Windows 365 und Microsoft Business Premium](#2-vergleich-zwischen-azure-virtual-desktop-windows-365-und-microsoft-business-premium)
3. [Kauf und Zuweisung der Microsoft 365 E5 Lizenz](#3-kauf-und-zuweisung-der-microsoft-365-e5-lizenz)
4. [Gruppen- und Policy-Erstellung in Intune](#4-gruppen-und-policy-erstellung-in-intune)
5. [Provisionierung eines Windows 365 Cloud-PCs](#5-provisionierung-eines-windows-365-cloud-pcs)
6. [Analyse von Bereitstellungsproblemen und Fehlerbehebung](#6-analyse-von-bereitstellungsproblemen-und-fehlerbehebung)
7. [Zusammenfassung und Fazit](#7-zusammenfassung-und-fazit)

---

## 1. Erstellung eines Microsoft Azure-Kontos und Subscription

In diesem Abschnitt wird die grundlegende Einrichtung eines Microsoft Azure-Kontos beschrieben. Ein aktives Konto mit einer gültigen Subscription ist eine unverzichtbare Voraussetzung für alle weiteren Schritte, wie die Bereitstellung von Cloud-Diensten und die Lizenzierung.

### Schritte zur Erstellung eines Azure-Kontos und Aktivierung einer Subscription:
1. **Registrierung des Azure-Kontos:**
   - Zugriff auf die Registrierungsseite von Microsoft Azure unter [azure.microsoft.com](https://azure.microsoft.com/de-de/free/).
   - Eingabe der persönlichen Daten wie Name, E-Mail-Adresse und Telefonnummer.
   - Auswahl einer globalen Administrationsrolle für das erstellte Konto.

2. **Hinterlegen einer Zahlungsmethode:**
   - Eine gültige Kreditkarte wurde hinterlegt, um die Identität zu verifizieren und zukünftige Abrechnungen zu ermöglichen.
   - Hinweis: Ohne eine hinterlegte Zahlungsmethode können keine kostenpflichtigen Dienste wie Intune oder Windows 365 genutzt werden.

3. **Aktivierung der Subscription:**
   - Zunächst wurde eine kostenlose Testversion aktiviert. Nach Ablauf der Testphase wurde die Subscription auf das Modell „Pay-as-you-go“ umgestellt.
   - Die aktive Subscription stellt sicher, dass alle notwendigen Azure-Dienste, wie Intune und Windows 365, genutzt werden können.

Diese Subscription ist die oberste Instanz worauf alle weiteren Produkte laufen sollen wie .B. Lizenzen, Services und weiteres.In meinem Fall **"Azure Subscription 1"**

![img](https://i.imgur.com/sqZQcsV.png)

---

## 2. Vergleich zwischen Azure Virtual Desktop, Windows 365 und Microsoft Business Premium

Dieser Abschnitt beschreibt die Entscheidungsfindung bei der Wahl zwischen Azure Virtual Desktop (AVD), Windows 365 und Microsoft Business Premium. Ziel ist es, die Unterschiede und Vorteile jeder Lösung herauszuarbeiten und darzulegen, warum Windows 365 und die Microsoft 365 E5 Lizenz den Anforderungen besser entsprachen.

### Vergleich der Plattformen und Lizenzen:
#### Azure Virtual Desktop (AVD)
- **Flexibilität:** AVD bietet eine hochgradig anpassbare Umgebung, die jedoch eine tiefere technische Expertise erfordert.
- **Kostenmodell:** Abrechnung erfolgt basierend auf der tatsächlichen Nutzung (z. B. Rechenleistung, Speicher), was zu variablen Kosten führen kann.
- **Netzwerkkonfiguration:** Erfordert die Einrichtung von Azure Virtual Networks (VNets), um die Desktops bereitzustellen.
- **Zielgruppe:** Geeignet für Unternehmen mit erfahrenen IT-Teams und komplexen Anforderungen.

#### Windows 365
- **Einfache Bereitstellung:** Ohne VNet-Konfiguration, ideal für schnelle Bereitstellung.
- **Kostenmodell:** Festes monatliches Abrechnungsmodell pro Benutzer, ideal für planbare Budgets.
- **Zero-Trust-Sicherheit:** Zentrale Verwaltung über Microsoft Intune und Multi-Faktor-Authentifizierung.
- **Zielgruppe:** Unternehmen, die eine unkomplizierte und sichere Cloud-Desktop-Lösung suchen.

Hier auch ein Vergleich Animation zwischen Microsoft 365 und Azure Virtual Desktop Solution:
![img](https://i.imgur.com/ZZg2ove.png)
![img](https://i.imgur.com/HJoXr8y.png)

#### Microsoft Business Premium
- **Kostengünstiger:** Geeignet für kleine Unternehmen mit weniger komplexen Anforderungen.
- **Begrenzte Funktionen:** Enthält keine erweiterten Sicherheitsfeatures wie Entra ID P2 und Defender für Endpoint.
- **Zielgruppe:** Kleine bis mittelständische Unternehmen ohne Bedarf an hochentwickelten Sicherheitslösungen.

### Entscheidung gegen Microsoft Business Premium
Die Wahl fiel bewusst nicht auf Microsoft Business Premium, da folgende Anforderungen nicht erfüllt wurden:
- **Fehlende Zero-Trust-Unterstützung:** Entra ID P2 ist notwendig für Sicherheitsrichtlinien.
- **Begrenzte Sicherheitsfunktionen:** Microsoft Defender für Endpoint ist nicht enthalten.

### Tabelle: Vergleich der Optionen
| **Feature**                      | **Azure Virtual Desktop (AVD)** | **Windows 365 (Microsoft 365 E5)** | **Microsoft Business Premium** |
|-----------------------------------|--------------------------------|------------------------------------|---------------------------------|
| **Einfache Bereitstellung**       | ❌ Hoher Aufwand               | ✅ Intuitiv                        | ✅ Intuitiv                     |
| **Kostenmodell**                 | Variabel                       | Fest                              | Fest                           |
| **Zero-Trust-Unterstützung**     | ✅ Optional                    | ✅ Vollständig                     | ❌ Nicht enthalten              |
| **Entra ID P2**                  | ❌ Optional                    | ✅ Enthalten                       | ❌ Nicht enthalten              |
| **Intune-Integration**           | ✅ Optional                    | ✅ Vollständig                     | ✅ Eingeschränkt                |

---

## 3. Kauf und Zuweisung der Microsoft 365 E5 Lizenz und Windows 365 Cloud-PC-Lizenz

In diesem Abschnitt wird der Kauf und die Zuweisung der Microsoft 365 E5 Lizenz sowie der Windows 365 Cloud-PC-Lizenz beschrieben. Beide Lizenzen sind notwendig, da die Microsoft 365 E5 Lizenz die Sicherheits- und Verwaltungsfunktionen bietet und die Cloud-PC-Lizenz die eigentliche Nutzung eines Windows 365 PCs ermöglicht.

### Schritte zum Kauf und zur Zuweisung:
1. **Microsoft 365 E5 Lizenz:**
   - Zugriff auf das Microsoft 365 Admin Center unter [admin.microsoft.com](https://admin.microsoft.com/).
   - Auswahl der E5 Lizenz aufgrund ihrer erweiterten Sicherheitsfunktionen, wie Entra ID P2 und Microsoft Defender.

2. **Windows 365 Cloud-PC-Lizenz:**
   - Erwerb der Lizenz „Windows 365 Enterprise 2 vCPU, 8 GB, 128 GB“.
   - Diese Lizenz ist **erforderlich**, damit Benutzer der Zielgruppe einen Cloud-PC provisioniert bekommen können.
![img](https://i.imgur.com/tmWBHDH.png)

3. **Zuweisung:**
   - Beide Lizenzen wurden dem globalen Administrator-Account **popal.e@popaleoutlook.onmicrosoft.com** zugewiesen.
     
![img](https://i.imgur.com/BLRBkMB.png)

P.S.:
 Ich habe noch dazu eine Microsoft Intune Suite Lizenz dazugekauft für weitere Lab Szenarios. Der granulare Unterschied zwischen Microsoft 365 E5 und eine Intune Suite sind folgende:
	•	**Remote Help**: Sicherer Remote-Support für Benutzergeräte, ideal für BYOD-Szenarien.
	•	**Endpoint Privilege Management (EPM)**: Temporäre Admin-Rechte für Benutzer, ohne Sicherheitsrisiken.
	•	**Automatisiertes Drittanbieter-App-Management**: Patch-Updates für Apps wie Adobe oder Chrome.
	•	**Erweiterte Compliance**: Automatische Behebung von Richtlinienverstößen auf Geräten.
	•	**Advanced Endpoint Analytics**: Proaktive Fehlererkennung und -vermeidung (z. B. Abstürze).
	•	**Microsoft Tunnel**: Sichere App-Verbindungen und Zugriff, speziell für mobile Mitarbeiter.
	•	**Mehr Sicherheit und Effizienz**: Verbesserte Verwaltung und Schutz von BYOD- und Unternehmensgeräten.

Für kleinere Unternehmen in nicht Risikobehafteten Infrastrukturen reicht jedoch eine Microsoft 365 E5 Lizenz vollkommen aus.
---

## 4. Gruppen-Einstellung in Intune

Nach dem Kauf und der Zuweisung der Lizenzen wurde eine Sicherheitsgruppe erstellt, um die Provisionierung der Cloud-PCs zu vereinfachen.
Hierbei gibts es in Azure 2 Optionen bei der Art der Gruppe: Security & Microsoft 365. Der Granulare Unterschied sind natürlich die Sicerheitsmechanismen, die man bei der Security Group hat.
Hier eine kurze Tabelle über die Unterschied:
### Tabelle: Vergleich von Security Groups und Microsoft 365 Groups

| **Feature**                     | **Security Group**                             | **Microsoft 365 Group**                    |
|----------------------------------|-----------------------------------------------|--------------------------------------------|
| **Primärer Zweck**               | Zugriffskontrolle und Sicherheitsverwaltung   | Kollaboration und Kommunikation            |
| **Verwendung für Berechtigungen**| ✅ Zugriff auf Ressourcen und Rollenverwaltung | ❌ Nicht für Berechtigungen geeignet       |
| **Geräteunterstützung**          | ✅ Kann Benutzer und Geräte enthalten          | ❌ Unterstützt nur Benutzer                |
| **Dynamische Mitgliedschaft**    | ✅ Unterstützt automatische Regeln             | ❌ Keine dynamischen Regeln                |
| **Intune-Integration**           | ✅ Vollständig integriert                      | ❌ Nicht für Richtlinien geeignet          |
| **Integration mit Conditional Access** | ✅ Kann für MFA- und Sicherheitsrichtlinien genutzt werden | ❌ Nicht unterstützt            |
| **Rollenbasierte Zugriffskontrolle (RBAC)** | ✅ Direkte Zuweisung von Rollen möglich        | ❌ Nicht für RBAC geeignet                 |
| **Kollaborationsfunktionen**     | ❌ Keine Kollaborationsressourcen enthalten    | ✅ Enthält Mailbox, Planner und Teams      |
| **Mailfunktionalität**           | ❌ Nicht enthalten                             | ✅ Integrierte Mailbox und Kalender        |
| **Typische Anwendungsfälle**     | Sicherheitsgruppen, Zugriffskontrolle, Gerätemanagement | Teams-Kanäle, E-Mail, Projektmanagement   |
### Schritte zur Erstellung:
1. **Erstellen einer Sicherheitsgruppe:**
   - Navigieren zu **Gruppen → Neue Gruppe erstellen** unter [intune.microsoft.com](https://intune.microsoft.com/).
   - Gruppentyp: **Sicherheitsgruppe**.
   - Name: „Windows365-EntraID“.

2. **Zuweisung der Sicherheitsgruppe:**
   - Der globalen Administrator **popal.e@popaleoutlook.onmicrosoft.com** wurde als Mitglied hinzugefügt.

![img](https://i.imgur.com/o24lCAX.png)
---

## 5. Provisionierung eines Windows 365 Cloud-PCs

Die Provisionierung eines Windows 365 Cloud-PCs ist ein zentraler Schritt, um einen virtuellen Arbeitsplatz bereitzustellen. In diesem Abschnitt wird beschrieben, wie eine Provisioning-Policy erstellt wurde und warum bestimmte Entscheidungen, wie die Auswahl eines Standard-Images, getroffen wurden.

### Schritte zur Provisionierung eines Windows 365 Cloud-PCs:
1. **Zugriff auf das Intune Admin Center:**
   - Aufruf von [intune.microsoft.com](https://intune.microsoft.com/) und Anmeldung mit dem globalen Administrator-Account.

2. **Erstellen der Provisioning-Policy:**
3. **License type:** Enterprise – da die Lizenzierung auf Enterprise basiert und umfangreiche Funktionen wie Sicherheitsrichtlinien und Management unterstützt.
2. **Join type:** Entra ID Join, da keine Hybrid-Umgebung verwendet wurde und der Benutzer direkt in Entra ID erstellt wurde.
3. **Region:** Automatisch – empfohlen für eine schnellere Bereitstellung.
4. **Namensschema:** **EPL-%USERNAME:5%-%RAND:5%**, wobei:
   - **EPL** für die Initialen steht.
   - **%USERNAME:5%** die ersten 5 Zeichen des Benutzernamens übernimmt.
   - **%RAND:5%** einen zufälligen 5-stelligen Wert zur eindeutigen Identifikation generiert.

5. **Zuweisung:**  
   - Die Sicherheitsgruppe „Windows365-EntraID“ wurde der Provisioning-Policy zugewiesen.

3. **Auswahl des Images:**
   - **Image type:** Aus der Microsoft-Galerie wurde das Image „Windows 11 Enterprise + Microsoft 365 Apps“ gewählt.
   - **Gründe für die Auswahl:**
     - Vorinstallierte Microsoft 365 Apps.
     - Aktualität und Sicherheit der Version.
     - Reduzierter Aufwand im Vergleich zu Custom Images.

4. **Option für Custom Images:**
   - Alternativ könnten benutzerdefinierte Images hochgeladen werden, um spezifische Anforderungen zu erfüllen. Weitere Details: [Microsoft Custom Images](https://learn.microsoft.com/de-de/mem/autopilot/custom-images).

5. **Gerätekonfiguration:**
   - Sprache und Region: **German**.

6. **Zuweisung der Gruppe:**
   - Die zuvor erstellt Sicherheitsgruppe „Windows365-EntraID“ wurde der Provisioning-Policy zugewiesen.

![img](https://i.imgur.com/i0bN1S8.png)
---

## 6. Analyse von Bereitstellungsproblemen und Fehlerbehebung

Während der Bereitstellung des Windows 365 Cloud-PCs traten Probleme auf, die eine Anpassung der Einstellungen erforderten. Dieser Abschnitt beschreibt die auftretenden Fehler und deren Lösung.

### Beschreibung der Fehler:
1. **Problem:**  
   Die Einstellung „Mobile Device Management Authority“ war standardmäßig auf „None“ gesetzt.  
   **Auswirkungen:**  
   Die Bereitstellung des Cloud-PCs schlug mehrfach fehl, obwohl alle anderen Konfigurationen korrekt waren.

2. **Analyse:**  
   Überprüfung des Dashboards ergab, dass die Standardkonfiguration von Intune geändert werden musste. Ein Bericht aus September 2024 bestätigte das Problem.

### Lösung:
- Aktivierung der Mobile Device Management Authority gemäß [Microsoft-Dokumentation](https://learn.microsoft.com/en-us/mem/intune/fundamentals/mdm-authority-set).
- Anpassung der Konfiguration im Intune Admin Center.

![img](https://i.imgur.com/iSUwsGU.png)

![img](https://i.imgur.com/pSCWDqs.png)

![img](https://i.imgur.com/AnkIlNj.png)

Verifizierung, dass der Cloud PC auch bereitgestellt ist und nutzbar ist: Hierbei kann man ganz einfach auf die URL https://windows365.microsoft.com/ gehen und man sieht, dass man den bereitgestellten Cloud PC direkt benutzen kann.

![img](https://i.imgur.com/KMTzxbe.png)

---

## 7. Zusammenfassung und Fazit

Dieser Bericht dokumentiert die Einrichtung eines Microsoft Azure-Kontos, die Auswahl der geeigneten Lizenzen und die Bereitstellung eines Windows 365 Cloud-PCs. Der Fokus lag auf der Wahl einer sicheren, kosteneffizienten und einfach zu verwaltenden Lösung.

### Fazit:
- **Windows 365** erwies sich als die optimale Lösung für die Bereitstellung sicherer Cloud-PCs.
- **Microsoft 365 E5** bot die erforderlichen Sicherheits- und Verwaltungsfunktionen.
- Die Herausforderungen bei der Bereitstellung wurden erfolgreich gelöst, wodurch ein zuverlässiges und skalierbares Setup geschaffen wurde.

---

### Passende Links:
- [Azure Virtual Desktop vs. Windows 365](https://learn.microsoft.com/de-de/azure/virtual-desktop/)
- [Microsoft 365 E5 Lizenzübersicht](https://www.microsoft.com/de-de/microsoft-365/compare-microsoft-365-enterprise-plans)
- [Windows 365 Dokumentation](https://learn.microsoft.com/de-de/windows-365/enterprise/)
- [Intune Custom Images](https://learn.microsoft.com/de-de/mem/autopilot/custom-images)
