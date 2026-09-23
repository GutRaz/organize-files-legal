> **Käännös tarjotaan avuksi.** Viiteversiot ovat [englanninkielinen EULA](../en/eula.md) ja [englanninkielinen tietosuojakäytäntö](../en/privacy-policy.md). Jos maasi pakottava kuluttajalainsäädäntö antaa etusijan omalla kielelläsi olevalle versiolle, sovelletaan sitä versiota. Ei oikeudellista neuvontaa — käänny pätevän asianajajan puoleen omalla lainkäyttöalueellasi.

---

# Tietosuojakäytäntö — Organize Files

**Julkaisija:** Guțulov Răzvan Constantin PFA  
**Rekisteröity osoite:** Str. Republicii nr. 33B, bl. N3, sc. A, et. 1, ap. 3, Breaza de Sus, 105400 Breaza, jud. Prahova, România  
**Kaupparekisteri:** F2026004513003 (EUID ROONRC.F2026004513003)  
**Verotunniste:** 53610310  
**Ota yhteyttä:** razvan.gutulov@outlook.com  
**Voimaan:** 28.5.2026  
**Julkinen URL-osoite:** `https://github.com/GutRaz/organize-files-legal/blob/main/fi/privacy-policy.md`

---

## Yhteenveto

Organize Files käsittelee tiedostoja **paikallisesti laitteessa**. Tiedoston sisältöä **ei ladata julkaisijan omille palvelimille** normaaleja järjestely- tai korjaustoimintoja varten. Sovellus **kirjoittaa paikallisia tiedostoja** laitteeseen (istunnon tilannekuvat, jatkamistila, valinnaiset lokit) alla kuvatulla tavalla.

## Rekisterinpitäjä ja yhteystiedot

Julkaisijan käsittelemien henkilötietojen rekisterinpitäjä on **Guțulov Răzvan Constantin PFA**. Yhteys: **razvan.gutulov@outlook.com**.

## Tiedot käsitellään paikallisesti

| Tiedot | Missä säilytetään | Tarkoitus |
|------|----------------|----------|
| Valitsemasi tiedostot ja kansiot | Vain laitteessasi | Järjestäminen, kaksoiskappaleiden haku, korjaus ja poisto, kun se valitaan |
| Käyttöliittymän istunnon tilannekuva (`last-ui-session.json`) | Kansio `sessions\<id>\` sovelluksen profiilikansiossa: `%LocalAppData%\OrganizeFilesCrossPlatform` Windowsissa, `~/Library/Application Support/OrganizeFilesCrossPlatform` macOS:ssä, `~/.local/share/OrganizeFilesCrossPlatform` Linuxissa tai sovelluksen yksityinen tallennustila Androidissa ja iOS:ssä | Palauta työtila: polut, laajennukset, asetukset |
| Järjestelyajon jatkamistila + valinnainen siirtoloki | `_OrganizeMediaLogs` tuloskansiossa tai istuntokansio | Jo tehtyjen siirtojen ohitus, palautustiedot koodatuin poluin |
| Valinnainen ajon edistymistiedosto, JSON | `_OrganizeMediaLogs` tuloskansiossa | Edistymislaskurit muille ohjelmille |
| Kokeilun ja lisenssin tila | Sovelluksen profiilikansio | Kokeilun tai kauppaoston soveltaminen |
| Päivitystarkistuksen tila | Sovelluksen profiilikansio | Rajoittaa, kuinka usein valinnainen versiotarkistus suoritetaan |
| Android: kopiot järjestelmän valitsimella SAF valituista kansioista | Istuntokansio sovelluksen tallennustilassa | Kopioi `content://`-kansiopuut, jotta moottori voi lukea ne |
| Valinnainen SMTP-salasana sähköposti-ilmoituksiin | Tallennetaan laitteelle istuntoasetuksiin salattuna (AES-GCM ja profiilikohtainen avaintiedosto). Päivityksen yhteydessä vanha ilman AES-GCM:ää tallennettu SMTP-salasana kirjoitetaan kerran uudelleen AES-GCM-muotoon, jos kenttä on olemassa. AES-GCM-avaintiedosto pysyy sovelluksen profiilikansiossa ja kirjautunut OS-käyttäjätili voi lukea sen; se suojaa asetusten JSON-tiedoston satunnaiselta lukemiselta, ei ole laitteistopohjainen holvi. | Vain jos otat sähköposti-ilmoitukset käyttöön ja annat SMTP-tunnukset |

## Mitä julkaisija ei saa oletusarvoisesti

- Tiedoston sisältö järjestely-/korjausajoista  
- Yhteystiedot, sijainti, mikrofoni tai kamera (ei käytössä)  
- Analytiikka- tai mainosdata (sovellus ei sisällä tällaista SDK:ta)  
- Paikallisesti tallentamasi SMTP-salasanat (ne pysyvät laitteessasi, ellet lähetä postia oman SMTP-palvelimesi kautta)

## Valinnainen verkon käyttö

| Toiminta | Tiedot lähetetty | Vastaanottaja |
|----------|-----------|------------|
| Valinnainen päivityksen tarkistus | HTTPS GET versioluetteloon. Isäntä (esimerkiksi GitHub) vastaanottaa pyynnön IP-osoitteen, käyttäjäagentin "OrganizeFiles-UpdateCheck/1.0" ja TLS-metatiedot. Tiedostopolkuja tai tiedoston sisältöä ei lähetetä. Poista käytöstä komennolla `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | JSON-luetteloa palveleva isäntä |
| Kauppaostos / lisenssi | Alustan laskutuksen sovellusliittymät | Microsoft, Google tai Apple (kanavaa kohti) |
| Valinnainen lisenssipalvelin (operaattorin määrittämä) | Satunnainen pysyvä asennustunnus (GUID tallennettu tiedostoon `license_installation_id.txt`) lähetetään julkaisijan ylläpitämään tai operaattorin määrittämälle lisenssipalvelimelle osoitteessa ORGANIZE_FILES_LICENSE_SERVER_URL. Asennustunnus on GDPR:n johdanto-osan 30 kappaleen mukainen laitetunnus. Laillinen perusta: sopimuksen täyttäminen. Julkaisijan ylläpitämä säilytys: oikeustietueet aktiivisuuden ajan plus enintään 24 kuukautta vanhenemisen/peruutuksen jälkeen väärinkäytön estämiseksi ja riitojen käsittelyyn; kirjanpitoaineistoa voidaan säilyttää enintään 7 vuotta lain niin vaatiessa. Operaattorin ylläpitämät palvelimet noudattavat operaattorin dokumentoitua säilytysaikataulua. Tämä ominaisuus ei ole aktiivinen, ellei ORGANIZE_FILES_LICENSE_SERVER_URL ole asetettu. | Julkaisijan tai operaattorin lisenssipalvelin |
| Valinnainen OpenTelemetry-seuranta (operaattorin määrittämä) | Kun ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT on asetettu, automaatiotyön metatiedot (työtunnukset, korrelaatiotunnukset, kohdetyyppitunnisteet, W3C-jäljityskonteksti) viedään määritettyyn OTLP-keräilijään. Mukana ei ole tiedostopolkuja tai tiedoston sisältöä. Tämä ominaisuus on oletusarvoisesti ei-aktiivinen ja vaatii nimenomaisen operaattorin määrityksen. | Käyttäjän määrittämä OTLP-keräin |
| Valinnaiset sähköposti-ilmoitukset (kun käytössä) | Suorituksen tila ja lokiotteet (voivat sisältää tiedostopolkuja) lähetetään operaattorin määrittämän SMTP-palvelimen kautta | Operaattorin SMTP / sähköpostipalvelu |
| Valinnaiset automaation webhookit (ylläpitäjän määrittämät) | Kun `ORGANIZE_FILES_AUTOMATION_WEBHOOK_URL` on asetettu, työn elinkaaren tapahtumat, joissa on korrelaatiotunnisteet ja automaation tilatiedostojen polut | Ylläpitäjän määrittämä webhook-päätepiste |
| Valinnainen henkilöllisyyden tarkistus suorituksen hyväksynnässä (operaattorin määrittämä) | Kun `ORGANIZE_FILES_APPROVE_OAUTH_JWKS_URL` on asetettu, HTTPS GET hakee allekirjoitusavaimet ja pitää ne välimuistissa tunnin; laitteesta ei lähde token. Kun `ORGANIZE_FILES_APPROVE_OAUTH_INTROSPECTION_URL` on asetettu, operaattorin oma bearer-token lähetetään tähän päätepisteeseen tarkistettavaksi (RFC 7662), HTTP Basic -asiakastunnuksin jos ne on määritetty. Ei käytössä, ellei toista näistä osoitteista ole asetettu. | Operaattorin määrittämä tunnistetietojen tarjoaja |
| Moottorin NAS-uudelleenyritysapuohjelmat | Ei muita kuin määritettyjä verkkopolkuja | NAS / SMB-isäntä |

Päivitystarkistukset vertaavat **vain version metatietoja**. Työpöytäsovellus voi suorittaa tämän tarkistuksen kerran päivässä EULA:n hyväksymisen jälkeen, ellei sitä ole poistettu käytöstä.

## Oikeusperustat (GDPR-tyylinen kehystys, ei oikeudellinen neuvonta)

| Käsittely | Tyypillinen perusta |
|------------|-----------------|
| Paikallinen järjestä/korjaa jo valitut kansiot | Sopimuksen täyttäminen / toiminnanharjoittajan oikeutettu etu |
| Paikalliset istunto-, jatkamis- ja edistymistiedostot | Sama, tarpeen työkalun tarjoamiseksi |
| Liikkeen laskutus ja käyttöoikeudet | Sopimus alustakaupan kanssa |
| Valinnainen päivitysluettelon tarkistus | Perusteltu etu tietoturvapäivityksiä kohtaan; voidaan poistaa käytöstä ympäristömuuttujan avulla |
| Tuen sähköposti | Perusteltu etu / sopimusta edeltävät vaiheet pyynnöstäsi |

## Kansainväliset siirrot

Valinnaiset päivitystarkistukset voivat tavoittaa palvelimia Euroopan talousalueen ulkopuolella (esimerkiksi GitHub Yhdysvalloissa). Kaupan laskutus hoidetaan kunkin alustan ehtojen mukaisesti.

## Valvontaviranomainen ja valitukset

Jos sovellettava laki myöntää rekisteröidylle oikeudet tai valituksen valvontaviranomaiselle, ota ensin yhteyttä julkaisijaan osoitteessa **razvan.gutulov@outlook.com**. EU:n/ETA:n asukkaat voivat myös tehdä valituksen paikalliselle tietosuojaviranomaiselle (Romania: ANSPDCP, https://www.dataprotection.ro).

## Kolmannen osapuolen prosessorit (kun näitä ominaisuuksia käytetään)

- **Microsoft Store / Google Play / Mac App Store** - laskutus ja käyttöoikeudet. Google Play vahvistaa ostot laitteessa.
- **GitHub (tai manifesti-isäntä)** — valinnainen JSON-versio HTTPS:n kautta (voi sisältää asiakkaan IP:n palvelimen lokeihin)
- **Sähköpostiohjelma** — kun otat yhteyttä tukeen mailto-linkin kautta

## Operaattorin velvollisuudet (GDPR-tyylinen kehystys)

Tiedostojesi **sisällä** voi olla henkilötietoja. Jos käsittelet tällaisia ​​tietoja, sinä (tai organisaatiosi) saatat olla **rekisterinpitäjä**, ja sinun on valittava laillinen perusta, minimoitava säilytys ja vastattava tietoihin liittyviin pyyntöihin.

## Säilyttäminen

Paikalliset tiedostot säilyvät, kunnes poistat ne, tyhjennät sovellustiedot, poistat sovelluksen tai korvaat tulostuskansiot. Julkaisija ei käytä keskitettyä säilytysaikataulua vain paikallisille tiedoille.
Julkaisijan hallussa oleville tiedoille:

- Tukisähköposti ja kirjeenvaihto: enintään 24 kuukautta viimeisestä merkityksellisestä yhteydenotosta, ellei riita tai lakisääteinen velvoite edellytä pidempää säilytystä.
- Suorat ostot, hyvitykset, vero- ja kirjanpitotiedot: enintään 7 vuotta, jos vero- tai kirjanpitolaki sitä edellyttää.
- Julkaisijan ylläpitämän lisenssipalvelimen käyttöoikeustiedot: käyttöoikeuden aktiivisen ajan sekä enintään 24 kuukautta päättymisen tai peruutuksen jälkeen.
- Julkaisijan ylläpitämän palvelimen käyttö- ja suojauslokit: enintään 90 päivää, ellei pidempi aika ole tarpeen turvallisuustutkinnan, petosten ehkäisyn tai oikeusvaateiden vuoksi.

## Sinun oikeutesi

Julkaisijan hallussa olevia tietoja (esim. tukisähköpostiviestintä) varten ota yhteyttä **razvan.gutulov@outlook.com**. Vain laitteellesi tallennetuista tiedoista voit poistaa useimmat sovellustiedot valitsemalla **Poista sovellustiedot**, poistamalla asennuksen tai poistamalla tiedostot manuaalisesti. **Tyhjennä sovellustiedot** poistaa istunnot, lokit ja automaatioluonnokset, mutta saattaa säilyttää lisenssikokeilun ankkurit, maksulliset asennusmerkit ja asennustunnisteen, jota käytetään valinnaisiin lisenssitarkistuksiin – katso sovelluksen sisäinen vahvistusteksti ennen kuin jatkat. Soveltuvin osin voit pyytää pääsyä tietoihin, niiden oikaisua tai poistamista, käsittelyn rajoittamista, vastustaa käsittelyä, pyytää tietojen siirrettävyyttä tai peruuttaa suostumuksesi.

Julkaisija pyrkii vastaamaan rekisteröidyn pyyntöihin sovellettavan lain vaatiman ajan kuluessa vahvistetusta pyynnöstä (henkilöllisyyden varmistusta voidaan pyytää, kun se on kohtuudella tarpeen).

## Lapset

Yleinen tuottavuustyökalu, jota ei ole suunnattu alle 13-vuotiaille (tai lainkäyttöalueellasi vaaditun iän alapuolelle).

## Muutoksia

Olennaisten muutosten pitäisi näkyä kaupan tietosivuilla ja sovelluksen sisäisissä dokumentaatioissa ennen julkaisua.

## Aiheeseen liittyvät asiakirjat

- [EULA (englanti)](../en/eula.md)  
- [Tietosuojakäytäntö (romania)](../ro/privacy-policy.md)  
- [Tietosuojakäytäntö (saksa)](../de/privacy-policy.md)  
- [Tietosuojakäytäntö (ranska)](../fr/privacy-policy.md)

---

Jos tämä käännös on puutteellinen, englanninkielinen tietosuojakäytäntö on määräävä.
