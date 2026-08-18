> **Suomenkielinen versio.** Ristiriitatilanteessa [englanninkielinen](./DATA_DELETION.md) versio on määräävä.

---

# Tietojen poistaminen — Organize Files

**Organize Files** käsittelee tiedostosi **paikallisesti laitteessasi**.
Julkaisija **ei** ylläpidä tilijärjestelmää eikä tallenna tiedostojasi omille
palvelimilleen tavallisten järjestely- tai korjaustoimintojen aikana. Koska
palvelinpuolen tiliä ei ole, suurin osa tiedoistasi ei koskaan poistu
laitteeltasi ja säilytät niihin täyden hallinnan.

Tällä sivulla kerrotaan, miten poistat sovelluksen laitteellesi tallentamat
tiedot sekä ne rajalliset tiedot, joita julkaisija voi säilyttää.

## Laitteellesi tallennetut tiedot

Sovellus tallentaa paikallisia työtietoja, kuten istunnon tilannevedoksia,
jatkamistilan, valinnaisia lokeja, kokeilu-/lisenssitilan ja – vain jos otat
sähköposti-ilmoitukset käyttöön – salatun SMTP-salasanan. Voit poistaa ne milloin
tahansa:

1. **Tyhjennä sovelluksen tiedot** — avaa sovellus ja käytä toimintoa **Tyhjennä
   sovelluksen tiedot**. Tämä poistaa istunnot, lokit ja automaatioluonnokset. Se
   voi säilyttää paikallisen lisenssitilan ja anonyymin asennustunnisteen, jota
   käytetään valinnaisiin lisenssitarkistuksiin; sovelluksen vahvistus kertoo
   tarkalleen, mitä säilytetään.
2. **Poista sovellus** — sovelluksen poistaminen tyhjentää sen yksityisen
   tallennustilan mobiililaitteella. Työpöydällä voit myös poistaa profiilikansion
   manuaalisesti:
   - Windows: `%LocalAppData%\OrganizeFilesCrossPlatform\`
   - Linux / macOS: sovelluksen profiilikansio kotihakemistossasi
3. **Poista tuloskansiot** — kaikki luomasi järjestellyt tai korjatut tiedostot
   säilyvät, kunnes poistat ne itse.

## Tiedot, joita julkaisija voi säilyttää

Julkaisija säilyttää vain tietoja, jotka lähetät aktiivisesti, kuten:

- **Tukisähköposti**viestintä, jos otat yhteyttä tukeen
- **Lisenssipalvelimen tietueet**, vain jos koontiversiollesi on määritetty
  lisenssipalvelin

Pyytääksesi näiden tietojen poistamista, kirjoita osoitteeseen
**razvan.gutulov@outlook.com** ja liitä mukaan:

- Sähköpostiosoite, jolla otit yhteyttä tukeen, ja/tai
- Lisenssi- tai tilausviitteesi, jos sellainen on

Julkaisija pyrkii vastaamaan **30 päivän** kuluessa vahvistetusta pyynnöstä.
Joitakin tietueita voidaan säilyttää lain vaatiessa (esimerkiksi vero- ja
kirjanpitoaineisto). Katso [Tietosuojakäytäntö](./PRIVACY_POLICY_FI.md) saadaksesi
kaikki tiedot säilytyksestä.

## Ostokset kaupoissa

Ostokset ja laskutus hoitaa kauppa, josta ostit (Microsoft Store, Google Play tai
Apple App Store). Hallitaksesi tai poistaaksesi kaupan säilyttämiä ostotietoja
käytä kyseisen kaupan tiliasetuksia.

---

© 2026 Razvan Constantin Gutulov. Kaikki oikeudet pidätetään.
