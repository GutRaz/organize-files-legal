> **Onofficiële automatische vertaling – geen juridisch advies.** De [Engelse EULA](./EULA_EN.md) en het [Engelse privacybeleid](./PRIVACY_POLICY_EN.md) zijn van toepassing als deze vertaling daarmee in strijd is. Raadpleeg een gekwalificeerde raadsman in uw rechtsgebied.

---

# Privacybeleid — Bestanden ordenen

**Uitgever:** Razvan Constantin Gutulov  
**Contact:** razvan.gutulov@outlook.com  
**Ingangsdatum:** 28-05-2026  
**Openbare URL:** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_NL.md`

---

## Samenvatting

Bestanden organiseren verwerkt bestanden **lokaal op het apparaat**. Bestandsinhoud wordt **niet geüpload naar de eigen servers van de uitgever** voor normale organisatie- of reparatiewerkzaamheden. De app **schrijft lokale bestanden** op het apparaat (sessiemomentopnamen, hervattingsstatus, optionele logboeken) zoals hieronder beschreven.

## Verwerkingsverantwoordelijke en contact

Voor persoonsgegevens die de uitgever verwerkt, is de verwerkingsverantwoordelijke **Razvan Constantin Gutulov**. Contact: **razvan.gutulov@outlook.com**.

## Gegevens lokaal verwerkt

| Gegevens | Waar opgeslagen | Doel |
|-----|---------------|---------|
| Bestanden en mappen die u selecteert | Alleen jouw apparaat | Organiseren, ontdubbelen, repareren, optioneel verwijderen |
| Momentopname van UI-sessie (`last-ui-session.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (desktop) of app-privéopslag (Android) | Werkruimte herstellen: paden, extensies, opties |
| Organiseer cv + optioneel verhuislogboek | Uitvoer `_OrganizeMediaLogs` of sessiemap | Sla voltooide zetten over; herstelmetagegevens (gecodeerde paden) |
| Optioneel hartslag-JSON uitvoeren | Uitvoer `_OrganizeMediaLogs` | Voortgangstellers voor externe tools |
| Proef-/licentiestatus | Profielmap onder Lokale app-gegevens | Proef- of winkelrecht afdwingen |
| Update-controlestatus | Profielmap | Optionele versiemanifestcontroles beperken |
| Android SAF-enscenering | Sessiemap onder app-opslag | Kopieer `content://`-bomen zodat de engine ze kan lezen |
| Optioneel SMTP-wachtwoord voor e-mailmeldingen | Versleuteld opgeslagen in sessievoorkeuren op het apparaat (AES-GCM met een sleutelbestand per profiel). Bij een upgrade wordt een oud SMTP-wachtwoord dat zonder AES-GCM is opgeslagen eenmalig herschreven naar AES-GCM wanneer dat veld aanwezig is. Het AES-GCM-sleutelbestand blijft in de profielmap van de app en is leesbaar voor het aangemelde OS-gebruikersaccount; het beschermt toevallig lezen van voorkeuren-JSON, geen hardwarekluis. | Alleen als je e-mailmeldingen inschakelt en SMTP-gegevens invoert |

## Wat de uitgever standaard niet ontvangt

- Bestandsinhoud van organisatie-/reparatieruns  
- Contacten, locatie, microfoon of camera (niet gebruikt)  
- Analytics-SDK's gebundeld in de open-sourcestructuur  

## Optioneel netwerkgebruik

| Activiteit | Gegevens verzonden | Ontvanger |
|----------|-----------|-----------|
| Optionele updatecontrole | HTTPS GET naar een versiemanifest. De host (bijvoorbeeld GitHub) ontvangt het IP-adres van de aanvraag, User-Agent `OrganizeFiles-UpdateCheck/1.0` en TLS-metagegevens. Er worden geen bestandspaden of bestandsinhoud verzonden. Schakel uit met `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Host die het JSON-manifest levert |
| Winkelaankoop / licentie | Platform-facturerings-API's | Microsoft, Google of Apple (per kanaal) |
| Optionele licentieserver (door de operator geconfigureerd) | Een willekeurige persistente installatie-ID (GUID opgeslagen in `license_installation_id.txt`) wordt verzonden naar een door de uitgever beheerde of door de operator geconfigureerde licentieserver op `ORGANIZE_FILES_LICENSE_SERVER_URL`. De installatie-ID is een apparaatidentificatie volgens AVG-overweging 30. Wettelijke basis: uitvoering van contract. Uitgever-beheerde retentie: entitlement-records terwijl actief plus tot 24 maanden na verval/intrekking voor misbruikpreventie en geschillen; boekhoudkundige gegevens kunnen tot 7 jaar worden bewaard wanneer de wet dat vereist. Door de operator beheerde servers volgen het gedocumenteerde retentieschema van de operator. Deze functie is inactief tenzij `ORGANIZE_FILES_LICENSE_SERVER_URL` is ingesteld. | Uitgever- of operatorlicentieserver |
| Optionele OpenTelemetry-tracering (door de operator geconfigureerd) | Wanneer 'ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT' is ingesteld, worden metagegevens van automatiseringstaak (taak-ID's, correlatie-ID's, doeltype-tags, W3C-traceercontext) geëxporteerd naar de geconfigureerde OTLP-verzamelaar. Er zijn geen bestandspaden of bestandsinhoud opgenomen. Deze functie is standaard inactief en vereist een expliciete operatorconfiguratie. | Door de operator geconfigureerde OTLP-collector |
| Optionele e-mailmeldingen (indien ingeschakeld) | Uitvoeringsstatus en logfragmenten (kunnen bestandspaden bevatten) verzonden via de door de operator geconfigureerde SMTP-server | Operator-SMTP / e-mailprovider |
| Helpers voor nieuwe pogingen van Engine NAS | Geen buiten de geconfigureerde netwerkpaden | NAS/SMB-host |

Bij updatecontroles wordt **alleen metagegevens van de versie** vergeleken. De desktop-app kan deze controle eenmaal per dag uitvoeren na acceptatie van de EULA, tenzij uitgeschakeld.

## Rechtsgrondslagen (framing in AVG-stijl, geen juridisch advies)

| Verwerking | Typische basis |
|-----------|---------------|
| Lokaal organiseren/repareren van reeds geselecteerde mappen | Uitvoering van het contract / legitiem belang van de exploitant |
| Lokale sessie-, cv- en hartslagbestanden | Hetzelfde — noodzakelijk om de tool te bieden |
| Facturering en rechten opslaan | Contract met de platformwinkel |
| Optionele update-manifestcontrole | Gerechtvaardigd belang bij beveiligingsupdates; kan worden uitgeschakeld via omgevingsvariabele |
| Ondersteunings-e-mail | Gerechtvaardigd belang / precontractuele stappen op uw verzoek |

## Internationale overschrijvingen

Optionele updatecontroles kunnen servers buiten de Europese Economische Ruimte bereiken (bijvoorbeeld GitHub in de Verenigde Staten). Winkelfacturering wordt afgehandeld volgens de voorwaarden van elk platform.

## Toezichthoudende autoriteit en klachten

Als de toepasselijke wetgeving de betrokkene rechten verleent of een klacht indient bij een toezichthoudende autoriteit, neem dan eerst contact op met de uitgever via **razvan.gutulov@outlook.com**. Inwoners van de EU/EER kunnen ook een klacht indienen bij hun lokale gegevensbeschermingsautoriteit (voor Roemenië: ANSPDCP, https://www.dataprotection.ro).

## Externe processors (wanneer deze functies worden gebruikt)

- **Microsoft Store / Google Play / Mac App Store** — facturering en rechten. Google Play maakt gebruik van facturering op het apparaat; productievermeldingen moeten Play-integriteit en/of serververificatie toevoegen volgens het beleid van Google.
- **GitHub (of de manifesthost)** — optionele versie JSON via HTTPS (kan client-IP bevatten in serverlogboeken)
- **E-mailclient** — wanneer u contact opneemt met de ondersteuning via de mailto-link

## Verantwoordelijkheden van de operator (framing in AVG-stijl)

Er kunnen persoonlijke gegevens **in** uw bestanden aanwezig zijn. Als u dergelijke gegevens verwerkt, bent u (of uw organisatie) mogelijk een **gegevensbeheerder** en moet u een wettelijke basis kiezen, de bewaring minimaliseren en reageren op verzoeken van betrokkenen.

## Retentie

Lokale bestanden blijven bewaard totdat u ze verwijdert, app-gegevens wist, de app verwijdert of uitvoermappen overschrijft. De uitgever hanteert geen centraal bewaarschema voor uitsluitend lokale gegevens.

Voor gegevens die de uitgever bewaart:

- Ondersteuningsmail en correspondentie: tot 24 maanden na het laatste relevante contact, tenzij een geschil of wettelijke verplichting langere bewaring vereist.
- Directe aankopen, terugbetalingen, belastingen en boekhouding: tot 7 jaar wanneer fiscaal of boekhoudkundig recht dat vereist.
- Entitlement-records van een door de uitgever beheerde licentieserver: terwijl actief plus tot 24 maanden na verval of intrekking.
- Toegangs-/beveiligingslogs van een door de uitgever beheerde server: tot 90 dagen, tenzij langer nodig voor beveiligingsonderzoek, fraudepreventie of claims.

## Jouw rechten

Neem voor gegevens waarover de uitgever beschikt (bijvoorbeeld ondersteuningsmailcorrespondentie) contact op met **razvan.gutulov@outlook.com**. Waar van toepassing kunt u toegang, rectificatie, wissing, beperking, bezwaar, overdraagbaarheid of intrekking van toestemming verzoeken. De uitgever streeft ernaar geverifieerde verzoeken binnen **30 dagen** te beantwoorden (identiteitsverificatie kan redelijkerwijs worden gevraagd). Voor gegevens die alleen op uw apparaat zijn opgeslagen, kunt u de meeste app-gegevens verwijderen via **App-gegevens wissen**, verwijderen of handmatig bestanden verwijderen. **Door app-gegevens te wissen** worden sessies, logboeken en automatiseringsconcepten verwijderd, maar kunnen licentieproefankers, markeringen voor betaalde installaties en een anonieme installatie-ID die wordt gebruikt voor optionele licentiecontroles behouden blijven. Bekijk de bevestigingstekst in de app voordat u doorgaat.

## Kinderen

Algemeen productiviteitshulpmiddel dat niet gericht is op kinderen onder de 13 jaar (of de leeftijd die vereist is in uw rechtsgebied).

## Veranderingen

Materiële wijzigingen moeten vóór de release in winkelvermeldingen en in-app-documentatie verschijnen.

## Gerelateerde documenten

- [EULA (Engels)](./EULA_EN.md)  
- [Privacybeleid (Roemeens)](./PRIVACY_POLICY_RO.md)  
- [Privacybeleid (Duits)](./PRIVACY_POLICY_DE.md)  
- [Privacybeleid (Frans)](./PRIVACY_POLICY_FR.md)
