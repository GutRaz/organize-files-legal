> **Uofficiel maskinoversættelse — ikke juridisk rådgivning.** [English EULA](./EULA_EN.md) og [English Privacy Policy](./PRIVACY_POLICY_EN.md) regulerer, hvis denne oversættelse er i konflikt med dem. Kontakt kvalificeret advokat i din jurisdiktion.

---

# Privatlivspolitik — Organiser filer

**Udgiver:** Razvan Constantin Gutulov  
**Kontakt:** razvan.gutulov@outlook.com  
**Ikrafttrædelsesdato:** 2026-05-28  
**Offentlig webadresse:** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_DA.md`

---

## Resumé

Organize Files behandler filer **lokalt på enheden**. Filindhold er **ikke uploadet til udgiverens egne servere** til normal organisering eller reparation. Appen **skriver lokale filer** på enheden (sessionssnapshots, genoptagetilstand, valgfri logfiler) som beskrevet nedenfor.

## Data behandlet lokalt

| Data | Hvor opbevaret | Formål |
|------|----------------|---------|
| Filer og mapper, du vælger | Kun din enhed | Organiser, dedupliker, reparer, valgfri sletning |
| Snapshot af UI-session (`last-ui-session.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (desktop) eller app-privat lagring (Android) | Gendan arbejdsområde: stier, udvidelser, muligheder |
| Organiser CV + valgfri flyttejournal | Output `_OrganizeMediaLogs` eller sessionsmappe | Spring over gennemførte træk; gendannelsesmetadata (stier kodet) |
| Valgfrit run heartbeat JSON | Output `_OrganizeMediaLogs` | Fremskridtstællere for eksterne værktøjer |
| Prøve-/licenstilstand | Profilmappe under Local App Data | Håndhæve prøve- eller butiksberettigelse |
| Opdaterings-tjek tilstand | Profilmappe | Throttle valgfri version manifest kontrol |
| Android SAF iscenesættelse | Sessionsmappe under applagring | Kopier `content://`-træer, så motoren kan læse dem |
| Valgfri SMTP-adgangskode til e-mailnotifikationer | Gemmes krypteret i sessionspræferencer på enheden (AES-GCM med en nøglefil pr. profil). Ved opgradering omskrives en ældre SMTP-adgangskode uden AES-GCM én gang til AES-GCM, når feltet findes. AES-GCM-nøglefilen bliver i appens profilmappe og kan læses af den indloggede OS-brugerkonto; den beskytter tilfældig læsning af præference-JSON, ikke en hardwareboks. | Kun hvis e-mailnotifikationer aktiveres, og SMTP-oplysninger indtastes |

## Hvad udgiveren ikke modtager som standard

- Filindhold fra organisering/reparationskørsler  
- Kontakter, placering, mikrofon eller kamera (bruges ikke)  
- Analytics-SDK'er samlet i open source-træet  

## Valgfri netværksbrug

| Aktivitet | Data sendt | Modtager |
|--------|--------|--------|
| Valgfri opdateringskontrol | HTTPS GET til et versionsmanifest. Værten (for eksempel GitHub) modtager anmodningens IP-adresse, User-Agent `OrganizeFiles-UpdateCheck/1.0` og TLS-metadata. Ingen filstier eller filindhold sendes. Deaktiver med `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Vært, der betjener JSON-manifestet |
| Butikskøb/licens | Platformsfakturerings-API'er | Microsoft, Google eller Apple (pr. kanal) |
| Valgfri licensserver (operatørkonfigureret) | Et tilfældigt vedvarende installations-id (GUID gemt i `license_installation_id.txt`) sendes til en udgiver-drevet eller operatør-konfigureret licensserver på `ORGANIZE_FILES_LICENSE_SERVER_URL`. Installations-id'et er en enhedsidentifikator i henhold til GDPR-betragtning 30. Lovgrundlag: opfyldelse af kontrakt. Udgiverdrevet opbevaring: rettighedsregistre mens aktive plus op til 24 måneder efter udløb/tilbagekaldelse til misbrugsforebyggelse og tvister; regnskabsoptegnelser kan opbevares op til 7 år, hvor loven kræver det. Operatordrevne servere følger operatørens dokumenterede opbevaringsplan. Denne funktion er inaktiv, medmindre `ORGANIZE_FILES_LICENSE_SERVER_URL` er indstillet. | Udgiver- eller operatørlicensserver |
| Valgfri OpenTelemetry-sporing (operatørkonfigureret) | Når `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT` er indstillet, eksporteres automatiseringsjob-metadata (job-id'er, korrelations-id'er, måltype-tags, W3C-sporingskontekst) til den konfigurerede OTLP-opsamler. Ingen filstier eller filindhold er inkluderet. Denne funktion er inaktiv som standard og kræver eksplicit operatørkonfiguration. | Operatør-konfigureret OTLP-opsamler |
| Valgfri e-mailnotifikationer (når aktiveret) | Kørselsstatus og loguddrag (kan indeholde filstier) sendt via den operatorkonfigurerede SMTP-server | Operatør-SMTP / mailudbyder |
| Engine NAS genforsøg hjælpere | Ingen ud over konfigurerede netværksstier | NAS / SMB vært |

Opdateringstjek sammenligner **kun versionsmetadata**. Desktop-appen kan køre denne kontrol én gang om dagen efter EULA-accept, medmindre den er deaktiveret.

## Retsgrundlag (indramning i GDPR-stil, ikke juridisk rådgivning)

| Behandler | Typisk grundlag |
|------------|----------------|
| Lokal organisering/reparation på allerede valgte mapper | Opfyldelse af kontrakt / operatørens legitime interesse |
| Lokale sessions-, CV- og hjerteslagsfiler | Samme — nødvendigt for at levere værktøjet |
| Butiksfakturering og berettigelse | Kontrakt med platformbutikken |
| Valgfri opdateringsmanifestkontrol | Legitim interesse i sikkerhedsopdateringer; kan deaktiveres via miljøvariabel |
| Support e-mail | Berettiget interesse/trin forud for kontrakt på din anmodning |

## Internationale overførsler

Valgfri opdateringskontrol kan nå servere uden for Det Europæiske Økonomiske Samarbejdsområde (for eksempel GitHub i USA). Butiksfakturering håndteres under hver platforms vilkår.

## Tilsynsmyndighed og klager

Hvis gældende lov tildeler datasubjektrettigheder eller en klage til en tilsynsmyndighed, skal du først kontakte udgiveren på **razvan.gutulov@outlook.com**. EU/EØS-boere kan også indgive en klage til deres lokale databeskyttelsesmyndighed (for Rumænien: ANSPDCP, https://www.dataprotection.ro).

## Tredjepartsprocessorer (når disse funktioner bruges)

- **Microsoft Store / Google Play / Mac App Store** — fakturering og berettigelse. Google Play bruger fakturering på enheden; Produktionslister skal tilføje Play Integrity og/eller server-sidebekræftelse i henhold til Googles politik.
- **GitHub (eller manifest-værten)** - valgfri version JSON over HTTPS (kan inkludere klient-IP i serverlogfiler)
- **E-mail-klient** — når du kontakter support via mailto-link

## Operatøransvar (indramning i GDPR-stil)

Personlige data kan eksistere **inde i** dine filer. Hvis du behandler sådanne data, kan du (eller din organisation) være **dataansvarlig** og skal vælge et lovligt grundlag, minimere opbevaring og svare på anmodninger fra registrerede.

## Fastholdelse

Lokale filer forbliver, indtil du sletter dem, rydder appdata, afinstallerer appen eller overskriver outputmapper. Udgiveren har ikke en central opbevaringsplan for data, der kun er lokalt.

## Dine rettigheder

Kontakt **razvan.gutulov@outlook.com** for data, som udgiveren har (f.eks. support-e-mail-korrespondance). For data, der kun er gemt på din enhed, kan du slette de fleste appdata via **Ryd appdata**, afinstallation eller manuel filsletning. **Ryd appdata** fjerner sessioner, logfiler og automatiseringsudkast, men kan beholde licensprøveankre, betalte installationsmarkører og en anonym installationsidentifikator, der bruges til valgfri licenskontrol – se bekræftelsesteksten i appen, før du fortsætter.

## Børn

Generelt produktivitetsværktøj, der ikke er rettet mod børn under 13 (eller den alder, der kræves i din jurisdiktion).

## Ændringer

Væsentlige ændringer bør vises i butiksfortegnelser og i dokumentationen i appen før frigivelse.

## Relaterede dokumenter

- [EULA (engelsk)](./EULA_EN.md)  
- [Privatlivspolitik (rumænsk)](./PRIVACY_POLICY_RO.md)  
- [Privatlivspolitik (tysk)](./PRIVACY_POLICY_DE.md)  
- [Privatlivspolitik (fransk)](./PRIVACY_POLICY_FR.md)

---

Hvis denne oversættelse er ufuldstændig, gælder den engelske privatlivspolitik.

## Dataansvarlig og kontakt

For personoplysninger behandlet af udgiveren er den dataansvarlige **Razvan Constantin Gutulov**. Kontakt: **razvan.gutulov@outlook.com**.

## Opbevaring (udgiverens registre)

For data, som udgiveren opbevarer:

- Support-e-mail og korrespondance: op til 24 måneder efter den seneste meningsfulde kontakt, medmindre en tvist eller juridisk pligt kræver længere opbevaring.
- Direkte køb, refunderinger, skatte- og regnskabsoplysninger: op til 7 år, hvor skatte- eller regnskabslovgivning kræver det.
- Rettighedsregistre på en licensserver drevet af udgiveren: mens rettigheden er aktiv plus op til 24 måneder efter udløb eller tilbagekaldelse.
- Adgangs- og sikkerhedslogge på en server drevet af udgiveren: op til 90 dage, medmindre længere tid er nødvendig for sikkerhedsundersøgelse, svigforebyggelse eller juridiske krav.

## Dine rettigheder (svartid)

Udgiveren tilstræber at besvare anmodninger fra registrerede inden for **30 dage** efter en verificeret anmodning (identitetsbekræftelse kan kræves, når det med rimelighed er nødvendigt).
