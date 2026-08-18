> **Inofficiell maskinöversättning — inte juridisk rådgivning.** [Engelska EULA](./EULA_EN.md) och [English Privacy Policy](./PRIVACY_POLICY_EN.md) styr om denna översättning är i konflikt med dem. Rådfråga kvalificerad advokat i din jurisdiktion.

---

# Sekretesspolicy — Organisera filer

**Förlag:** Razvan Constantin Gutulov  
**Kontakta:** razvan.gutulov@outlook.com  
**Ikraftträdandedatum:** 2026-05-28  
**Offentlig webbadress:** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_SV.md`

---

## Sammanfattning

Organize Files behandlar filer **lokalt på enheten**. Filinnehåll laddas **inte upp till utgivarens egna servrar** för normal organisering eller reparation. Appen **skriver lokala filer** på enheten (sessionsögonblicksbilder, återuppta status, valfria loggar) enligt beskrivningen nedan.

## Data bearbetas lokalt

| Data | Var lagrad | Syfte |
|------|----------------|--------|
| Filer och mappar du väljer | Endast din enhet | Organisera, deduplicera, reparera, valfri radering |
| Ögonblicksbild av UI-session (`last-ui-session.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (dator) eller app-privat lagring (Android) | Återställ arbetsyta: sökvägar, tillägg, alternativ |
| Organisera CV + valfri flyttjournal | Utdata `_OrganizeMediaLogs` eller sessionsmapp | Hoppa över genomförda drag; återställningsmetadata (sökvägar kodade) |
| Valfritt kör hjärtslag JSON | Utdata `_OrganizeMediaLogs` | Framstegsräknare för externa verktyg |
| Prov/licensstatus | Profilmapp under Lokal appdata | Genomför rättegång till prov eller butik |
| Uppdateringskontrollstatus | Profilmapp | Throttle valfri version manifestkontroller |
| Android SAF iscensättning | Sessionsmapp under applagring | Kopiera `content://`-träd så att motorn kan läsa dem |
| Valfritt SMTP-lösenord för e-postaviseringar | Lagras krypterat i sessionsinställningar på enheten (AES-GCM med en nyckelfil per profil). Vid uppgradering skrivs ett äldre SMTP-lösenord utan AES-GCM om en gång till AES-GCM när fältet finns. AES-GCM-nyckelfilen ligger kvar i appens profilmapp och kan läsas av det inloggade OS-användarkontot; den skyddar mot tillfällig läsning av inställnings-JSON, inte ett hårdvaruvalv. | Endast om e-postaviseringar aktiveras och SMTP-uppgifter anges |

## Vad utgivaren inte tar emot som standard

- Filinnehåll från organiserings-/reparationskörningar  
- Kontakter, plats, mikrofon eller kamera (används ej)  
- Analytics-SDK:er samlade i trädet med öppen källkod  

## Valfri nätverksanvändning

| Aktivitet | Data skickade | Mottagare |
|--------|--------|--------|
| Valfri uppdateringskontroll | HTTPS GET till ett versionsmanifest. Värden (till exempel GitHub) tar emot förfrågans IP-adress, User-Agent `OrganizeFiles-UpdateCheck/1.0` och TLS-metadata. Inga filsökvägar eller filinnehåll skickas. Inaktivera med `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Värd som betjänar JSON-manifestet |
| Butiksköp/licens | Plattformsfakturerings-API:er | Microsoft, Google eller Apple (per kanal) |
| Valfri licensserver (operatörskonfigurerad) | Ett slumpmässigt beständigt installations-ID (GUID lagrat i `license_installation_id.txt`) skickas till en utgivarstyrd eller operatörskonfigurerad licensserver på `ORGANIZE_FILES_LICENSE_SERVER_URL`. Installations-ID:t är en enhetsidentifierare enligt GDPR skäl 30. Laglig grund: fullgörande av kontrakt. Utgivardriven lagring: rättighetsregister medan aktiva plus upp till 24 månader efter utgång/återkallelse för missbruksförebyggande och tvister; bokföringsuppgifter kan lagras upp till 7 år där lag kräver det. Operatörsdrivna servrar följer operatörens dokumenterade lagringsschema. Den här funktionen är inaktiv om inte `ORGANIZE_FILES_LICENSE_SERVER_URL` är inställd. | Utgivar- eller operatörslicensserver |
| Valfri OpenTelemetry-spårning (operatörskonfigurerad) | När `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT` är inställt, exporteras automatiseringsjobbmetadata (jobb-ID, korrelations-ID, måltypstaggar, W3C-spårningskontext) till den konfigurerade OTLP-samlaren. Inga filsökvägar eller filinnehåll ingår. Den här funktionen är inaktiv som standard och kräver explicit operatörskonfiguration. | Operatörskonfigurerad OTLP-samlare |
| Valfria e-postaviseringar (när aktiverade) | Körstatus och loggutdrag (kan inkludera filsökvägar) som skickas via den operatörskonfigurerade SMTP-servern | Operatörens SMTP / e-postleverantör |
| Försök med hjälp av motor NAS igen | Inga utöver konfigurerade nätverksvägar | NAS / SMB-värd |

Uppdateringskontroller jämför **endast versionsmetadata**. Desktopappen kan köra den här kontrollen en gång om dagen efter godkännande av EULA om den inte är inaktiverad.

## Rättslig grund (inramning i GDPR-stil, inte juridisk rådgivning)

| Bearbetar | Typisk grund |
|------------|----------------|
| Lokal organisering/reparation på redan valda mappar | Fullgörande av kontrakt/operatörens berättigade intresse |
| Lokala sessions-, CV- och hjärtslagsfiler | Samma — nödvändigt för att tillhandahålla verktyget |
| Butiksfakturering och berättigande | Kontrakt med plattformsbutiken |
| Valfri uppdateringsmanifestkontroll | Berättigat intresse för säkerhetsuppdateringar; kan inaktiveras via miljövariabel |
| Support e-post | Berättigat intresse / steg före avtalet på din begäran |

## Internationella överföringar

Valfria uppdateringskontroller kan nå servrar utanför Europeiska ekonomiska samarbetsområdet (till exempel GitHub i USA). Butiksfakturering hanteras under varje plattforms villkor.

## Tillsynsmyndighet och klagomål

Om tillämplig lag ger registrerade rättigheter eller ett klagomål till en tillsynsmyndighet, kontakta först utgivaren på **razvan.gutulov@outlook.com**. Invånare i EU/EES kan också lämna in ett klagomål till sin lokala dataskyddsmyndighet (för Rumänien: ANSPDCP, https://www.dataprotection.ro).

## Tredjepartsprocessorer (när dessa funktioner används)

- **Microsoft Store / Google Play / Mac App Store** — fakturering och berättigande. Google Play använder fakturering på enheten; produktionslistor bör lägga till spelintegritet och/eller verifiering på serversidan enligt Googles policy.
- **GitHub (eller manifestvärden)** — valfri version JSON över HTTPS (kan inkludera klient-IP i serverloggar)
- **E-postklient** — när du kontaktar support via mailto-länk

## Operatörsansvar (GDPR-stil inramning)

Personuppgifter kan finnas **inuti** dina filer. Om du behandlar sådana uppgifter kan du (eller din organisation) vara en **uppgiftsansvarig** och måste välja en laglig grund, minimera lagring och svara på förfrågningar från registrerade.

## Retention

Lokala filer finns kvar tills du tar bort dem, rensar appdata, avinstallerar appen eller skriver över utdatamappar. Utgivaren har inget centralt lagringsschema för endast lokal data.

För data som utgivaren innehar:

- Support-e-post och korrespondens: upp till 24 månader efter den senaste meningsfulla kontakten, om inte en tvist eller rättslig skyldighet kräver längre lagring.
- Direkta köp, återbetalningar, skatte- och bokföringsregister: upp till 7 år där skatte- eller bokföringslag kräver det.
- Rättighetsregister på en licensserver som drivs av utgivaren: medan rättigheten är aktiv plus upp till 24 månader efter utgång eller återkallelse.
- Åtkomst- och säkerhetsloggar på en server som drivs av utgivaren: upp till 90 dagar, om inte längre tid behövs för säkerhetsutredning, bedrägeriförebyggande eller rättsliga anspråk.


## Dina rättigheter

Kontakta **razvan.gutulov@outlook.com** för data som utgivaren har (t.ex. support via e-postkorrespondens). För data som endast lagras på din enhet kan du radera de flesta appdata via **Rensa appdata**, avinstallera eller manuell radering av filer. **Rensa appdata** tar bort sessioner, loggar och automatiseringsutkast, men kan behålla licensankare, betalda installationsmarkörer och en anonym installationsidentifierare som används för valfria licenskontroller – se bekräftelsetexten i appen innan du fortsätter.

## Barn

Allmänt produktivitetsverktyg som inte är riktat till barn under 13 år (eller den ålder som krävs i din jurisdiktion).

## Ändringar

Materialändringar bör visas i butiksuppgifterna och i dokumentationen i appen innan de släpps.

## Relaterade dokument

- [EULA (engelska)](./EULA_EN.md)  
- [Sekretesspolicy (rumänska)](./PRIVACY_POLICY_RO.md)  
- [Sekretesspolicy (tyska)](./PRIVACY_POLICY_DE.md)  
- [Sekretesspolicy (franska)](./PRIVACY_POLICY_FR.md)

---

Om denna översättning är ofullständig gäller den engelska integritetspolicyn.

## Personuppgiftsansvarig och kontakt

För personuppgifter som behandlas av utgivaren är personuppgiftsansvarig **Razvan Constantin Gutulov**. Kontakt: **razvan.gutulov@outlook.com**.

## Lagring (utgivarens register)

För data som innehas av utgivaren:

- Support-e-post och korrespondens: upp till 24 månader efter den senaste meningsfulla kontakten, om inte en tvist eller rättslig skyldighet kräver längre lagring.
- Direkta köp, återbetalningar, skatte- och bokföringsregister: upp till 7 år där skatte- eller bokföringslag kräver det.
- Rättighetsregister på en licensserver som drivs av utgivaren: medan rättigheten är aktiv plus upp till 24 månader efter utgång eller återkallelse.
- Åtkomst- och säkerhetsloggar på en server som drivs av utgivaren: upp till 90 dagar, om inte längre tid behövs för säkerhetsutredning, bedrägeriförebyggande eller rättsliga anspråk.

## Dina rättigheter (svarstid)

Utgivaren strävar efter att svara på registrerades begäranden inom **30 dagar** efter en verifierad begäran (identitetsverifiering kan begäras när det är rimligen nödvändigt).
