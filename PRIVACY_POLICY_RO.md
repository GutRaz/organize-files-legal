> **Versiune în limba română.** În caz de conflict, [EULA în engleză](./EULA_EN.md) și [Politica de confidențialitate în engleză](./PRIVACY_POLICY_EN.md) prevalează. Consultați un avocat calificat în jurisdicția dvs.

---

# Politica de confidențialitate — Organize Files

**Editor:** Guțulov Răzvan Constantin PFA  
**Sediu profesional:** Str. Republicii nr. 33B, bl. N3, sc. A, et. 1, ap. 3, Breaza de Sus, 105400 Breaza, jud. Prahova, România  
**Registrul comerțului:** F2026004513003 (EUID ROONRC.F2026004513003)  
**Cod unic de înregistrare:** 53610310  
**Contact:** razvan.gutulov@outlook.com  
**Data efectivă:** 2026-05-28  
**URL public:** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_RO.md`

---

## Rezumat

Organize Files prelucrează fișiere **local pe dispozitiv**. Conținutul fișierelor **nu se încarcă** la editor pentru organizare sau reparare obișnuită. Aplicația **scrie fișiere locale** (snapshot sesiune, resume, jurnale opționale), conform secțiunilor de mai jos.

## Operator și contact

Pentru datele personale prelucrate de editor, operatorul este **Guțulov Răzvan Constantin PFA**. Contact: **razvan.gutulov@outlook.com**.

## Date prelucrate local

| Date | Unde | Scop |
|------|------|------|
| Fișiere și foldere alese | Doar pe dispozitiv | Organizare, deduplicare, reparare, ștergere opțională |
| Snapshot UI (`last-ui-session.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (desktop) sau stocare privată aplicație (Android) | Reluare spațiu de lucru: căi, extensii, opțiuni |
| Resume organize + jurnal mutări | `_OrganizeMediaLogs` sau folder sesiune | Sări peste mutări finalizate; metadate recuperare (căi codificate) |
| Heartbeat JSON opțional | `_OrganizeMediaLogs` | Contoare progres pentru instrumente externe |
| Trial / licență | Profil aplicație | Entitlement |
| Stare verificare actualizări | Profil aplicație | Limitare verificări manifest |
| Staging SAF (Android) | Folder sesiune | Copiere arbori `content://` pentru acces motor |
| Parolă SMTP notificări e-mail (opțional) | Criptată pe disc în preferințele sesiunii (AES-GCM cu fișier cheie per profil). La upgrade, o migrare unică rescrie orice parolă SMTP legacy nestocată cu AES-GCM către AES-GCM când acel câmp este prezent |  Doar dacă activezi notificările e-mail și introduci credențiale SMTP. Fișierul cheie AES-GCM rămâne în folderul de profil al aplicației și poate fi citit de contul de utilizator conectat al sistemului de operare. Protejează citirile ocazionale ale preferințelor JSON, nu un seif susținut de hardware. |
| ID instalare licență (opțional) | `license_installation_id.txt` în profil | Trimis doar când `ORGANIZE_FILES_LICENSE_SERVER_URL` este configurat de operator |
| Telemetrie OpenTelemetry (opțional) | Configurată de operator | Metadate job automatizare (ID job, tip țintă, context trace W3C) — fără căi sau conținut fișiere |

## Ce nu primește editorul implicit

- Conținutul fișierelor din rulări organize/repair  
- Contacte, locație, microfon, cameră (nefolosite)  
- SDK-uri de analiză în sursa deschisă  
- Parolele SMTP pe care le stochezi local (rămân pe dispozitiv, în afară de trimiterea mailului prin serverul SMTP al tău)  

## Utilizare opțională a rețelei

| Activitate | Date trimise | Destinatar |
|----------|--------------|------------|
| Verificare actualizări opțională | GET HTTPS; User-Agent `OrganizeFiles-UpdateCheck/1.0` + URL manifest. Dezactivare: `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Gazda JSON-ului (ex. GitHub) |
| Achiziție Store / licență | API-uri de facturare platformă | Microsoft, Google sau Apple (per canal) |
| Server licențe opțional (configurat de operator) | ID instalare persistent (GUID în `license_installation_id.txt`) trimis la un server de licențe operat de editor sau configurat de operator la `ORGANIZE_FILES_LICENSE_SERVER_URL`. ID-ul de instalare este un identificator de dispozitiv conform Considerentului 30 GDPR. Bază legală: executarea contractului. Retenție la editor: înregistrări de entitlement pe durata activă plus până la 24 de luni după expirare/revocare (prevenire abuz și litigii); documente contabile pot fi păstrate până la 7 ani unde legea o cere. Serverele operate de un operator urmează calendarul documentat al operatorului. Inactiv dacă `ORGANIZE_FILES_LICENSE_SERVER_URL` nu este setat. | Server operat de editor/operator |
| OpenTelemetry opțional (configurat de operator) | Metadate job la `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT` (ID job, tip țintă, context trace W3C) — fără căi sau conținut fișiere. Inactiv implicit; necesită configurare explicită. | Colector OTLP configurat de operator |
| Notificări e-mail opționale (când sunt activate) | Starea rulării și fragmente din jurnal (pot include căi de fișiere) trimise prin serverul SMTP configurat de operator | SMTP / furnizor de e-mail al operatorului |
| Webhook-uri opționale de automatizare (configurate de operator) | Când `ORGANIZE_FILES_AUTOMATION_WEBHOOK_URL` este setat, evenimente din ciclul de viață al joburilor, cu ID-uri de corelare și căile fișierelor de stare ale automatizării | Endpoint webhook configurat de operator |

Verificările de actualizare compară **doar metadate de versiune** — nu căi sau conținut de fișiere. Desktop-ul poate rula verificarea o dată pe zi după acceptarea EULA, dacă nu este dezactivată.

## Google Play

Achizițiile folosesc **Google Play Billing pe dispozitiv**. Clientul open-source validează achizițiile local. Listările **de producție** Play ar trebui să adauge **Play Integrity** și/sau **verificare server-side** conform politicii Google; acel procesare pe server este configurată de editor, nu activată implicit în acest depozit.

## Procesori terți (când folosiți aceste funcții)

- **Microsoft Store / Google Play / Mac App Store** — facturare și entitlement  
- **GitHub (sau gazda manifestului)** — JSON versiune opțional prin HTTPS  
- **Client e-mail** — dacă contactați suportul prin link mailto  

## Baze legale (cadru GDPR, nu sfat juridic)

| Prelucrare | Bază tipică |
|------------|-------------|
| Organizare/reparare locală pe foldere alese | Executarea contractului / interes legitim al operatorului |
| Snapshot sesiune, resume, heartbeat | Necesar pentru funcționarea instrumentului |
| Facturare Store | Contract cu magazinul |
| Verificare manifest actualizări (opțional) | Interes legitim (actualizări de securitate); poate fi dezactivată |
| E-mail suport | Interes legitim / pași precontractuali la cererea utilizatorului |

## Transferuri internaționale

Verificările opționale de actualizare pot ajunge la servere în afara SEE (ex. GitHub în SUA). Facturarea magazinului este guvernată de termenii fiecărei platforme.

## Autoritate de supraveghere

Dacă legea aplicabilă acordă drepturi sau plângeri la o autoritate de supraveghere, contactați mai întâi editorul la **razvan.gutulov@outlook.com**. Rezidenții UE/SEE pot depune plângere la autoritatea locală (România: ANSPDCP, https://www.dataprotection.ro).

## Responsabilități operator (cadru GDPR)

Date personale pot exista **în interiorul fișierelor**. Utilizatorul sau organizația poate fi **operator** și trebuie să aleagă baza legală, să minimizeze retenția și să răspundă la cererile persoanelor vizate.

## Retenție

Fișierele locale rămân până le ștergeți, goliți datele aplicației, dezinstalați aplicația sau suprascrieți folderele de ieșire. Editorul nu operează un program central de retenție pentru date doar locale.

Pentru datele deținute de editor:

- E-mail de suport și corespondență: până la 24 de luni după ultimul contact relevant, exceptând litigiul sau o obligație legală care cere retenție mai lungă.
- Achiziții directe, rambursări, fiscalitate și contabilitate: până la 7 ani unde legea fiscală sau contabilă o cere.
- Înregistrări de entitlement pe un server de licențe operat de editor: pe durata activă plus până la 24 de luni după expirare sau revocare.
- Jurnale de acces/securitate pe un server operat de editor: până la 90 de zile, exceptând nevoie mai lungă pentru investigații de securitate, prevenire fraudă sau pretenții legale.

## Drepturile dumneavoastră

Pentru datele pe care editorul le deține (ex. corespondență suport e-mail), contactați **razvan.gutulov@outlook.com**. Unde este cazul, puteți solicita acces, rectificare, ștergere, restricționare, opoziție, portabilitate sau retragerea consimțământului. Editorul urmărește să răspundă cererilor persoanelor vizate în maxim **30 de zile** de la o cerere verificată (poate fi solicitată verificarea identității când este rezonabil necesar). Pentru date stocate doar pe dispozitiv, le puteți șterge prin **Șterge date salvate**, dezinstalare sau ștergere manuală. **Șterge date salvate** elimină sesiuni, jurnale și ciorne de automatizare, dar poate păstra starea locală de entitlement și un identificator de instalare folosit pentru verificări opționale de licență — vedeți textul de confirmare din aplicație înainte de a continua.

## Copii

Instrument de productivitate general, neadresat copiilor sub 13 ani (sau vârsta cerută în jurisdicția dumneavoastră).

## Modificări

Modificările materiale ar trebui reflectate în listările store și documentația in-app înainte de lansare.

## Documente conexe

- [EULA (română)](./EULA_RO.md)  
- [EULA (engleză)](./EULA_EN.md)  
- [Politica de confidențialitate (engleză)](./PRIVACY_POLICY_EN.md)  
- [Politica de confidențialitate (germană)](./PRIVACY_POLICY_DE.md)  
- [Politica de confidențialitate (franceză)](./PRIVACY_POLICY_FR.md)
