> **Übersetzung zur Erleichterung bereitgestellt.** Die [englische EULA](../en/eula.md) und die [englische Datenschutzerklärung](../en/privacy-policy.md) sind die Referenzfassungen. Soweit zwingendes Verbraucherrecht in Ihrem Land der Fassung in Ihrer eigenen Sprache Vorrang einräumt, gilt diese Fassung. Keine Rechtsberatung — wenden Sie sich an einen qualifizierten Anwalt in Ihrer Jurisdiktion.

---

# Datenschutzerklärung — Organize Files

**Herausgeber:** Guțulov Răzvan Constantin PFA  
**Eingetragene Anschrift:** Str. Republicii nr. 33B, bl. N3, sc. A, et. 1, ap. 3, Breaza de Sus, 105400 Breaza, jud. Prahova, România  
**Handelsregister:** F2026004513003 (EUID ROONRC.F2026004513003)  
**Steuernummer:** 53610310  
**Kontakt:** razvan.gutulov@outlook.com  
**Gültig ab:** 2026-05-28  
**Öffentliche URL:** `https://github.com/GutRaz/organize-files-legal/blob/main/de/privacy-policy.md`

---

## Zusammenfassung

Organize Files verarbeitet Dateien **lokal auf Ihrem Gerät**. Dateiinhalte werden bei normalen Organize- oder Repair-Läufen **nicht** an den Herausgeber hochgeladen. Die App **schreibt lokale Dateien** (Sitzungs-Snapshots, Resume-Status, optionale Logs) wie unten beschrieben.

## Verantwortlicher und Kontakt

Für personenbezogene Daten, die der Herausgeber verarbeitet, ist der Verantwortliche **Guțulov Răzvan Constantin PFA**. Kontakt: **razvan.gutulov@outlook.com**.

## Lokal verarbeitete Daten

| Daten | Speicherort | Zweck |
|------|-------------|--------|
| Von Ihnen ausgewählte Dateien und Ordner | Nur auf Ihrem Gerät | Organisieren, Duplikate finden, reparieren und, wenn gewählt, löschen |
| UI-Sitzungs-Snapshot (`last-ui-session.json`) | Der Ordner `sessions\<id>\` im Profilordner der App: `%LocalAppData%\OrganizeFilesCrossPlatform` unter Windows, `~/Library/Application Support/OrganizeFilesCrossPlatform` unter macOS, `~/.local/share/OrganizeFilesCrossPlatform` unter Linux oder der private App-Speicher unter Android und iOS | Arbeitsbereich wiederherstellen |
| Fortsetzungsstand eines Organize-Laufs + optionales Verschiebeprotokoll | `_OrganizeMediaLogs` im Ausgabeordner oder der Sitzungsordner | Bereits erledigte Verschiebungen überspringen, Wiederherstellungsdaten mit kodierten Pfaden |
| Optionale Fortschrittsdatei eines Laufs, JSON | `_OrganizeMediaLogs` im Ausgabeordner | Fortschrittszähler für andere Programme |
| Test- und Lizenzstatus | Profilordner der App | Testphase oder Store-Kauf anwenden |
| Status der Update-Prüfung | Profilordner der App | Begrenzen, wie oft die optionale Versionsprüfung läuft |
| Android: Kopien von Ordnern, die über die Systemauswahl SAF gewählt wurden | Sitzungsordner im App-Speicher | Kopiert `content://`-Ordnerbäume, damit die Engine sie lesen kann |
| Optionales SMTP-Passwort für E-Mail-Benachrichtigungen | Verschlüsselt im Ruhezustand in den Sitzungseinstellungen auf dem Gerät (AES-GCM mit profilspezifischer Schlüsseldatei). Bei einem Upgrade schreibt eine einmalige Migration jedes ältere SMTP-Passwort ohne AES-GCM auf AES-GCM um, wenn dieses Feld vorhanden ist |  Nur wenn E-Mail-Benachrichtigungen aktiviert und SMTP-Zugangsdaten eingegeben werden. Die AES-GCM-Schlüsseldatei verbleibt im App-Profilordner und ist für das angemeldete Betriebssystem-Benutzerkonto lesbar. Es schützt gelegentliche Lesevorgänge von JSON-Einstellungen und nicht durch einen hardwaregestützten Tresor. |

## Was der Herausgeber standardmäßig nicht erhält

- Dateiinhalte aus Organize-/Repair-Läufen  
- Kontakte, Standort, Mikrofon oder Kamera (nicht genutzt)  
- Analyse- oder Werbedaten (kein solches SDK ist in der App enthalten)  
- SMTP-Passwörter, die Sie lokal speichern (bleiben auf dem Gerät, außer beim Senden über Ihren SMTP-Server)  

## Optionale Netzwerknutzung

| Aktivität | Gesendete Daten | Empfänger |
|-----------|-----------------|-----------|
| Optionaler Update-Check | HTTPS GET zu einem Versionsmanifest. Der Host (z. B. GitHub) empfängt IP, User-Agent `OrganizeFiles-UpdateCheck/1.0` und TLS-Metadaten. Keine Dateipfade oder Inhalte. Deaktivierung: `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Host des JSON-Manifests |
| Store-Kauf / Lizenz | Plattform-Abrechnungs-APIs | Microsoft, Google oder Apple |
| Optionaler Lizenzserver (betreiberkonfiguriert) | Eine zufällige persistente Installations-ID (GUID in `license_installation_id.txt`) wird an einen vom Herausgeber oder Betreiber betriebenen Lizenzserver unter `ORGANIZE_FILES_LICENSE_SERVER_URL` gesendet. Die Installations-ID ist eine Gerätekennung im Sinne von Erwägungsgrund 30 DSGVO. Rechtsgrundlage: Vertragserfüllung. Aufbewahrung beim Herausgeber: Entitlement-Datensätze während der aktiven Laufzeit zuzüglich bis zu 24 Monaten nach Ablauf/Widerruf (Missbrauchsprävention und Streitfälle); Buchhaltungsunterlagen ggf. bis zu 7 Jahre, soweit gesetzlich erforderlich. Betreibergeführte Server folgen dem dokumentierten Aufbewahrungsplan des Betreibers. Inaktiv, solange `ORGANIZE_FILES_LICENSE_SERVER_URL` nicht gesetzt ist. | Lizenzserver des Herausgebers oder Betreibers |
| Optionales OpenTelemetry-Tracing (betreiberkonfiguriert) | Wenn `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT` gesetzt ist, werden Automatisierungs-Job-Metadaten (Job-IDs, Korrelations-IDs, Zieltyp-Tags, W3C-Trace-Kontext) an den konfigurierten OTLP-Collector exportiert. Keine Dateipfade oder Dateiinhalte. Standardmäßig inaktiv; erfordert explizite Betreiberkonfiguration. | Betreiberkonfigurierter OTLP-Collector |
| Optionale E-Mail-Benachrichtigungen (wenn aktiviert) | Laufstatus und Protokollauszüge (können Dateipfade enthalten) über den betreiberkonfigurierten SMTP-Server | Betreiber-SMTP / Mail-Anbieter |
| Optionale Automatisierungs-Webhooks (vom Betreiber konfiguriert) | Wenn `ORGANIZE_FILES_AUTOMATION_WEBHOOK_URL` gesetzt ist, Ereignisse aus dem Auftragslebenszyklus mit Korrelations-IDs und den Dateipfaden der Automatisierungsstatusdateien | Vom Betreiber konfigurierter Webhook-Endpunkt |
| Optionale Identitätsprüfung bei der Ausführungsgenehmigung (vom Betreiber eingerichtet) | Ist `ORGANIZE_FILES_APPROVE_OAUTH_JWKS_URL` gesetzt, holt ein HTTPS-GET die Signaturschlüssel und hält sie eine Stunde im Cache; kein Token verlässt das Gerät. Ist `ORGANIZE_FILES_APPROVE_OAUTH_INTROSPECTION_URL` gesetzt, wird das Bearer-Token des Betreibers selbst zur Validierung an diesen Endpunkt gesendet (RFC 7662), mit HTTP-Basic-Client-Anmeldedaten, sofern eingerichtet. Inaktiv, solange keine dieser URLs gesetzt ist. | Vom Betreiber eingerichteter Identitätsanbieter |

Update-Checks vergleichen **nur Versionsmetadaten** — keine Dateipfade oder Inhalte.

## Rechtsgrundlagen (DSGVO-Rahmen, keine Rechtsberatung)

| Verarbeitung | Typische Grundlage |
|--------------|--------------------|
| Lokales Organize/Repair auf bereits gewählten Ordnern | Vertragserfüllung / berechtigtes Interesse des Betreibers |
| Lokale Sitzungs-, Fortsetzungs- und Fortschrittsdateien | Dieselbe, erforderlich zur Bereitstellung des Tools |
| Store-Abrechnung und Entitlement | Vertrag mit der Store-Plattform |
| Optionaler Update-Manifest-Check | Berechtigtes Interesse an Sicherheitsupdates; per Umgebungsvariable abschaltbar |
| Support-E-Mail | Berechtigtes Interesse / vorvertragliche Schritte auf Ihre Anfrage |
| Optionaler Lizenzserver / OpenTelemetry | Vertragserfüllung bzw. berechtigtes Interesse des Betreibers; nur bei expliziter Konfiguration |

## Internationale Übermittlungen

Optionale Update-Prüfungen können Server außerhalb des Europäischen Wirtschaftsraums erreichen (zum Beispiel GitHub in den Vereinigten Staaten). Die Store-Abrechnung erfolgt nach den Bedingungen der jeweiligen Plattform.

## Aufsichtsbehörde und Beschwerden

Wenn das anwendbare Recht Betroffenenrechte oder eine Beschwerde bei einer Aufsichtsbehörde vorsieht, wenden Sie sich zuerst an den Herausgeber unter **razvan.gutulov@outlook.com**. Personen mit Wohnsitz in der EU oder im EWR können außerdem Beschwerde bei ihrer örtlichen Datenschutzbehörde einlegen (für Rumänien: ANSPDCP, https://www.dataprotection.ro).

## Drittanbieter (bei Nutzung)

- **Microsoft Store / Google Play / Mac App Store** — Abrechnung und Entitlement. Google Play prüft Käufe auf dem Gerät.  
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

- [EULA (Englisch)](../en/eula.md)  
- [EULA (Deutsch)](./eula.md)  
- [Datenschutz (Englisch)](../en/privacy-policy.md)  
- [Datenschutz (Rumänisch)](../ro/privacy-policy.md)  
- [Datenschutz (Französisch)](../fr/privacy-policy.md)
