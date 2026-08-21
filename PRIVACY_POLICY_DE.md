> **Unoffizielle maschinelle Übersetzung — keine Rechtsberatung.** Die [englische EULA](./EULA_EN.md) und die [englische Datenschutzerklärung](./PRIVACY_POLICY_EN.md) gelten, wenn diese Übersetzung mit ihnen in Konflikt steht. Wenden Sie sich an einen qualifizierten Rechtsanwalt in Ihrer Rechtsordnung.

---

# Datenschutzerklärung — Organize Files

**Herausgeber:** Guțulov Răzvan Constantin PFA  
**Eingetragene Anschrift:** Str. Republicii nr. 33B, bl. N3, sc. A, et. 1, ap. 3, Breaza de Sus, 105400 Breaza, jud. Prahova, România  
**Handelsregister:** F2026004513003 (EUID ROONRC.F2026004513003)  
**Steuernummer:** 53610310  
**Kontakt:** razvan.gutulov@outlook.com  
**Gültig ab:** 2026-05-28  
**Öffentliche URL:** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_DE.md`

---

## Zusammenfassung

Organize Files verarbeitet Dateien **lokal auf Ihrem Gerät**. Dateiinhalte werden bei normalen Organize- oder Repair-Läufen **nicht** an den Herausgeber hochgeladen. Die App **schreibt lokale Dateien** (Sitzungs-Snapshots, Resume-Status, optionale Logs) wie unten beschrieben.

## Verantwortlicher und Kontakt

Für personenbezogene Daten, die der Herausgeber verarbeitet, ist der Verantwortliche **Guțulov Răzvan Constantin PFA**. Kontakt: **razvan.gutulov@outlook.com**.

## Lokal verarbeitete Daten

| Daten | Speicherort | Zweck |
|------|-------------|--------|
| Von Ihnen gewählte Dateien und Ordner | Nur Ihr Gerät | Organisieren, Deduplizieren, Reparieren, optionales Löschen |
| UI-Sitzungs-Snapshot (`last-ui-session.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (Desktop) oder App-Speicher (Android) | Arbeitsbereich wiederherstellen |
| Organize-Resume + optionales Move-Journal | Output `_OrganizeMediaLogs` oder Sitzungsordner | Abgeschlossene Moves überspringen |
| Optionales Run-Heartbeat-JSON | Output `_OrganizeMediaLogs` | Fortschrittszähler für externe Tools |
| Test-/Lizenzstatus | Profilordner unter Local App Data | Trial oder Store-Entitlement |
| Update-Check-Status | Profilordner | Drosselung optionaler Versionsmanifest-Checks |
| Android SAF-Staging | Sitzungsordner | `content://`-Bäume für die Engine kopieren |
| Optionales SMTP-Passwort für E-Mail-Benachrichtigungen | Verschlüsselt im Ruhezustand in den Sitzungseinstellungen auf dem Gerät (AES-GCM mit profilspezifischer Schlüsseldatei). Bei einem Upgrade schreibt eine einmalige Migration jedes ältere SMTP-Passwort ohne AES-GCM auf AES-GCM um, wenn dieses Feld vorhanden ist |  Nur wenn E-Mail-Benachrichtigungen aktiviert und SMTP-Zugangsdaten eingegeben werden. Die AES-GCM-Schlüsseldatei verbleibt im App-Profilordner und ist für das angemeldete Betriebssystem-Benutzerkonto lesbar. Es schützt gelegentliche Lesevorgänge von JSON-Einstellungen und nicht durch einen hardwaregestützten Tresor. |

## Was der Herausgeber standardmäßig nicht erhält

- Dateiinhalte aus Organize-/Repair-Läufen  
- Kontakte, Standort, Mikrofon oder Kamera (nicht genutzt)  
- Analytics-SDKs im Open-Source-Baum  
- SMTP-Passwörter, die Sie lokal speichern (bleiben auf dem Gerät, außer beim Senden über Ihren SMTP-Server)  

## Optionale Netzwerknutzung

| Aktivität | Gesendete Daten | Empfänger |
|-----------|-----------------|-----------|
| Optionaler Update-Check | HTTPS GET zu einem Versionsmanifest. Der Host (z. B. GitHub) empfängt IP, User-Agent `OrganizeFiles-UpdateCheck/1.0` und TLS-Metadaten. Keine Dateipfade oder Inhalte. Deaktivierung: `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Host des JSON-Manifests |
| Store-Kauf / Lizenz | Plattform-Abrechnungs-APIs | Microsoft, Google oder Apple |
| Optionaler Lizenzserver (betreiberkonfiguriert) | Eine zufällige persistente Installations-ID (GUID in `license_installation_id.txt`) wird an einen vom Herausgeber oder Betreiber betriebenen Lizenzserver unter `ORGANIZE_FILES_LICENSE_SERVER_URL` gesendet. Die Installations-ID ist eine Gerätekennung im Sinne von Erwägungsgrund 30 DSGVO. Rechtsgrundlage: Vertragserfüllung. Aufbewahrung beim Herausgeber: Entitlement-Datensätze während der aktiven Laufzeit zuzüglich bis zu 24 Monaten nach Ablauf/Widerruf (Missbrauchsprävention und Streitfälle); Buchhaltungsunterlagen ggf. bis zu 7 Jahre, soweit gesetzlich erforderlich. Betreibergeführte Server folgen dem dokumentierten Aufbewahrungsplan des Betreibers. Inaktiv, solange `ORGANIZE_FILES_LICENSE_SERVER_URL` nicht gesetzt ist. | Lizenzserver des Herausgebers oder Betreibers |
| Optionales OpenTelemetry-Tracing (betreiberkonfiguriert) | Wenn `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT` gesetzt ist, werden Automatisierungs-Job-Metadaten (Job-IDs, Korrelations-IDs, Zieltyp-Tags, W3C-Trace-Kontext) an den konfigurierten OTLP-Collector exportiert. Keine Dateipfade oder Dateiinhalte. Standardmäßig inaktiv; erfordert explizite Betreiberkonfiguration. | Betreiberkonfigurierter OTLP-Collector |
| Optionale E-Mail-Benachrichtigungen (wenn aktiviert) | Laufstatus und Protokollauszüge (können Dateipfade enthalten) über den betreiberkonfigurierten SMTP-Server | Betreiber-SMTP / Mail-Anbieter |

Update-Checks vergleichen **nur Versionsmetadaten** — keine Dateipfade oder Inhalte.

## Google Play

In-App-Käufe nutzen **Google Play Billing auf dem Gerät**. Der Open-Source-Client validiert Käufe lokal. **Produktions**-Play-Einträge sollten **Play Integrity** und/oder **serverseitige Kaufvalidierung** ergänzen; diese Verarbeitung konfiguriert der Herausgeber, sie ist im Repo standardmäßig nicht aktiv.

## Rechtsgrundlagen (DSGVO-Rahmen, keine Rechtsberatung)

| Verarbeitung | Typische Grundlage |
|--------------|--------------------|
| Lokales Organize/Repair auf bereits gewählten Ordnern | Vertragserfüllung / berechtigtes Interesse des Betreibers |
| Lokale Sitzungs-, Resume- und Heartbeat-Dateien | Dieselbe — erforderlich zur Bereitstellung des Tools |
| Store-Abrechnung und Entitlement | Vertrag mit der Store-Plattform |
| Optionaler Update-Manifest-Check | Berechtigtes Interesse an Sicherheitsupdates; per Umgebungsvariable abschaltbar |
| Support-E-Mail | Berechtigtes Interesse / vorvertragliche Schritte auf Ihre Anfrage |
| Optionaler Lizenzserver / OpenTelemetry | Vertragserfüllung bzw. berechtigtes Interesse des Betreibers; nur bei expliziter Konfiguration |

## Drittanbieter (bei Nutzung)

- **Microsoft Store / Google Play / Mac App Store** — Abrechnung und Entitlement  
- **GitHub (oder Ihr Manifest-Host)** — optionales Versions-JSON per HTTPS  
- **E-Mail-Client** — bei Kontakt per mailto-Link  

## Ihre Verantwortung (DSGVO-Rahmen)

Personenbezogene Daten können **in Ihren Dateien** enthalten sein. Wenn Sie solche Daten verarbeiten, können Sie (oder Ihre Organisation) **Verantwortlicher** sein und müssen Rechtsgrundlage, Minimierung und Betroffenenrechte beachten.

## Aufbewahrung

Lokale Dateien bleiben, bis Sie sie löschen, App-Daten leeren, deinstallieren oder Output-Ordner überschreiben. Der Herausgeber betreibt keinen zentralen Aufbewahrungsplan für rein lokale Daten.

Für Daten, die der Herausgeber hält:

- Support-E-Mail und Korrespondenz: bis zu 24 Monate nach dem letzten relevanten Kontakt, sofern ein Streitfall oder eine gesetzliche Pflicht keine längere Aufbewahrung erfordert.
- Direktkauf-, Erstattungs-, Steuer- und Buchhaltungsunterlagen: bis zu 7 Jahre, soweit steuer- oder buchhaltungsrechtlich erforderlich.
- Entitlement-Datensätze eines vom Herausgeber betriebenen Lizenzservers: während der aktiven Laufzeit zuzüglich bis zu 24 Monaten nach Ablauf oder Widerruf.
- Zugriffs-/Sicherheitsprotokolle eines vom Herausgeber betriebenen Servers: bis zu 90 Tage, sofern nicht länger für Sicherheitsuntersuchungen, Betrugsprävention oder Rechtsansprüche erforderlich.

## Ihre Rechte

Für Daten, die der Herausgeber hält (z. B. Support-E-Mail), kontaktieren Sie **razvan.gutulov@outlook.com**. Soweit anwendbar, können Sie Auskunft, Berichtigung, Löschung, Einschränkung, Widerspruch, Datenübertragbarkeit oder Widerruf einer Einwilligung verlangen. Der Herausgeber strebt an, verifizierte Betroffenenanfragen innerhalb von **30 Tagen** zu beantworten (eine Identitätsprüfung kann verlangt werden, wenn dies vernünftigerweise erforderlich ist). Für nur lokal gespeicherte Daten: **App-Daten löschen**, Deinstallation oder manuelles Löschen. **App-Daten löschen** entfernt Sitzungen, Logs und Automatisierungsentwürfe, kann aber lokalen Lizenzstatus und eine Installationskennung für optionale Lizenzchecks behalten — siehe den In-App-Bestätigungstext vor dem Fortfahren.

## Kinder

Allgemeines Produktivitäts-Tool, nicht an Kinder unter 13 (oder das lokale Mindestalter) gerichtet.

## Änderungen

Wesentliche Änderungen sollten vor Release in Store-Einträgen und In-App-Dokumentation erscheinen.

## Verwandte Dokumente

- [EULA (Englisch)](./EULA_EN.md)  
- [EULA (Deutsch)](./EULA_DE.md)  
- [Datenschutz (Englisch)](./PRIVACY_POLICY_EN.md)  
- [Datenschutz (Rumänisch)](./PRIVACY_POLICY_RO.md)  
- [Datenschutz (Französisch)](./PRIVACY_POLICY_FR.md)
