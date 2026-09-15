> **A fordítást a könnyebb tájékozódás érdekében adjuk közre.** A referenciaváltozatok az [angol EULA](../en/eula.md) és az [angol adatvédelmi szabályzat](../en/privacy-policy.md). Ahol az Ön országának kógens fogyasztóvédelmi joga elsőbbséget ad az Ön saját nyelvén készült változatnak, az a változat irányadó. Ez nem jogi tanács — forduljon szakképzett ügyvédhez a saját joghatóságában.

---

# Adatvédelmi szabályzat — Organize Files

**Kiadó:** Guțulov Răzvan Constantin PFA  
**Bejegyzett cím:** Str. Republicii nr. 33B, bl. N3, sc. A, et. 1, ap. 3, Breaza de Sus, 105400 Breaza, jud. Prahova, România  
**Cégjegyzék:** F2026004513003 (EUID ROONRC.F2026004513003)  
**Adóazonosító szám:** 53610310  
**Kapcsolat:** razvan.gutulov@outlook.com  
**Hatálybalépés dátuma:** 2026-05-28  
**Nyilvános URL:** `https://github.com/GutRaz/organize-files-legal/blob/main/hu/privacy-policy.md`

---

## Összegzés

Az Organize Files **helyben, az eszközön** dolgozza fel a fájlokat. A fájl tartalma **nem kerül feltöltésre a kiadó saját szervereire** normál rendszerezési vagy javítási műveletekhez. Az alkalmazás **helyi fájlokat** ír az eszközön (munkamenet-pillanatképek, folytatási állapot, opcionális naplók) az alábbiak szerint.

## Adatkezelő és kapcsolat

A kiadó által kezelt személyes adatok adatkezelője **Guțulov Răzvan Constantin PFA**. Kapcsolat: **razvan.gutulov@outlook.com**.

## Az adatok helyben feldolgozva

| Adatok | A tárolás helye | Cél |
|------|----------------|----------|
| A kiválasztott fájlok és mappák | Csak az eszközön | Rendezés, ismétlődések keresése, javítás és törlés, ha ki van választva |
| UI munkamenet pillanatképe (`last-ui-session.json`) | Az alkalmazás profilmappájában lévő `sessions\<id>\` mappa: `%LocalAppData%\OrganizeFilesCrossPlatform` Windows rendszeren, `~/Library/Application Support/OrganizeFilesCrossPlatform` macOS rendszeren, `~/.local/share/OrganizeFilesCrossPlatform` Linux rendszeren, illetve az alkalmazás privát tárhelye Androidon és iOS-en | Munkaterület visszaállítása: elérési utak, bővítmények, beállítások |
| Rendezési futtatás folytatási állapota + opcionális áthelyezési napló | `_OrganizeMediaLogs` a kimeneti mappában, vagy a munkamenet mappája | A már elvégzett áthelyezések kihagyása, helyreállítási adatok kódolt útvonalakkal |
| Egy futtatás opcionális állapotfájlja, JSON | `_OrganizeMediaLogs` a kimeneti mappában | Állapotszámlálók más programok számára |
| Próbaidő és licenc állapota | Az alkalmazás profilmappája | A próbaidő vagy az áruházi vásárlás érvényesítése |
| Frissítés-ellenőrzés állapota | Az alkalmazás profilmappája | Korlátozza, milyen gyakran fut az opcionális verzióellenőrzés |
| Android: a rendszer választójával, SAF, kiválasztott mappák másolatai | Munkamenet-mappa az alkalmazás tárhelyén | A `content://` mappafák másolása, hogy a motor olvasni tudja őket |
| Opcionális SMTP-jelszó e-mail értesítésekhez | Titkosítva tárolódik az eszközön a munkamenet-beállításokban (AES-GCM profilonkénti kulcsfájllal). Frissítéskor a mező megléte esetén az AES-GCM nélkül tárolt régi SMTP-jelszó egyszer átírásra kerül AES-GCM formátumba. Az AES-GCM kulcsfájl az alkalmazás profilmappájában marad, és a bejelentkezett OS-fiók olvashatja; a beállítások JSON alkalmi olvasása ellen véd, nem hardveres trezor. | Csak ha engedélyezed az e-mail értesítéseket és megadod az SMTP-hitelesítő adatokat |

## Amit a kiadó alapértelmezés szerint nem kap meg

- Fájltartalom rendezési/javítási futásokból  
- Névjegyek, hely, mikrofon vagy kamera (nem használt)  
- Analitikai vagy hirdetési adatok (az alkalmazás nem tartalmaz ilyen SDK-t)  
- A helyben tárolt SMTP-jelszavak (az eszközén maradnak, hacsak nem küld levelet a saját SMTP-kiszolgálóján keresztül)

## Opcionális hálózati használat

| Tevékenység | Adatok elküldve | Címzett |
|----------|-----------|------------|
| Opcionális frissítés-ellenőrzés | HTTPS ELJÁRÁS a verziójegyzékhez. A gazdagép (például a GitHub) megkapja a kérés IP-címét, az „OrganizeFiles-UpdateCheck/1.0” felhasználói ügynököt és a TLS metaadatokat. A rendszer nem küldi el a fájl elérési útját vagy tartalmát. Letiltása a következővel: `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1'. | A JSON-jegyzéket kiszolgáló gazdagép |
| Bolti vásárlás / licenc | Platformszámlázási API-k | Microsoft, Google vagy Apple (csatornánként) |
| Opcionális licencszerver (üzemeltető által konfigurált) | A rendszer egy véletlenszerű állandó telepítési azonosítót (a `license_installation_id.txt' fájlban tárolt GUID) elküld a kiadó által üzemeltetett vagy üzemeltető által konfigurált licencszervernek a `ORGANIZE_FILES_LICENSE_SERVER_URL' címen. A telepítési azonosító egy eszközazonosító a GDPR 30. preambulumbekezdése szerint. Jogalap: szerződés teljesítése. Kiadói megőrzés: jogosultsági nyilvántartások az aktív időszak alatt, plusz legfeljebb 24 hónap lejárat/visszavonás után a visszaélések megelőzése és viták kezelése céljából; számviteli nyilvántartások legfeljebb 7 évig őrizhetők, ha a törvény előírja. Az üzemeltető által futtatott szerverek az üzemeltető dokumentált megőrzési ütemtervét követik. Ez a funkció inaktív, hacsak nincs beállítva a `ORGANIZE_FILES_LICENSE_SERVER_URL'. | Kiadói vagy üzemeltetői licencszerver |
| Opcionális OpenTelemetry nyomkövetés (operátor által konfigurált) | Ha az `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT' be van állítva, az automatizálási feladatok metaadatai (feladatazonosítók, korrelációs azonosítók, céltípus-címkék, W3C nyomkövetési kontextus) exportálódnak a konfigurált OTLP-gyűjtőbe. Nem tartalmaz fájl elérési utat vagy fájltartalmat. Ez a funkció alapértelmezés szerint inaktív, és kifejezett kezelői konfigurációt igényel. | Kezelő által konfigurált OTLP gyűjtő |
| Opcionális e-mail értesítések (ha engedélyezve) | Futási állapot és naplórészletek (tartalmazhatnak fájlútvonalakat) az üzemeltető által konfigurált SMTP-kiszolgálón keresztül | Üzemeltetői SMTP / levelezőszolgáltató |
| Opcionális automatizálási webhookok (az üzemeltető állítja be) | Ha az `ORGANIZE_FILES_AUTOMATION_WEBHOOK_URL` be van állítva, a feladatok életciklus-eseményei korrelációs azonosítókkal és az automatizálás állapotfájljainak elérési útjaival | Az üzemeltető által beállított webhook-végpont |
| Választható személyazonosság-ellenőrzés a végrehajtás jóváhagyásához (az üzemeltető állítja be) | Ha `ORGANIZE_FILES_APPROVE_OAUTH_JWKS_URL` be van állítva, egy HTTPS GET lekéri az aláírókulcsokat és egy órára gyorsítótárazza őket; token nem hagyja el az eszközt. Ha `ORGANIZE_FILES_APPROVE_OAUTH_INTROSPECTION_URL` van beállítva, magát az üzemeltető bearer tokenjét küldi el a rendszer ellenőrzésre erre a végpontra (RFC 7662), beállítás esetén HTTP Basic ügyfél-hitelesítéssel. Inaktív, amíg egyik URL sincs beállítva. | Az üzemeltető által beállított identitásszolgáltató |
| Motor NAS újrapróbálkozás segítők | A konfigurált hálózati útvonalakon kívül nincs | NAS / SMB gazdagép |

A frissítési ellenőrzések összehasonlítják a **csak a verzió metaadatait**. Az asztali alkalmazás az EULA elfogadása után naponta egyszer futtathatja ezt az ellenőrzést, hacsak nincs letiltva.

## Jogalapok (GDPR-stílusú keretezés, nem jogi tanácsadás)

| Feldolgozás | Tipikus alap |
|------------|-----------------|
| Helyi rendezés/javítás a már kiválasztott mappákon | A szerződés teljesítése / az üzemeltető jogos érdeke |
| Helyi munkamenet-, folytatási és állapotfájlok | Ugyanaz, az eszköz nyújtásához szükséges |
| Bolti számlázás és jogosultság | Szerződés a platformbolttal |
| Opcionális frissítési jegyzékellenőrzés | A biztonsági frissítések iránti jogos érdek; letiltható a | környezeti változón keresztül
| Támogatási e-mail | Jogos érdek / szerződéskötést megelőző lépések az Ön kérésére |

## Nemzetközi átutalások

Az opcionális frissítési ellenőrzések elérhetik az Európai Gazdasági Térségen kívüli szervereket (például a GitHubot az Egyesült Államokban). A bolti számlázás az egyes platformok feltételei szerint történik.

## Felügyeleti hatóság és panaszok

Ha az alkalmazandó jogszabályok az érintettek jogait biztosítják, vagy panaszt tehet a felügyeleti hatóságnál, először lépjen kapcsolatba a kiadóval a **razvan.gutulov@outlook.com** címen. Az EU/EGT lakosai a helyi adatvédelmi hatóságukhoz is panaszt tehetnek (Románia esetében: ANSPDCP, https://www.dataprotection.ro).

## Harmadik féltől származó processzorok (ha ezeket a szolgáltatásokat használják)

- **Microsoft Store / Google Play / Mac App Store** – számlázás és jogosultság. A Google Play az eszközön ellenőrzi a vásárlásokat.
- **GitHub (vagy a jegyzékbe foglalt gazdagép)** – opcionális JSON-verzió HTTPS-en keresztül (a kiszolgálónaplókban szerepelhet az ügyfél IP-címe)
- **E-mail kliens** – amikor a mailto linken keresztül lép kapcsolatba az ügyfélszolgálattal

## Üzemeltetői kötelezettségek (GDPR-stílusú keretezés)

Személyes adatok lehetnek **a fájlokban**. Ha ilyen adatokat dolgoz fel, Ön (vagy szervezete) **adatkezelő** lehet, és meg kell választania a törvényes alapot, minimálisra kell csökkentenie a megőrzést, és válaszolnia kell az érintettek kérésére.

## Megőrzés

A helyi fájlok mindaddig megmaradnak, amíg nem törli őket, törli az alkalmazásadatokat, eltávolítja az alkalmazást, vagy felülírja a kimeneti mappákat. A kiadó nem működtet központi megőrzési ütemtervet a csak helyi adatokhoz.
A kiadó által tárolt adatokra:

- Támogatási e-mail és levelezés: az utolsó érdemi kapcsolatfelvételtől számított legfeljebb 24 hónapig, kivéve ha vita vagy jogi kötelezettség hosszabb megőrzést igényel.
- Közvetlen vásárlási, visszatérítési, adó- és könyvelési adatok: legfeljebb 7 évig, ahol ezt adó- vagy számviteli jog előírja.
- Kiadó által működtetett licenckiszolgáló jogosultsági adatai: a jogosultság aktív ideje alatt, majd lejárat vagy visszavonás után legfeljebb 24 hónapig.
- Kiadó által működtetett kiszolgáló hozzáférési és biztonsági naplói: legfeljebb 90 napig, kivéve ha biztonsági vizsgálat, csalásmegelőzés vagy jogi igény miatt hosszabb idő szükséges.

## Az Ön jogai

A kiadó birtokában lévő adatokkal kapcsolatban (pl. támogatási e-mailes levelezés) forduljon a **razvan.gutulov@outlook.com** címhez. A csak az eszközén tárolt adatok esetében törölheti a legtöbb alkalmazásadatot az **Alkalmazásadatok törlése**, az eltávolítás vagy a fájl manuális törlésével. Az **Alkalmazásadatok törlése** eltávolítja a munkameneteket, a naplókat és az automatizálási vázlatokat, de megtarthatja a licencpróba horgonyokat, a fizetett telepítési jelzőket és az opcionális licencellenőrzésekhez használt névtelen telepítési azonosítót – a folytatás előtt tekintse meg az alkalmazáson belüli megerősítő szöveget. Ahol alkalmazandó, kérheti az adataihoz való hozzáférést, azok helyesbítését vagy törlését, a kezelés korlátozását, tiltakozhat a kezelés ellen, kérheti az adathordozhatóságot, vagy visszavonhatja a hozzájárulását.

A kiadó törekszik arra, hogy az érintetti kérelmekre az ellenőrzött kéréstől számított **30 napon** belül válaszoljon (személyazonosság igazolása kérhető, ha ez ésszerűen szükséges).

## Gyerekek

Általános hatékonyságnövelő eszköz, amely nem 13 éven aluli (vagy az Ön joghatóságában előírt életkor alatti) gyermekek számára készült.

## Változások

A lényeges változtatásoknak a megjelenés előtt meg kell jelenniük az áruházi adatlapokon és az alkalmazáson belüli dokumentációban.

## Kapcsolódó dokumentumok

- [EULA (angol)](./eula.md)  
- [Adatvédelmi irányelvek (román)](../ro/privacy-policy.md)  
- [Adatvédelmi irányelvek (német)](../de/privacy-policy.md)  
- [Adatvédelmi irányelvek (francia)](../fr/privacy-policy.md)

---

Ha ez a fordítás hiányos, az angol adatvédelmi szabályzat az irányadó.
