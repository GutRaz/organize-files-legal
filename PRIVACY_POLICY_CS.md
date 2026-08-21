> **Neoficiální strojový překlad – nikoli právní poradenství.** Pokud je tento překlad v rozporu, řídí se [anglická EULA](./EULA_EN.md) a [anglické zásady ochrany osobních údajů](./PRIVACY_POLICY_EN.md). Poraďte se s kvalifikovaným právníkem ve vaší jurisdikci.

---

# Zásady ochrany osobních údajů — Uspořádejte soubory

**Vydavatel:** Guțulov Răzvan Constantin PFA  
**Sídlo:** Str. Republicii nr. 33B, bl. N3, sc. A, et. 1, ap. 3, Breaza de Sus, 105400 Breaza, jud. Prahova, România  
**Obchodní rejstřík:** F2026004513003 (EUID ROONRC.F2026004513003)  
**Daňové identifikační číslo:** 53610310  
**Kontakt:** razvan.gutulov@outlook.com  
**Datum účinnosti:** 28.05.2026  
**Veřejná adresa URL:** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_CS.md`

---

## Shrnutí

Organize Files zpracovává soubory **místně v zařízení**. Obsah souboru se **nenahrává na vlastní servery vydavatele** pro běžné organizování nebo opravy. Aplikace **zapisuje místní soubory** na zařízení (snímky relace, stav obnovení, volitelné protokoly), jak je popsáno níže.

## Data zpracována lokálně

| Údaje | Kde jsou uloženy | Účel |
|------|----------------|---------|
| Soubory a složky, které vyberete | Pouze vaše zařízení | Uspořádat, deduplikovat, opravit, volitelně odstranit |
| Snímek relace uživatelského rozhraní (`last-ui-session.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (počítač) nebo soukromé úložiště aplikace (Android) | Obnovit pracovní prostor: cesty, rozšíření, možnosti |
| Uspořádejte životopis + volitelný deník přesunů | Výstup `_OrganizeMediaLogs` nebo složku relace | Přeskočit dokončené pohyby; metadata pro obnovu (zakódované cesty) |
| Volitelný spouštěcí prezenční signál JSON | Výstup `_OrganizeMediaLogs` | Čítače pokroku pro externí nástroje |
| Zkušební / licenční stav | Složka profilu pod Local App Data | Uplatnit nárok na zkoušku nebo uložit |
| Aktualizace-kontrola stavu | Složka profilu | Kontrola volitelné verze manifestu plynu |
| Android SAF staging | Složka relace pod úložištěm aplikace | Zkopírujte stromy `content://`, aby je engine mohl číst |
| Volitelné heslo SMTP pro e-mailová oznámení | Uloženo šifrovaně v předvolbách relace na zařízení (AES-GCM se souborem klíče pro každý profil). Při upgradu se starší heslo SMTP uložené bez AES-GCM jednorázově přepíše na AES-GCM, pokud je pole přítomné. Soubor klíče AES-GCM zůstává ve složce profilu aplikace a může jej číst přihlášený účet OS; chrání běžné čtení JSON předvoleb, ne hardwarový trezor. | Pouze pokud zapnete e-mailová oznámení a zadáte údaje SMTP |

## Co vydavatel standardně neobdrží

- Obsah souborů z organizování/oprav  
– Kontakty, poloha, mikrofon nebo kamera (nepoužívá se)  
– Analytics SDK sdružené ve stromu s otevřeným zdrojovým kódem  

## Volitelné použití sítě

| Aktivita | Údaje odeslány | Příjemce |
|----------|-----------|-----------|
| Volitelná kontrola aktualizací | HTTPS GET do manifestu verze. Hostitel (například GitHub) obdrží IP adresu požadavku, User-Agent `OrganizeFiles-UpdateCheck/1.0` a metadata TLS. Nejsou odeslány žádné cesty k souboru ani obsah souboru. Zakázat pomocí `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Hostitel obsluhující manifest JSON |
| Nákup v obchodě / licence | Rozhraní API pro fakturaci platformy | Microsoft, Google nebo Apple (za kanál) |
| Volitelný licenční server (nakonfigurovaný operátorem) | Náhodné trvalé ID instalace (GUID uložené v `license_installation_id.txt`) je odesláno na licenční server provozovaný vydavatelem nebo operátorem nakonfigurovaný na `ORGANIZE_FILES_LICENSE_SERVER_URL`. ID instalace je identifikátor zařízení podle bodu odůvodnění 30 GDPR. Právní základ: plnění smlouvy. Uchování u vydavatele: záznamy nároků po dobu aktivního nároku plus až 24 měsíců po skončení/odvolání (prevence zneužití a spory); účetní záznamy mohou být uchovány až 7 let, pokud to vyžaduje zákon. Servery provozované operátorem se řídí operátorovým dokumentovaným plánem uchování. Tato funkce je neaktivní, pokud není nastavena adresa URL `ORGANIZE_FILES_LICENSE_SERVER_URL`. | Licenční server vydavatele nebo provozovatele |
| Volitelné trasování OpenTelemetry (nakonfigurováno operátorem) | Když je nastaveno `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT`, metadata automatizační úlohy (ID úlohy, ID korelace, značky cílového typu, kontext trasování W3C) se exportují do nakonfigurovaného kolektoru OTLP. Nejsou zahrnuty žádné cesty k souboru ani obsah souboru. Tato funkce je ve výchozím nastavení neaktivní a vyžaduje explicitní konfiguraci operátora. | Operátorem konfigurovaný kolektor OTLP |
| Volitelná e-mailová oznámení (pokud jsou povolena) | Stav běhu a výňatky z protokolu (mohou obsahovat cesty k souborům) odesílané přes operátorem nakonfigurovaný SMTP server | Operátorův SMTP / poskytovatel pošty |
| Pomocníci pro opakování NAS motoru | Žádné kromě nakonfigurovaných síťových cest | Hostitel NAS / SMB |

Kontroly aktualizací porovnávají **pouze metadata verze**. Desktopová aplikace může tuto kontrolu spustit jednou denně po přijetí EULA, pokud není zakázána.

## Právní základy (rámování ve stylu GDPR, nikoli právní poradenství)

| Zpracování | Typický základ |
|------------|----------------|
| Místní organizace/oprava již vybraných složek | Plnění smlouvy / oprávněný zájem provozovatele |
| Místní soubory relace, obnovení a srdečního tepu | Totéž – nutné k poskytnutí nástroje |
| Účtování obchodu a nárok | Smlouva s platformou obchod |
| Volitelná kontrola manifestu aktualizace | Oprávněný zájem o aktualizace zabezpečení; lze zakázat pomocí proměnné prostředí |
| E-mail podpory | Oprávněný zájem / předsmluvní kroky na Vaši žádost |

## Mezinárodní převody

Volitelné kontroly aktualizací se mohou dostat na servery mimo Evropský hospodářský prostor (například GitHub ve Spojených státech). Fakturace obchodu se řídí podmínkami každé platformy.

## Dozorčí orgán a stížnosti

Pokud platné zákony udělují práva subjektu údajů nebo stížnost u dozorového úřadu, kontaktujte nejprve vydavatele na **razvan.gutulov@outlook.com**. Obyvatelé EU/EHP mohou také podat stížnost svému místnímu úřadu pro ochranu údajů (pro Rumunsko: ANSPDCP, https://www.dataprotection.ro).

## Procesory třetích stran (při použití těchto funkcí)

- **Microsoft Store / Google Play / Mac App Store** – fakturace a nárok. Google Play používá fakturaci na zařízení; produkční záznamy by měly obsahovat integritu služby Play a/nebo ověření na straně serveru podle zásad společnosti Google.
- **GitHub (nebo hostitel manifestu)** – volitelná verze JSON přes HTTPS (může obsahovat IP klienta v protokolech serveru)
- **E-mailový klient** — při kontaktování podpory prostřednictvím odkazu mailto

## Povinnosti operátora (rámování ve stylu GDPR)

Osobní údaje mohou existovat **uvnitř** vašich souborů. Pokud takové údaje zpracováváte, můžete být vy (nebo vaše organizace) **správcem údajů** a musíte zvolit zákonný základ, minimalizovat uchovávání a reagovat na žádosti subjektů údajů.

## Uchování

Místní soubory zůstanou, dokud je neodstraníte, nevymažete data aplikace, neodinstalujete aplikaci nebo nepřepíšete výstupní složky. Vydavatel neprovozuje centrální plán uchovávání pouze pro místní data.

Pro údaje držené vydavatelem:

- E-mail podpory a korespondence: až 24 měsíců po posledním významném kontaktu, pokud spor nebo právní povinnost nevyžaduje delší uchování.
- Záznamy o přímých nákupech, refundacích, daních a účetnictví: až 7 let, pokud to vyžaduje daňové nebo účetní právo.
- Záznamy nároků na licenčním serveru provozovaném vydavatelem: po dobu aktivního nároku plus až 24 měsíců po skončení nebo odvolání.
- Přístupové a bezpečnostní logy na serveru provozovaném vydavatelem: až 90 dnů, pokud nejsou déle potřeba pro bezpečnostní šetření, prevenci podvodů nebo právní nároky.


## Vaše práva

Údaje, které má vydavatel k dispozici (např. e-mailová korespondence podpory), získáte na **razvan.gutulov@outlook.com**. U dat uložených pouze ve vašem zařízení můžete většinu dat aplikací smazat pomocí **Vymazat data aplikace**, odinstalovat nebo ručně odstranit soubor. **Vymazat data aplikace** odstraní relace, protokoly a koncepty automatizace, ale může si ponechat kotvy zkušebních licencí, značky placených instalací aí identifikátor instalace používaný pro volitelné kontroly licencí – než budete pokračovat, přečtěte si text potvrzení v aplikaci.

## Děti

Obecný nástroj produktivity není zaměřen na děti mladší 13 let (nebo věk požadovaný ve vaší jurisdikci).

## Změny

Podstatné změny by se měly objevit v záznamech obchodu a dokumentaci v aplikaci před vydáním.

## Související dokumenty

- [EULA (anglicky)] (./EULA_CS.md)  
- [Zásady ochrany osobních údajů (rumunština)](./PRIVACY_POLICY_RO.md)  
- [Zásady ochrany osobních údajů (němčina)](./PRIVACY_POLICY_DE.md)  
- [Zásady ochrany osobních údajů (francouzština)](./PRIVACY_POLICY_FR.md)

---

Pokud je tento překlad neúplný, řídí se znění anglickými Zásadami ochrany osobních údajů.

## Správce a kontakt

Pro osobní údaje zpracovávané vydavatelem je správcem **Guțulov Răzvan Constantin PFA**. Kontakt: **razvan.gutulov@outlook.com**.

## Uchovávání (záznamy vydavatele)

Pro údaje držené vydavatelem:

- E-mail podpory a korespondence: až 24 měsíců po posledním významném kontaktu, pokud spor nebo právní povinnost nevyžaduje delší uchování.
- Záznamy o přímých nákupech, refundacích, daních a účetnictví: až 7 let, pokud to vyžaduje daňové nebo účetní právo.
- Záznamy nároků na licenčním serveru provozovaném vydavatelem: po dobu aktivního nároku plus až 24 měsíců po skončení nebo odvolání.
- Přístupové a bezpečnostní logy na serveru provozovaném vydavatelem: až 90 dnů, pokud nejsou déle potřeba pro bezpečnostní šetření, prevenci podvodů nebo právní nároky.

## Vaše práva (lhůta odpovědi)

Vydavatel se snaží odpovědět na žádosti subjektů údajů do **30 dnů** od ověřené žádosti (ověření totožnosti může být požadováno, když je to přiměřeně nutné).
