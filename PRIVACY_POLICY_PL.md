> **Nieoficjalne tłumaczenie maszynowe — nie jest to porada prawna.** Jeśli tłumaczenie jest z nimi sprzeczne, obowiązują [Angielska umowa EULA](./EULA_EN.md) i [Angielska polityka prywatności](./PRIVACY_POLICY_EN.md). Skonsultuj się z wykwalifikowanym doradcą w swojej jurysdykcji.

---

# Polityka prywatności — Organizuj pliki

**Wydawca:** Guțulov Răzvan Constantin PFA  
**Adres rejestrowy:** Str. Republicii nr. 33B, bl. N3, sc. A, et. 1, ap. 3, Breaza de Sus, 105400 Breaza, jud. Prahova, România  
**Rejestr handlowy:** F2026004513003 (EUID ROONRC.F2026004513003)  
**Numer identyfikacji podatkowej:** 53610310  
**Kontakt:** razvan.gutulov@outlook.com  
**Data wejścia w życie:** 28.05.2026 r  
**Publiczny adres URL:** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_PL.md`

---

## Podsumowanie

Organize Files przetwarza pliki **lokalnie na urządzeniu**. Zawartość plików **nie jest przesyłana na własne serwery wydawcy** w celu normalnych operacji porządkowania lub naprawy. Aplikacja **zapisuje pliki lokalne** na urządzeniu (migawki sesji, stan wznowienia, opcjonalne dzienniki), jak opisano poniżej.

## Dane przetwarzane lokalnie

| Dane | Gdzie przechowywane | Cel |
|------|----------------|------------|
| Wybrane pliki i foldery | Tylko Twoje urządzenie | Organizuj, deduplikuj, naprawiaj, opcjonalnie usuwaj |
| Migawka sesji interfejsu użytkownika (`last-ui-session.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (komputer stacjonarny) lub prywatna pamięć aplikacji (Android) | Przywróć obszar roboczy: ścieżki, rozszerzenia, opcje |
| Zorganizuj CV + opcjonalnie przenieś dziennik | Wyprowadź `_OrganizeMediaLogs` lub folder sesji | Pomiń ukończone ruchy; metadane odzyskiwania (ścieżki zakodowane) |
| Opcjonalne uruchomienie pulsu JSON | Wyjście `_OrganizeMediaLogs` | Liczniki postępu dla narzędzi zewnętrznych |
| Stan wersji próbnej/licencyjnej | Folder profilu w obszarze Dane aplikacji lokalnej | Egzekwuj uprawnienia do wersji próbnej lub przechowywania |
| Stan sprawdzenia aktualizacji | Folder profilu | Kontrola manifestu wersji opcjonalnej przepustnicy |
| Inscenizacja Androida SAF | Folder sesji w magazynie aplikacji | Skopiuj drzewa `content://`, aby silnik mógł je odczytać |
| Opcjonalne hasło SMTP do powiadomień e-mail | Przechowywane na urządzeniu w preferencjach sesji w postaci zaszyfrowanej (AES-GCM z plikiem klucza dla profilu). Podczas aktualizacji, jeśli pole istnieje, starsze hasło SMTP zapisane bez AES-GCM jest jednorazowo przepisywane do AES-GCM. Plik klucza AES-GCM pozostaje w folderze profilu aplikacji i może być odczytany przez zalogowane konto użytkownika OS; chroni przed przypadkowym odczytem JSON preferencji, nie jest sejfem sprzętowym. | Tylko jeśli włączysz powiadomienia e-mail i wpiszesz dane SMTP |

## Czego wydawca domyślnie nie otrzymuje

- Zawartość plików z przebiegów porządkowania/naprawy  
- Kontakty, lokalizacja, mikrofon lub kamera (nieużywane)  
- Zestawy SDK Analytics zawarte w drzewie open source  

## Opcjonalne korzystanie z sieci

| Aktywność | Dane przesłane | Odbiorca |
|---------|-----------|----------|
| Opcjonalna kontrola aktualizacji | HTTPS GET do manifestu wersji. Host (na przykład GitHub) otrzymuje adres IP żądania, agenta użytkownika „OrganizeFiles-UpdateCheck/1.0” i metadane TLS. Nie są wysyłane żadne ścieżki plików ani zawartość plików. Wyłącz za pomocą `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Host obsługujący manifest JSON |
| Zakup w sklepie / licencja | Interfejsy API rozliczeń platformy | Microsoft, Google lub Apple (na kanał) |
| Opcjonalny serwer licencji (skonfigurowany przez operatora) | Losowy identyfikator trwałej instalacji (GUID przechowywany w pliku `license_installation_id.txt`) jest wysyłany do obsługiwanego przez wydawcę lub skonfigurowanego przez operatora serwera licencji pod adresem `ORGANIZE_FILES_LICENSE_SERVER_URL`. Identyfikator instalacji jest identyfikatorem urządzenia w rozumieniu punktu 30 preambuły RODO. Podstawa prawna: wykonanie umowy. Retencja po stronie wydawcy: rejestry uprawnień w okresie aktywności plus do 24 miesięcy po wygaśnięciu/odwołaniu (zapobieganie nadużyciom i spory); rejestry księgowe mogą być przechowywane do 7 lat, gdy wymaga tego prawo. Serwery prowadzone przez operatora stosują udokumentowany harmonogram retencji operatora. Ta funkcja jest nieaktywna, chyba że ustawiono „ORGANIZE_FILES_LICENSE_SERVER_URL”. | Serwer licencji wydawcy lub operatora |
| Opcjonalne śledzenie OpenTelemetry (skonfigurowane przez operatora) | Gdy ustawiona jest opcja `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT`, metadane zadania automatyzacji (identyfikatory zadań, identyfikatory korelacji, znaczniki typu docelowego, kontekst śledzenia W3C) są eksportowane do skonfigurowanego modułu zbierającego OTLP. Nie są uwzględniane żadne ścieżki plików ani zawartość plików. Ta funkcja jest domyślnie nieaktywna i wymaga jawnej konfiguracji operatora. | Kolektor OTLP konfigurowany przez operatora |
| Opcjonalne powiadomienia e-mail (gdy włączone) | Status uruchomienia i fragmenty dziennika (mogą zawierać ścieżki plików) wysyłane przez skonfigurowany przez operatora serwer SMTP | SMTP operatora / dostawca poczty |
| Opcjonalne webhooki automatyzacji (konfigurowane przez operatora) | Gdy ustawiono `ORGANIZE_FILES_AUTOMATION_WEBHOOK_URL`, zdarzenia cyklu życia zadań z identyfikatorami korelacji i ścieżkami plików stanu automatyzacji | Punkt końcowy webhooka skonfigurowany przez operatora |
| Pomocnicy ponownej próby silnika NAS | Brak poza skonfigurowanymi ścieżkami sieciowymi | Host NAS/SMB |

Kontrole aktualizacji porównują **tylko metadane wersji**. Aplikacja komputerowa może przeprowadzać tę kontrolę raz dziennie po zaakceptowaniu umowy EULA, chyba że jest wyłączona.

## Podstawa prawna (ramki w stylu RODO, a nie porada prawna)

| Przetwarzanie | Typowa podstawa |
|------------|----------------|
| Lokalne organizowanie/naprawa w już wybranych folderach | Wykonanie umowy / prawnie uzasadniony interes operatora |
| Sesja lokalna, CV i pliki pulsu | To samo — konieczne do zapewnienia narzędzia |
| Rozliczenia i uprawnienia w sklepie | Umowa ze sklepem platformowym |
| Opcjonalne sprawdzenie manifestu aktualizacji | Uzasadnione zainteresowanie aktualizacjami zabezpieczeń; można wyłączyć za pomocą zmiennej środowiskowej |
| E-mail pomocy technicznej | Uzasadniony interes / kroki przedumowne na Twoją prośbę |

## Przelewy międzynarodowe

Opcjonalne kontrole aktualizacji mogą dotrzeć do serwerów poza Europejskim Obszarem Gospodarczym (na przykład GitHub w Stanach Zjednoczonych). Rozliczenia w sklepie podlegają warunkom każdej platformy.

## Organ nadzorczy i skargi

Jeśli obowiązujące prawo przyznaje podmiotowi danych prawa lub skargę do organu nadzorczego, należy najpierw skontaktować się z wydawcą pod adresem **razvan.gutulov@outlook.com**. Mieszkańcy UE/EOG mogą również złożyć skargę do lokalnego organu ochrony danych (w przypadku Rumunii: ANSPDCP, https://www.dataprotection.ro).

## Procesory innych firm (jeśli używane są te funkcje)

- **Microsoft Store / Google Play / Mac App Store** — rozliczenia i uprawnienia. Google Play korzysta z rozliczeń na urządzeniu; wykazy produkcji powinny uwzględniać integralność Play i/lub weryfikację po stronie serwera zgodnie z zasadami Google.
- **GitHub (lub host manifestu)** — opcjonalna wersja JSON przez HTTPS (może zawierać adres IP klienta w logach serwera)
- **Klient poczty e-mail** — w przypadku kontaktu z pomocą techniczną za pośrednictwem łącza mailto

## Obowiązki operatora (ramki w stylu RODO)

Dane osobowe mogą znajdować się **wewnątrz** Twoich plików. Jeśli przetwarzasz takie dane, Ty (lub Twoja organizacja) możecie być **administratorem danych** i musicie wybrać podstawę prawną, zminimalizować przechowywanie i odpowiadać na żądania osób, których dane dotyczą.

## Zatrzymanie

Pliki lokalne pozostają do czasu ich usunięcia, wyczyszczenia danych aplikacji, odinstalowania aplikacji lub nadpisania folderów wyjściowych. Wydawca nie stosuje centralnego harmonogramu przechowywania danych wyłącznie lokalnych.

W przypadku danych przechowywanych przez wydawcę:

- E-mail wsparcia i korespondencja: do 24 miesięcy po ostatnim istotnym kontakcie, chyba że spór lub obowiązek prawny wymaga dłuższego przechowywania.
- Rejestry bezpośrednich zakupów, zwrotów, podatków i księgowości: do 7 lat, gdy wymaga tego prawo podatkowe lub rachunkowe.
- Rejestry uprawnień na serwerze licencji prowadzonym przez wydawcę: w okresie aktywności plus do 24 miesięcy po wygaśnięciu lub odwołaniu.
- Logi dostępu i bezpieczeństwa na serwerze obsługiwanym przez wydawcę: do 90 dni, chyba że dłuższy okres jest potrzebny do dochodzenia bezpieczeństwa, zapobiegania oszustwom lub roszczeń prawnych.

## Twoje prawa

W sprawie danych posiadanych przez wydawcę (np. korespondencji e-mailowej) prosimy o kontakt pod adresem **razvan.gutulov@outlook.com**. W przypadku danych przechowywanych tylko na Twoim urządzeniu możesz usunąć większość danych aplikacji, korzystając z opcji **Wyczyść dane aplikacji**, odinstalowania lub ręcznego usunięcia plików. **Wyczyść dane aplikacji** usuwa sesje, dzienniki i wersje robocze automatyzacji, ale może zachować kotwice wersji próbnej licencji, znaczniki płatnej instalacji i identyfikator instalacji używany do opcjonalnego sprawdzania licencji — zanim przejdziesz dalej, zobacz tekst potwierdzenia w aplikacji.

## Dzieci

Ogólne narzędzie zwiększające produktywność, nie skierowane do dzieci poniżej 13 roku życia (lub wieku wymaganego w Twojej jurysdykcji).

## Zmiany

Istotne zmiany powinny pojawić się w informacjach o sklepie i dokumentacji w aplikacji przed publikacją.

## Powiązane dokumenty

- [EULA (angielski)](./EULA_EN.md)  
- [Polityka prywatności (rumuński)](./PRIVACY_POLICY_RO.md)  
- [Polityka prywatności (niemiecki)](./PRIVACY_POLICY_DE.md)  
- [Polityka prywatności (francuski)](./PRIVACY_POLICY_FR.md)

---

Jeżeli to tłumaczenie jest niekompletne, obowiązuje angielska Polityka prywatności.

## Administrator i kontakt

Administratorem danych osobowych przetwarzanych przez wydawcę jest **Guțulov Răzvan Constantin PFA**. Kontakt: **razvan.gutulov@outlook.com**.

## Przechowywanie (rejestry wydawcy)

Dla danych przechowywanych przez wydawcę:

- E-mail pomocy technicznej i korespondencja: do 24 miesięcy po ostatnim istotnym kontakcie, chyba że spór lub obowiązek prawny wymaga dłuższego przechowywania.
- Rejestry zakupów bezpośrednich, zwrotów, podatków i księgowości: do 7 lat, gdy wymaga tego prawo podatkowe lub rachunkowe.
- Rejestry uprawnień na serwerze licencji obsługiwanym przez wydawcę: przez okres aktywnego uprawnienia oraz do 24 miesięcy po wygaśnięciu lub cofnięciu.
- Logi dostępu i bezpieczeństwa na serwerze obsługiwanym przez wydawcę: do 90 dni, chyba że dłuższy okres jest potrzebny do dochodzenia bezpieczeństwa, zapobiegania oszustwom lub roszczeń prawnych.

## Twoje prawa (czas odpowiedzi)

Wydawca dąży do odpowiedzi na żądania osób, których dane dotyczą, w ciągu **30 dni** od zweryfikowanego żądania (weryfikacja tożsamości może być wymagana, gdy jest rozsądnie potrzebna).
