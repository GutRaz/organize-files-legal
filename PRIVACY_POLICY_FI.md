> **Epävirallinen konekäännös – ei oikeudellista neuvontaa.** [Englannin EULA](./EULA_EN.md) ja [Englanninkielinen tietosuojakäytäntö](./PRIVACY_POLICY_EN.md) säätelevät, jos tämä käännös on ristiriidassa niiden kanssa. Käänny oman lainkäyttöalueen pätevän neuvonantajan puoleen.

---

# Tietosuojakäytäntö — Järjestä tiedostot

**Julkaisija:** Razvan Constantin Gutulov  
**Ota yhteyttä:** razvan.gutulov@outlook.com  
**Voimaan:** 28.5.2026  
**Julkinen URL-osoite:** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_FI.md`

---

## Yhteenveto

Järjestä tiedostot käsittelee tiedostoja **paikallisesti laitteessa**. Tiedoston sisältöä **ei ladata julkaisijan omille palvelimille** normaaleja järjestely- tai korjaustoimintoja varten. Sovellus **kirjoittaa paikallisia tiedostoja** laitteeseen (istunnon tilannekuvat, jatkamistila, valinnaiset lokit) alla kuvatulla tavalla.

## Tiedot käsitellään paikallisesti

| Tiedot | Missä säilytetään | Tarkoitus |
|------|----------------|----------|
| Valitsemasi tiedostot ja kansiot | Vain laitteesi | Järjestä, poista kaksoiskappaleet, korjaa, valinnainen poista |
| Käyttöliittymän istunnon tilannekuva (`last-ui-session.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (työpöytä) tai sovellusyksityinen tallennustila (Android) | Palauta työtila: polut, laajennukset, asetukset |
| Järjestä ansioluettelo + valinnainen siirtopäiväkirja | Tulosta _OrganizeMediaLogs tai istuntokansio | Ohita valmiit liikkeet; palautuksen metatiedot (polut koodattu) |
| Valinnainen suorita syke JSON | Tulosta "_OrganizeMediaLogs" | Edistymismittarit ulkoisille työkaluille |
| Kokeilu / lisenssitila | Profiilikansio Paikalliset sovellustiedot | Toteuta kokeilu- tai kauppaoikeus |
| Päivitys-tarkistustila | Profiilikansio | Ohjaa valinnaisia ​​versioluettelotarkistuksia |
| Android SAF lavastus | Istuntokansio sovellustallennustilan alla | Kopioi "content://"-puut, jotta kone voi lukea ne |
| Valinnainen SMTP-salasana sähköposti-ilmoituksiin | Tallennetaan laitteelle istuntoasetuksiin salattuna (AES-GCM ja profiilikohtainen avaintiedosto). Päivityksen yhteydessä vanha ilman AES-GCM:ää tallennettu SMTP-salasana kirjoitetaan kerran uudelleen AES-GCM-muotoon, jos kenttä on olemassa. AES-GCM-avaintiedosto pysyy sovelluksen profiilikansiossa ja kirjautunut OS-käyttäjätili voi lukea sen; se suojaa asetusten JSON-tiedoston satunnaiselta lukemiselta, ei ole laitteistopohjainen holvi. | Vain jos otat sähköposti-ilmoitukset käyttöön ja annat SMTP-tunnukset |

## Mitä julkaisija ei saa oletusarvoisesti

- Tiedoston sisältö järjestely-/korjausajoista  
- Yhteystiedot, sijainti, mikrofoni tai kamera (ei käytössä)  
- Analyticsin SDK:t niputettuina avoimen lähdekoodin puuhun  

## Valinnainen verkon käyttö

| Toiminta | Tiedot lähetetty | Vastaanottaja |
|----------|-----------|------------|
| Valinnainen päivityksen tarkistus | HTTPS GET versioluetteloon. Isäntä (esimerkiksi GitHub) vastaanottaa pyynnön IP-osoitteen, käyttäjäagentin "OrganizeFiles-UpdateCheck/1.0" ja TLS-metatiedot. Tiedostopolkuja tai tiedoston sisältöä ei lähetetä. Poista käytöstä komennolla `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | JSON-luetteloa palveleva isäntä |
| Kauppaostos / lisenssi | Alustan laskutuksen sovellusliittymät | Microsoft, Google tai Apple (kanavaa kohti) |
| Valinnainen lisenssipalvelin (operaattorin määrittämä) | Satunnainen pysyvä asennustunnus (GUID tallennettu tiedostoon `license_installation_id.txt`) lähetetään julkaisijan ylläpitämään tai operaattorin määrittämälle lisenssipalvelimelle osoitteessa ORGANIZE_FILES_LICENSE_SERVER_URL. Asennustunnus on GDPR:n johdanto-osan 30 kappaleen mukainen laitetunnus. Laillinen perusta: sopimuksen täyttäminen. Julkaisijan ylläpitämä säilytys: oikeustietueet aktiivisuuden ajan plus enintään 24 kuukautta vanhenemisen/peruutuksen jälkeen väärinkäytön estämiseksi ja riitojen käsittelyyn; kirjanpitoaineistoa voidaan säilyttää enintään 7 vuotta lain niin vaatiessa. Operaattorin ylläpitämät palvelimet noudattavat operaattorin dokumentoitua säilytysaikataulua. Tämä ominaisuus ei ole aktiivinen, ellei ORGANIZE_FILES_LICENSE_SERVER_URL ole asetettu. | Julkaisijan tai operaattorin lisenssipalvelin |
| Valinnainen OpenTelemetry-seuranta (operaattorin määrittämä) | Kun ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT on asetettu, automaatiotyön metatiedot (työtunnukset, korrelaatiotunnukset, kohdetyyppitunnisteet, W3C-jäljityskonteksti) viedään määritettyyn OTLP-keräilijään. Mukana ei ole tiedostopolkuja tai tiedoston sisältöä. Tämä ominaisuus on oletusarvoisesti ei-aktiivinen ja vaatii nimenomaisen operaattorin määrityksen. | Käyttäjän määrittämä OTLP-keräin |
| Valinnaiset sähköposti-ilmoitukset (kun käytössä) | Suorituksen tila ja lokiotteet (voivat sisältää tiedostopolkuja) lähetetään operaattorin määrittämän SMTP-palvelimen kautta | Operaattorin SMTP / sähköpostipalvelu |
| Moottorin NAS-uudelleenyritysapuohjelmat | Ei muita kuin määritettyjä verkkopolkuja | NAS / SMB-isäntä |

Päivitystarkistukset vertaavat **vain version metatietoja**. Työpöytäsovellus voi suorittaa tämän tarkistuksen kerran päivässä EULA:n hyväksymisen jälkeen, ellei sitä ole poistettu käytöstä.

## Oikeusperustat (GDPR-tyylinen kehystys, ei oikeudellinen neuvonta)

| Käsittely | Tyypillinen perusta |
|------------|-----------------|
| Paikallinen järjestä/korjaa jo valitut kansiot | Sopimuksen täyttäminen / toiminnanharjoittajan oikeutettu etu |
| Paikallinen istunto-, ansioluettelo- ja syketiedostot | Sama — tarvitaan työkalun toimittamiseen |
| Liikkeen laskutus ja käyttöoikeudet | Sopimus alustakaupan kanssa |
| Valinnainen päivitysluettelon tarkistus | Perusteltu etu tietoturvapäivityksiä kohtaan; voidaan poistaa käytöstä ympäristömuuttujan avulla |
| Tuen sähköposti | Perusteltu etu / sopimusta edeltävät vaiheet pyynnöstäsi |

## Kansainväliset siirrot

Valinnaiset päivitystarkistukset voivat tavoittaa palvelimia Euroopan talousalueen ulkopuolella (esimerkiksi GitHub Yhdysvalloissa). Kaupan laskutus hoidetaan kunkin alustan ehtojen mukaisesti.

## Valvontaviranomainen ja valitukset

Jos sovellettava laki myöntää rekisteröidylle oikeudet tai valituksen valvontaviranomaiselle, ota ensin yhteyttä julkaisijaan osoitteessa **razvan.gutulov@outlook.com**. EU:n/ETA:n asukkaat voivat myös tehdä valituksen paikalliselle tietosuojaviranomaiselle (Romania: ANSPDCP, https://www.dataprotection.ro).

## Kolmannen osapuolen prosessorit (kun näitä ominaisuuksia käytetään)

- **Microsoft Store / Google Play / Mac App Store** - laskutus ja käyttöoikeudet. Google Play käyttää laitteen laskutusta; tuotantotietoihin tulee lisätä Play Integrity ja/tai palvelinpuolen vahvistus Googlen käytännön mukaisesti.
- **GitHub (tai manifesti-isäntä)** — valinnainen JSON-versio HTTPS:n kautta (voi sisältää asiakkaan IP:n palvelimen lokeihin)
- **Sähköpostiohjelma** — kun otat yhteyttä tukeen mailto-linkin kautta

## Operaattorin velvollisuudet (GDPR-tyylinen kehystys)

Tiedostojesi **sisällä** voi olla henkilötietoja. Jos käsittelet tällaisia ​​tietoja, sinä (tai organisaatiosi) saatat olla **rekisterinpitäjä**, ja sinun on valittava laillinen perusta, minimoitava säilytys ja vastattava tietoihin liittyviin pyyntöihin.

## Säilyttäminen

Paikalliset tiedostot säilyvät, kunnes poistat ne, tyhjennät sovellustiedot, poistat sovelluksen tai korvaat tulostuskansiot. Julkaisija ei käytä keskitettyä säilytysaikataulua vain paikallisille tiedoille.

## Sinun oikeutesi

Julkaisijan hallussa olevia tietoja (esim. tukisähköpostiviestintä) varten ota yhteyttä **razvan.gutulov@outlook.com**. Vain laitteellesi tallennetuista tiedoista voit poistaa useimmat sovellustiedot valitsemalla **Poista sovellustiedot**, poistamalla asennuksen tai poistamalla tiedostot manuaalisesti. **Tyhjennä sovellustiedot** poistaa istunnot, lokit ja automaatioluonnokset, mutta saattaa säilyttää lisenssikokeilun ankkurit, maksulliset asennusmerkit ja anonyymin asennustunnisteen, jota käytetään valinnaisiin lisenssitarkistuksiin – katso sovelluksen sisäinen vahvistusteksti ennen kuin jatkat.

## Lapset

Yleinen tuottavuustyökalu, jota ei ole suunnattu alle 13-vuotiaille (tai lainkäyttöalueellasi vaaditun iän alapuolelle).

## Muutoksia

Olennaisten muutosten pitäisi näkyä kaupan tietosivuilla ja sovelluksen sisäisissä dokumentaatioissa ennen julkaisua.

## Aiheeseen liittyvät asiakirjat

- [EULA (englanti)](./EULA_EN.md)  
- [Tietosuojakäytäntö (romania)](./PRIVACY_POLICY_RO.md)  
- [Tietosuojakäytäntö (saksa)](./PRIVACY_POLICY_DE.md)  
- [Tietosuojakäytäntö (ranska)](./PRIVACY_POLICY_FR.md)

---

Jos tämä käännös on puutteellinen, englanninkielinen tietosuojakäytäntö on määräävä.

## Rekisterinpitäjä ja yhteystiedot

Julkaisijan käsittelemien henkilötietojen rekisterinpitäjä on **Razvan Constantin Gutulov**. Yhteys: **razvan.gutulov@outlook.com**.

## Säilytys (julkaisijan tiedot)

Julkaisijan hallussa oleville tiedoille:

- Tukisähköposti ja kirjeenvaihto: enintään 24 kuukautta viimeisestä merkityksellisestä yhteydenotosta, ellei riita tai lakisääteinen velvoite edellytä pidempää säilytystä.
- Suorat ostot, hyvitykset, vero- ja kirjanpitotiedot: enintään 7 vuotta, jos vero- tai kirjanpitolaki sitä edellyttää.
- Julkaisijan ylläpitämän lisenssipalvelimen käyttöoikeustiedot: käyttöoikeuden aktiivisen ajan sekä enintään 24 kuukautta päättymisen tai peruutuksen jälkeen.
- Julkaisijan ylläpitämän palvelimen käyttö- ja suojauslokit: enintään 90 päivää, ellei pidempi aika ole tarpeen turvallisuustutkinnan, petosten ehkäisyn tai oikeusvaateiden vuoksi.

## Oikeutesi (vastausaika)

Julkaisija pyrkii vastaamaan rekisteröidyn pyyntöihin **30 päivän** kuluessa vahvistetusta pyynnöstä (henkilöllisyyden varmistusta voidaan pyytää, kun se on kohtuudella tarpeen).
