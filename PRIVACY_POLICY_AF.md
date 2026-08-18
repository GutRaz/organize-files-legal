> **Nie-amptelike masjienvertaling — nie regsadvies nie.** Die [Engelse EULA](./EULA_EN.md) en [Engelse privaatheidsbeleid](./PRIVACY_POLICY_EN.md) bepaal indien hierdie vertaling met hulle bots. Raadpleeg gekwalifiseerde advokate in jou jurisdiksie.

---

# Privaatheidsbeleid - Organiseer lêers

**Uitgewer:** Razvan Constantin Gutulov  
**Kontak:** razvan.gutulov@outlook.com  
**Inwerkingtredingsdatum:** 2026-05-28  
**Publieke URL:** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_AF.md`

---

## Opsomming

Organiseer lêers verwerk lêers **plaaslik op die toestel**. Lêerinhoud word **nie na die uitgewer se eie bedieners opgelaai nie** vir normale organisering of herstelbewerkings. Die toepassing **skryf wel plaaslike lêers** op die toestel (sessiefoto's, hervattoestand, opsionele logs) soos hieronder beskryf.

## Data plaaslik verwerk

| Data | Waar gestoor | Doel |
|------|----------------|--------|
| Lêers en vouers wat jy kies | Slegs jou toestel | Organiseer, dedupliseer, herstel, opsionele verwydering |
| UI-sessie momentopname (`laaste-ui-sessie.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (rekenaar) of app-privaat berging (Android) | Herstel werkspasie: paaie, uitbreidings, opsies |
| Organiseer CV + opsionele skuifjoernaal | Voer `_OrganizeMediaLogs` of sessielêergids uit | Slaan voltooide bewegings oor; herstel metadata (paaie geënkodeer) |
| Opsionele hardloop hartklop JSON | Uitvoer `_OrganizeMediaLogs` | Vorderingstellers vir eksterne gereedskap |
| Verhoor / lisensie staat | Profielvouer onder Plaaslike toepassingdata | Dwing proef- of winkelregte af |
| Opdateer-kontroleer toestand | Profielgids | Throttle opsionele weergawe manifeskontroles |
| Android SAF-staging | Sessie-lêergids onder toepassingberging | Kopieer `content://`-bome sodat die enjin dit kan lees |
| Opsionele SMTP-wagwoord vir e-poskennisgewings | Geënkripteer in sessievoorkeure op die toestel (AES-GCM met sleutel lêer per profiel). By opgradering word enige ou SMTP-wagwoord wat sonder AES-GCM gestoor is, eenmalig na AES-GCM herskryf wanneer die veld bestaan. Die AES-GCM-sleutellêer bly in die app-profielmap en is leesbaar vir die aangemelde OS-gebruikersrekening; dit beskerm toevallige lees van voorkeure-JSON, nie ’n hardewarekluis nie. | Slegs as e-poskennisgewings geaktiveer is en SMTP-bewyse ingevoer word |

## Wat die uitgewer nie by verstek ontvang nie

- Lêerinhoud van organiseer-/herstellopies  
- Kontakte, ligging, mikrofoon of kamera (nie gebruik nie)  
- Analytics SDK's gebundel in die oopbronboom  

## Opsionele netwerkgebruik

| Aktiwiteit | Data gestuur | Ontvanger |
|--------|--------|--------|
| Opsionele opdateringkontrole | HTTPS KRY na 'n weergawemanifes. Die gasheer (byvoorbeeld GitHub) ontvang die versoek-IP-adres, User-Agent `OrganizeFiles-UpdateCheck/1.0` en TLS-metadata. Geen lêerpaaie of lêerinhoud word gestuur nie. Deaktiveer met `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Gasheer wat die JSON-manifes bedien |
| Winkel aankoop / lisensie | Platform-fakturering-API's | Microsoft, Google of Apple (per kanaal) |
| Opsionele lisensiebediener (operateur-gekonfigureerde) | 'n Ewekansige aanhoudende installasie-ID (GUID gestoor in `license_installation_id.txt`) word na 'n uitgewer-bestuurde of operateur-gekonfigureerde lisensiebediener by `ORGANIZE_FILES_LICENSE_SERVER_URL` gestuur. Die installasie-ID is 'n toestelidentifiseerder onder GDPR-oorweging 30. Wettige basis: uitvoering van kontrak. Uitgewer-beheerde behoud: regrekords terwyl aktief plus tot 24 maande na verstryking/herroeping vir misbruikvoorkoming en geskilhantering; rekeningkundige rekords mag tot 7 jaar behou word waar wet dit vereis. Operateur-bedryfde bedieners volg die operateur se gedokumenteerde bewaringskedule. Hierdie kenmerk is onaktief tensy `ORGANIZE_FILES_LICENSE_SERVER_URL` gestel is. | Uitgewer- of operateurlisensiebediener |
| Opsionele OpenTelemetry-nasporing (operateur-gekonfigureerde) | Wanneer `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT` gestel is, word outomatiseringswerk-metadata (taak-ID's, korrelasie-ID's, teikentipe-merkers, W3C-spoorkonteks) na die gekonfigureerde OTLP-versamelaar uitgevoer. Geen lêerpaaie of lêerinhoud is ingesluit nie. Hierdie kenmerk is by verstek onaktief en vereis eksplisiete operateurkonfigurasie. | Operator-gekonfigureerde OTLP-versamelaar |
| Opsionele e-poskennisgewings (wanneer geaktiveer) | Hardloopstatus en log-uittreksels (kan lêerpaaie insluit) gestuur deur die operateur-gekonfigureerde SMTP-bediener | Operateur SMTP / e-posverskaffer |
| Enjin NAS herprobeer helpers | Geen buite gekonfigureerde netwerkpaaie nie | NAS / SMB-gasheer |

Opdateringskontroles vergelyk slegs **weergawe-metadata**. Die rekenaarprogram kan hierdie tjek een keer per dag uitvoer na EULA-aanvaarding, tensy dit gedeaktiveer is.

## Regsbasisse (GDPR-styl raamwerk, nie regsadvies nie)

| Verwerking | Tipiese basis |
|------------|----------------|
| Plaaslike organiseer/herstel op dopgehou wat reeds gekies is | Nakoming van kontrak / wettige belang van die operateur |
| Plaaslike sessie-, CV- en hartkloplêers | Dieselfde — nodig om die instrument te voorsien |
| Winkelfakturering en -aanspraak | Kontrak met die platformwinkel |
| Opsionele opdateringsmanifeskontrole | Wettige belangstelling in sekuriteitsopdaterings; kan gedeaktiveer word via omgewingsveranderlike |
| Ondersteuning e-pos | Wettige belang / pre-kontraktuele stappe op u versoek |

## Internasionale oordragte

Opsionele opdateringskontroles kan bedieners buite die Europese Ekonomiese Gebied bereik (byvoorbeeld GitHub in die Verenigde State). Winkelfakturering word onder elke platform se bepalings hanteer.

## Toesighoudende gesag en klagtes

Indien toepaslike wetgewing dataonderwerpregte of 'n klagte aan 'n toesighoudende owerheid verleen, kontak eers die uitgewer by **razvan.gutulov@outlook.com**. EU/EEA-inwoners kan ook 'n klag by hul plaaslike databeskermingsowerheid indien (vir Roemenië: ANSPDCP, https://www.dataprotection.ro).

## Derdeparty-verwerkers (wanneer hierdie kenmerke gebruik word)

- **Microsoft Store / Google Play / Mac App Store** - fakturering en reg. Google Play gebruik fakturering op toestel; produksielysinskrywings moet Play-integriteit en/of bedienerkantverifikasie volgens Google-beleid byvoeg.
- **GitHub (of die manifesgasheer)** - opsionele weergawe JSON oor HTTPS (kan kliënt-IP in bedienerlogboeke insluit)
- **E-poskliënt** - wanneer ondersteuning via e-pos na skakel gekontak word

## Operateursverantwoordelikhede (GDPR-styl raamwerk)

Persoonlike data kan **binne** jou lêers wees. As jy sulke data verwerk, kan jy (of jou organisasie) 'n **databeheerder** wees en moet jy 'n wettige basis kies, behoud minimaliseer en op data-onderwerpversoeke reageer.

## Retensie

Plaaslike lêers bly totdat jy hulle uitvee, programdata uitvee, die program deïnstalleer of uitvoervouers oorskryf. Die uitgewer bedryf nie 'n sentrale bewaringskedule vir slegs plaaslike data nie.

Vir data wat deur die uitgewer gehou word:

- Ondersteunings-e-pos en korrespondensie: tot 24 maande ná die laaste betekenisvolle kontak, tensy 'n geskil of wetlike verpligting langer bewaring vereis.
- Direkte aankope, terugbetalings-, belasting- en rekeningkundige rekords: tot 7 jaar waar belasting- of rekeningkundige wetgewing dit vereis.
- Regrekords op 'n lisensiebediener wat deur die uitgewer bedryf word: terwyl die reg aktief is plus tot 24 maande ná verstryking of herroeping.
- Toegang- en sekuriteitslogboeke op 'n bediener wat deur die uitgewer bedryf word: tot 90 dae, tensy langer nodig vir sekuriteitsondersoek, bedrogvoorkoming of regseise.


## Jou regte

Kontak **razvan.gutulov@outlook.com** vir data wat die uitgewer hou (bv. steun-e-poskorrespondensie). Vir data wat net op jou toestel gestoor is, kan jy die meeste programdata uitvee via **Vee programdata uit**, deïnstallering of handmatige lêeruitvee. **Vee programdata uit** verwyder sessies, logboeke en outomatiseringskonsepte, maar kan lisensie-proefankers, betaalde-installasiemerkers en 'n anonieme installasie-identifiseerder wat vir opsionele lisensiekontroles gebruik word, behou – sien die inprogram-bevestigingsteks voordat jy voortgaan.

## Kinders

Algemene produktiwiteitsinstrument nie gerig op kinders onder 13 (of die ouderdom wat in jou jurisdiksie vereis word nie).

## Veranderinge

Materiële veranderinge moet voor vrystelling in winkellysinskrywings en inprogram-dokumentasie verskyn.

## Verwante dokumente

- [EULA (Engels)](./EULA_EN.md)  
- [Privaatheidsbeleid (Roemeens)](./PRIVACY_POLICY_RO.md)  
- [Privaatheidsbeleid (Duits)](./PRIVACY_POLICY_DE.md)  
- [Privaatheidsbeleid (Frans)](./PRIVACY_POLICY_FR.md)

---

Waar hierdie vertaling onvolledig is, geld die Engelse Privaatheidsbeleid.

## Beheerder en kontak

Vir persoonlike data wat deur die uitgewer verwerk word, is die beheerder **Razvan Constantin Gutulov**. Kontak: **razvan.gutulov@outlook.com**.

## Bewaring (uitgewerrekords)

Vir data wat deur die uitgewer gehou word:

- Ondersteunings-e-pos en korrespondensie: tot 24 maande ná die laaste betekenisvolle kontak, tensy 'n geskil of wetlike verpligting langer bewaring vereis.
- Direkte aankope, terugbetalings-, belasting- en rekeningkundige rekords: tot 7 jaar waar belasting- of rekeningkundige wetgewing dit vereis.
- Regrekords op 'n lisensiebediener wat deur die uitgewer bedryf word: terwyl die reg aktief is plus tot 24 maande ná verstryking of herroeping.
- Toegang- en sekuriteitslogboeke op 'n bediener wat deur die uitgewer bedryf word: tot 90 dae, tensy langer nodig vir sekuriteitsondersoek, bedrogvoorkoming of regseise.

## Jou regte (reaksietyd)

Die uitgewer mik daarna om versoeke van datasubjekte binne **30 dae** ná 'n geverifieerde versoek te beantwoord (identiteitsverifikasie kan gevra word wanneer dit redelikerwys nodig is).
