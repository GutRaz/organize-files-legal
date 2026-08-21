# Privacy Policy — Organize Files

**Publisher:** Guțulov Răzvan Constantin PFA  
**Registered address:** Str. Republicii nr. 33B, bl. N3, sc. A, et. 1, ap. 3, Breaza de Sus, 105400 Breaza, jud. Prahova, România  
**Trade register:** F2026004513003 (EUID ROONRC.F2026004513003)  
**Tax identification number:** 53610310  
**Contact:** razvan.gutulov@outlook.com  
**Effective date:** 2026-05-28  
**Public URL:** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_EN.md`

---

## Summary

Organize Files processes files **locally on the device**. File contents are **not uploaded to the publisher's own servers** for normal organize or repair operations. The app **does write local files** on the device (session snapshots, resume state, optional logs) as described below.

## Controller and contact

For personal data processed by the publisher, the controller is **Guțulov Răzvan Constantin PFA**. Contact: **razvan.gutulov@outlook.com**.

## Data processed locally

| Data | Where stored | Purpose |
|------|----------------|---------|
| Files and folders you select | Your device only | Organize, deduplicate, repair, optional delete |
| UI session snapshot (`last-ui-session.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (desktop) or app-private storage (Android) | Restore workspace: paths, extensions, options |
| Organize resume + optional move journal | Output `_OrganizeMediaLogs` or session folder | Skip completed moves; recovery metadata (paths encoded) |
| Optional run heartbeat JSON | Output `_OrganizeMediaLogs` | Progress counters for external tools |
| Trial / license state | Profile folder under Local App Data | Enforce trial or store entitlement |
| Update-check state | Profile folder | Throttle optional version manifest checks |
| Android SAF staging | Session folder under app storage | Copy `content://` trees so the engine can read them |
| Optional email-notification SMTP password | Encrypted at rest in session preferences on the device (AES-GCM with a per-profile key file). On upgrade, a one-time migration rewrites any legacy SMTP password stored without AES-GCM to AES-GCM when that field is present. The AES-GCM key file stays in the app profile folder and is readable to the signed-in OS user account. It protects casual reads of preferences JSON, not a hardware-backed vault. | Only if you enable email notifications and enter SMTP credentials |

## What the publisher does not receive by default

- File contents from organize/repair runs  
- Contacts, location, microphone, or camera (not used)  
- Analytics SDKs bundled in the open-source tree  
- SMTP passwords you store locally (they stay on your device unless you send mail through your SMTP server)  

## Optional network use

| Activity | Data sent | Recipient |
|----------|-----------|-----------|
| Optional update check | HTTPS GET to a version manifest. The host (for example GitHub) receives the request IP address, User-Agent `OrganizeFiles-UpdateCheck/1.0`, and TLS metadata. No file paths or file contents are sent. Disable with `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Host serving the JSON manifest |
| Store purchase / license | Platform billing APIs | Microsoft, Google, or Apple (per channel) |
| Optional license server (operator-configured) | A random persistent installation ID (GUID stored in `license_installation_id.txt`) is sent to a publisher-operated or operator-configured license server at `ORGANIZE_FILES_LICENSE_SERVER_URL`. The installation ID is a device identifier under GDPR Recital 30. Lawful basis: performance of contract. Publisher-operated retention: entitlement records while active plus up to 24 months after expiry/revocation for abuse prevention and dispute handling; accounting records may be retained up to 7 years where required by law. Operator-run servers follow the operator's documented retention schedule. This feature is inactive unless `ORGANIZE_FILES_LICENSE_SERVER_URL` is set. | Publisher or operator license server |
| Optional OpenTelemetry tracing (operator-configured) | When `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT` is set, automation job metadata (job IDs, correlation IDs, target type tags, W3C trace context) is exported to the configured OTLP collector. No file paths or file contents are included. This feature is inactive by default and requires explicit operator configuration. | Operator-configured OTLP collector |
| Optional email notifications (when enabled) | Run status and log excerpts (may include file paths) sent through the operator-configured SMTP server | Operator SMTP / mail provider |

Update checks compare **version metadata only**. The desktop app may run this check once per day after EULA acceptance unless disabled.

## Legal bases (GDPR-style framing, not legal advice)

| Processing | Typical basis |
|------------|----------------|
| Local organize/repair on folders already selected | Performance of contract / legitimate interest of the operator |
| Local session, resume, and heartbeat files | Same — necessary to provide the tool |
| Store billing and entitlement | Contract with the platform store |
| Optional update manifest check | Legitimate interest in security updates; can be disabled via environment variable |
| Support email | Legitimate interest / pre-contractual steps at your request |

## International transfers

Optional update checks may reach servers outside the European Economic Area (for example GitHub in the United States). Store billing is handled under each platform's terms.

## Supervisory authority and complaints

If applicable law grants data-subject rights or a complaint to a supervisory authority, contact the publisher first at **razvan.gutulov@outlook.com**. EU/EEA residents may also lodge a complaint with their local data protection authority (for Romania: ANSPDCP, https://www.dataprotection.ro).

## Third-party processors (when these features are used)

- **Microsoft Store / Google Play / Mac App Store** — billing and entitlement. Google Play uses on-device Billing; production listings should add Play Integrity and/or server-side verification per Google policy.
- **GitHub (or the manifest host)** — optional version JSON over HTTPS (may include client IP in server logs)
- **Email client** — when contacting support via mailto link

## Operator responsibilities (GDPR-style framing)

Personal data may exist **inside** your files. If you process such data, you (or your organization) may be a **data controller** and must choose a lawful basis, minimize retention, and respond to data-subject requests.

## Retention

Local files remain until you delete them, clear app data, uninstall the app, or overwrite output folders. The publisher does not operate a central retention schedule for local-only data.

For data held by the publisher:

- Support email and correspondence: up to 24 months after the last meaningful contact, unless a dispute or legal obligation requires longer retention.
- Direct purchase, refund, tax, and accounting records: up to 7 years where required by tax or accounting law.
- Publisher-operated license server entitlement records: while the entitlement is active plus up to 24 months after expiry or revocation.
- Publisher-operated server access/security logs: up to 90 days, unless needed longer for security investigation, fraud prevention, or legal claims.

## Your rights

For data the publisher holds (e.g. support email correspondence), contact **razvan.gutulov@outlook.com**. Where applicable, you may request access, correction, deletion, restriction, objection, portability, or withdrawal of consent. The publisher aims to respond to data-subject requests within **30 days** of a verified request (identity may be requested when reasonably necessary). For data stored only on your device, you can delete most app data via **Clear app data**, uninstall, or manual file deletion. **Clear app data** removes sessions, logs, and automation drafts, but may retain local license entitlement state and an installation identifier used for optional license checks — see the in-app confirmation text before you proceed.

## Children

General productivity tool not directed at children under 13 (or the age required in your jurisdiction).

## Changes

Material changes should appear in store listings and in-app documentation before release.

## Related documents

- [EULA (English)](./EULA_EN.md)  
- [Privacy policy (Romanian)](./PRIVACY_POLICY_RO.md)  
- [Privacy policy (German)](./PRIVACY_POLICY_DE.md)  
- [Privacy policy (French)](./PRIVACY_POLICY_FR.md)
