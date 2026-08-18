> **Tafsiri isiyo rasmi kwa mashine — si ushauri wa kisheria.** [Kiingereza EULA](./EULA_EN.md) na [Sera ya Faragha ya Kiingereza](./PRIVACY_POLICY_EN.md) hutawala ikiwa tafsiri hii inakinzana nazo. Wasiliana na mshauri aliyehitimu katika mamlaka yako.

---

# Sera ya Faragha - Panga Faili

**Mchapishaji:** Razvan Constantin Gutulov  
**Mawasiliano:** razvan.gutulov@outlook.com  
**Tarehe ya kuanza kutumika:** 2026-05-28  
**URL ya Umma:** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_SW.md`

---

## Muhtasari

Panga Faili huchakata faili **ndani kwenye kifaa**. Yaliyomo kwenye faili **hayajapakiwa kwa seva za mchapishaji mwenyewe** kwa shughuli za kawaida za kupanga au kurekebisha. Programu **huandika faili za ndani** kwenye kifaa (picha za kipindi, hali ya kuanza tena, kumbukumbu za hiari) kama ilivyoelezwa hapa chini.

## Data imechakatwa ndani

| Data | Mahali pa kuhifadhiwa | Kusudi |
|------|--------------------------|
| Faili na folda unazochagua | Kifaa chako pekee | Panga, punguza, rekebisha, futa kwa hiari |
| Muhtasari wa kipindi cha UI (`last-ui-session.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (desktop) au hifadhi ya kibinafsi ya programu (Android) | Rejesha nafasi ya kazi: njia, viendelezi, chaguo |
| Panga wasifu + shajara ya hiari ya kuhamisha | Toa `_OrganizeMediaLogs` au folda ya kipindi | Ruka hatua zilizokamilishwa; metadata ya uokoaji (njia zilizosimbwa) |
| Hiari ya kukimbia mapigo ya moyo JSON | Pato `_Organize MediaLogs` | Vihesabu vya maendeleo kwa zana za nje |
| Jaribio / hali ya leseni | Folda ya wasifu chini ya Data ya Ndani ya Programu | Tekeleza haki ya kujaribu au kuhifadhi |
| Sasisha-angalia hali | Folda ya wasifu | Kagua toleo la hiari la Throttle |
| Programu ya Android SAF | Folda ya kipindi chini ya hifadhi ya programu | Nakili `maudhui://` miti ili injini iweze kuisoma |
| Nenosiri la hiari la SMTP kwa arifa za barua pepe | Huhifadhiwa kwa usimbaji fiche katika mapendeleo ya kipindi kwenye kifaa (AES-GCM kwa faili ya ufunguo kwa kila wasifu). Wakati wa kusasisha, ikiwa sehemu ipo, nenosiri la zamani la SMTP lililohifadhiwa bila AES-GCM huandikwa upya mara moja kwa AES-GCM. Faili ya ufunguo ya AES-GCM hubaki kwenye folda ya wasifu wa programu na inaweza kusomwa na akaunti ya mtumiaji wa OS aliyeingia; hulinda usomaji wa kawaida wa JSON ya mapendeleo, si hifadhi ya maunzi. | Iwapo tu arifa za barua pepe zimewashwa na vitambulisho vya SMTP vimeingizwa |

## Kile ambacho mchapishaji hakipokei kwa chaguo-msingi

- Yaliyomo kwenye faili kutoka kwa uendeshaji / urekebishaji  
- Anwani, eneo, maikrofoni, au kamera (haitumiki)  
- SDK za uchanganuzi zilizounganishwa kwenye mti wa chanzo huria  

## Utumiaji wa mtandao wa hiari

| Shughuli | Data imetumwa | Mpokeaji |
|----------|-----------|-----------|
| Hundi ya hiari ya sasisho | HTTPS GET kwa faili ya maelezo ya toleo. Mpangishi (kwa mfano GitHub) hupokea ombi la anwani ya IP, Wakala wa Mtumiaji `OrganizeFiles-UpdateCheck/1.0`, na metadata ya TLS. Hakuna njia za faili au yaliyomo kwenye faili hutumwa. Zima kwa `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Mpangishi anayehudumia faili ya maelezo ya JSON |
| Ununuzi wa duka / leseni | API za bili za jukwaa | Microsoft, Google, au Apple (kwa kila kituo) |
| Seva ya leseni ya hiari (imesanidiwa na kiendeshaji) | Kitambulisho cha usakinishaji unaoendelea bila mpangilio (GUID iliyohifadhiwa katika `leseni_installation_id.txt`) hutumwa kwa seva ya leseni inayoendeshwa na mchapishaji au iliyosanidiwa na opereta katika `ORGANIZE_FILES_LICENSE_SERVER_URL`. Kitambulisho cha usakinishaji ni kitambulisho cha kifaa chini ya GDPR Recital 30. Msingi halali: utendaji wa mkataba. Uhifadhi unaoendeshwa na mchapishaji: rekodi za haki wakati zikiwa hai pamoja na hadi miezi 24 baada ya kuisha/kufutwa kwa kuzuia matumizi mabaya na utatuzi wa migogoro; rekodi za uhasibu zinaweza kuhifadhiwa hadi miaka 7 pale sheria inapohitaji. Seva zinazoendeshwa na opereta hufuata ratiba ya uhifadhi iliyoandikwa ya opereta. Kipengele hiki hakitumiki isipokuwa `ORGANIZE_FILES_LICENSE_SERVER_URL` kimewekwa. | Mchapishaji au seva ya leseni ya mwendeshaji |
| Ufuatiliaji wa hiari wa OpenTelemetry (kiendeshaji kimesanidiwa) | `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT` inapowekwa, metadata ya kazi ya otomatiki (Vitambulisho vya kazi, vitambulisho vya uunganisho, lebo za aina inayolengwa, muktadha wa ufuatiliaji wa W3C) inatumwa kwa kikusanyaji kilichosanidiwa cha OTLP. Hakuna njia faili au yaliyomo faili ni pamoja. Kipengele hiki hakitumiki kwa chaguo-msingi na kinahitaji usanidi wazi wa opereta. | Kikusanyaji cha OTLP kilichosanidiwa na opereta |
| Arifa za barua pepe za hiari (zinapowashwa) | Hali ya uendeshaji na sehemu za kumbukumbu (zinaweza kujumuisha njia za faili) zinazotumwa kupitia seva ya SMTP iliyosanidiwa na opereta | SMTP ya opereta / mtoa huduma wa barua pepe |
| Injini NAS jaribu tena wasaidizi | Hakuna zaidi ya njia za mtandao zilizosanidiwa | Mwenyeji wa NAS / SMB |

Ukaguzi wa sasisho unalinganisha **metadata ya toleo pekee**. Programu ya eneo-kazi inaweza kutekeleza ukaguzi huu mara moja kwa siku baada ya kukubalika kwa EULA isipokuwa kama imezimwa.

## Misingi ya kisheria (mtindo wa GDPR, sio ushauri wa kisheria)

| Inachakata | Msingi wa kawaida |
|-----------------------------|
| Panga/rekebisha kwenye folda zilizochaguliwa tayari | Utendaji wa mkataba / maslahi halali ya operator |
| Kipindi cha ndani, endelea, na faili za mapigo ya moyo | Sawa - inahitajika kutoa zana |
| Malipo ya duka na haki | Mkataba na duka la jukwaa |
| Ukaguzi wa hiari wa sasisho | Nia halali katika sasisho za usalama; inaweza kulemazwa kupitia kutofautisha kwa mazingira |
| Barua pepe ya usaidizi | Maslahi halali / hatua za awali za mkataba kwa ombi lako |

## Uhamisho wa kimataifa

Ukaguzi wa hiari wa sasisho unaweza kufikia seva nje ya Eneo la Kiuchumi la Ulaya (kwa mfano GitHub nchini Marekani). Malipo ya duka yanashughulikiwa chini ya sheria na masharti ya kila jukwaa.

## Mamlaka ya usimamizi na malalamiko

Ikiwa sheria inayotumika inatoa haki za data au malalamiko kwa mamlaka ya usimamizi, wasiliana na mchapishaji kwanza kupitia **razvan.gutulov@outlook.com**. Wakazi wa EU/EEA wanaweza pia kuwasilisha malalamiko kwa mamlaka ya eneo lao ya ulinzi wa data (kwa Romania: ANSPDCP, https://www.dataprotection.ro).

## Wachakataji wa wahusika wengine (vipengele hivi vinapotumika)

- **Duka la Microsoft / Google Play / Mac App Store** - bili na haki. Google Play hutumia Utozaji kwenye kifaa; uorodheshaji wa uzalishaji unapaswa kuongeza Uadilifu wa Play na/au uthibitishaji wa upande wa seva kwa kila sera ya Google.
- **GitHub (au seva pangishi ya maelezo)** — toleo la hiari la JSON juu ya HTTPS (linaweza kujumuisha IP ya mteja kwenye kumbukumbu za seva)
- **Mteja wa barua pepe** — unapowasiliana na usaidizi kupitia kiungo cha mailto

## Majukumu ya waendeshaji (uundaji wa mtindo wa GDPR)

Data ya kibinafsi inaweza kuwepo **ndani** ya faili zako. Ukichakata data kama hiyo, wewe (au shirika lako) unaweza kuwa **kidhibiti data** na lazima uchague msingi halali, upunguze uhifadhi, na ujibu maombi ya mada ya data.

## Uhifadhi

Faili za karibu nawe zitasalia hadi uzifute, ufute data ya programu, uondoe programu au ubatilishe folda za towe. Mchapishaji hafanyi kazi ratiba kuu ya uhifadhi kwa data ya ndani pekee.

##Haki zako

Kwa data aliyonayo mchapishaji (k.m. mawasiliano ya barua pepe ya usaidizi), wasiliana na **razvan.gutulov@outlook.com**. Kwa data iliyohifadhiwa kwenye kifaa chako pekee, unaweza kufuta data nyingi za programu kupitia **Futa data ya programu**, sanidua au kufuta faili mwenyewe. **Futa data ya programu** huondoa vipindi, kumbukumbu na rasimu za otomatiki, lakini inaweza kubaki na viambajengo vya majaribio ya leseni, vialama vya usakinishaji unaolipishwa na kitambulisho cha usakinishaji kisichokutambulisha kinachotumika kwa ukaguzi wa hiari wa leseni - angalia maandishi ya uthibitishaji wa ndani ya programu kabla ya kuendelea.

#Watoto

Zana ya jumla ya tija isiyoelekezwa kwa watoto walio na umri wa chini ya miaka 13 (au umri unaohitajika katika eneo lako la mamlaka).

##Mabadiliko

Mabadiliko muhimu yanapaswa kuonekana katika kurasa za programu katika Google Play na hati za ndani ya programu kabla ya kutolewa.

Kwa data inayoshikiliwa na mchapishaji:

- Barua pepe za usaidizi na mawasiliano: hadi miezi 24 baada ya mawasiliano ya mwisho yenye maana, isipokuwa mgogoro au wajibu wa kisheria uhitaji uhifadhi mrefu zaidi.
- Rekodi za ununuzi wa moja kwa moja, marejesho, kodi na uhasibu: hadi miaka 7 pale sheria ya kodi au uhasibu inapohitaji.
- Rekodi za haki kwenye seva ya leseni inayoendeshwa na mchapishaji: wakati haki iko hai pamoja na hadi miezi 24 baada ya kuisha au kufutwa.
- Logi za ufikiaji na usalama kwenye seva inayoendeshwa na mchapishaji: hadi siku 90, isipokuwa muda mrefu zaidi unahitajika kwa uchunguzi wa usalama, kuzuia udanganyifu au madai ya kisheria.


## Hati zinazohusiana

- [EULA (Kiingereza)](./EULA_EN.md)  
- [Sera ya Faragha (Kirumi)](./PRIVACY_POLICY_RO.md)  
- [Sera ya Faragha (Kijerumani)](./PRIVACY_POLICY_DE.md)  
- [Sera ya Faragha (Kifaransa)](./PRIVACY_POLICY_FR.md)

---

Ambapo tafsiri hii haijakamilika, Sera ya Faragha ya Kiingereza ndiyo itatumika.

## Mdhibiti na mawasiliano

Kwa data binafsi inayochakatwa na mchapishaji, mdhibiti ni **Razvan Constantin Gutulov**. Mawasiliano: **razvan.gutulov@outlook.com**.

## Uhifadhi (rekodi za mchapishaji)

Kwa data inayoshikiliwa na mchapishaji:

- Barua pepe za usaidizi na mawasiliano: hadi miezi 24 baada ya mawasiliano ya mwisho yenye maana, isipokuwa mgogoro au wajibu wa kisheria uhitaji uhifadhi mrefu zaidi.
- Rekodi za ununuzi wa moja kwa moja, marejesho, kodi na uhasibu: hadi miaka 7 pale sheria ya kodi au uhasibu inapohitaji.
- Rekodi za haki kwenye seva ya leseni inayoendeshwa na mchapishaji: wakati haki iko hai pamoja na hadi miezi 24 baada ya kuisha au kufutwa.
- Logi za ufikiaji na usalama kwenye seva inayoendeshwa na mchapishaji: hadi siku 90, isipokuwa muda mrefu zaidi unahitajika kwa uchunguzi wa usalama, kuzuia udanganyifu au madai ya kisheria.

## Haki zako (muda wa kujibu)

Mchapishaji analenga kujibu maombi ya wahusika wa data ndani ya **siku 30** baada ya ombi kuthibitishwa (uthibitisho wa utambulisho unaweza kuombwa inapohitajika kwa busara).
