> **Kolaylık sağlamak amacıyla sunulan çeviri.** Referans sürümler [İngilizce EULA](../en/eula.md) ve [İngilizce Gizlilik Politikası](../en/privacy-policy.md)'dır. Ülkenizdeki emredici tüketici hukuku kendi dilinizdeki sürüme öncelik veriyorsa o sürüm uygulanır. Yasal tavsiye değildir — kendi yargı çevrenizde nitelikli bir avukata danışın.

---

# Gizlilik Politikası — Organize Files

**Yayıncı:** Guțulov Răzvan Constantin PFA  
**Kayıtlı adres:** Str. Republicii nr. 33B, bl. N3, sc. A, et. 1, ap. 3, Breaza de Sus, 105400 Breaza, jud. Prahova, România  
**Ticaret sicili:** F2026004513003 (EUID ROONRC.F2026004513003)  
**Vergi kimlik numarası:** 53610310  
**İletişim:** razvan.gutulov@outlook.com  
**Geçerlilik tarihi:** 2026-05-28  
**Genel URL:** `https://github.com/GutRaz/organize-files-legal/blob/main/tr/privacy-policy.md`

---

## Özet

Organize Files, dosyaları **cihazda yerel olarak** işler. Dosya içerikleri normal düzenleme veya onarım işlemleri için **yayıncının kendi sunucularına yüklenmez**. Uygulama, aşağıda açıklandığı gibi cihaza **yerel dosyalar** yazar (oturum anlık görüntüleri, devam etme durumu, isteğe bağlı günlükler).

## Veri sorumlusu ve iletişim

Yayıncı tarafından işlenen kişisel veriler için veri sorumlusu **Guțulov Răzvan Constantin PFA**'dur. İletişim: **razvan.gutulov@outlook.com**.

## Veriler yerel olarak işlendi

| Veri | Nerede saklanıyor | Amaç |
|----------|-----|-----------|
| Seçtiğiniz dosya ve klasörler | Yalnızca cihazınızda | Düzenleme, yinelenenleri bulma, onarma ve seçildiğinde silme |
| Kullanıcı arayüzü oturumu anlık görüntüsü (`last-ui-session.json`) | Uygulama profil klasöründeki `sessions\<id>\` klasörü: Windows'ta `%LocalAppData%\OrganizeFilesCrossPlatform`, macOS'ta `~/Library/Application Support/OrganizeFilesCrossPlatform`, Linux'ta `~/.local/share/OrganizeFilesCrossPlatform` veya Android ve iOS'ta uygulamaya özel depolama | Çalışma alanını geri yükleyin: yollar, uzantılar, seçenekler |
| Bir düzenleme çalıştırmasının devam durumu + isteğe bağlı taşıma günlüğü | Çıktı klasöründe `_OrganizeMediaLogs` veya oturum klasörü | Önceden yapılmış taşımaları atlama, yolları kodlanmış kurtarma bilgileri |
| Bir çalıştırmanın isteğe bağlı ilerleme dosyası, JSON | Çıktı klasöründe `_OrganizeMediaLogs` | Diğer programlar için ilerleme sayaçları |
| Deneme ve lisans durumu | Uygulamanın profil klasörü | Deneme süresini veya mağaza satın alımını uygulama |
| Güncelleme denetimi durumu | Uygulamanın profil klasörü | İsteğe bağlı sürüm denetiminin ne sıklıkla çalıştığını sınırlama |
| Android: sistem seçicisi SAF ile seçilen klasörlerin kopyaları | Uygulama depolamasındaki oturum klasörü | Motorun okuyabilmesi için `content://` klasör ağaçlarını kopyalar |
| E-posta bildirimleri için isteğe bağlı SMTP parolası | Cihazdaki oturum tercihlerinde şifreli saklanır (profil başına anahtar dosyasıyla AES-GCM). Yükseltmede alan varsa, AES-GCM olmadan saklanmış eski SMTP parolası bir kez AES-GCM olarak yeniden yazılır. AES-GCM anahtar dosyası uygulama profil klasöründe kalır ve oturum açmış OS kullanıcı hesabı tarafından okunabilir; tercih JSON dosyasının gündelik okunmasına karşı korur, donanım kasası değildir. | Yalnızca e-posta bildirimleri etkinleştirilip SMTP bilgileri girilirse |

## Yayıncının varsayılan olarak almadığı şey

- Düzenleme/onarım çalıştırmalarından dosya içerikleri  
- Kişiler, konum, mikrofon veya kamera (kullanılmıyor)  
- Analiz veya reklam verileri (uygulamada bu tür bir SDK bulunmaz)  
- Yerel olarak sakladığınız SMTP parolaları (kendi SMTP sunucunuz üzerinden posta göndermediğiniz sürece cihazınızda kalır)

## İsteğe bağlı ağ kullanımı

| Etkinlik | Veri gönderildi | Alıcı |
|----------|---------------|-----------|
| İsteğe bağlı güncelleme kontrolü | HTTPS GET'i bir sürüm bildirimine aktarın. Ana bilgisayar (örneğin GitHub) istek IP adresini, Kullanıcı Aracısı 'OrganizeFiles-UpdateCheck/1.0' ve TLS meta verilerini alır. Hiçbir dosya yolu veya dosya içeriği gönderilmez. 'ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1' ile devre dışı bırakın. | JSON bildirimini sunan ana makine |
| Mağaza satın alma / lisanslama | Platform faturalandırma API'leri | Microsoft, Google veya Apple (kanal başına) |
| İsteğe bağlı lisans sunucusu (operatör tarafından yapılandırılmış) | Rastgele bir kalıcı kurulum kimliği ('license_installation_id.txt'de saklanan GUID), 'ORGANIZE_FILES_LICENSE_SERVER_URL' adresindeki yayıncı tarafından işletilen veya operatör tarafından yapılandırılan bir lisans sunucusuna gönderilir. Kurulum kimliği, GDPR Beyannamesi 30 kapsamında bir cihaz tanımlayıcısıdır. Yasal dayanak: sözleşmenin yerine getirilmesi. Yayıncı tarafından işletilen saklama: hak kayıtları aktifken artı sona erme/iptalden sonra en fazla 24 ay (kötüye kullanım önleme ve uyuşmazlık); muhasebe kayıtları yasanın gerektirdiği yerde en fazla 7 yıl saklanabilir. Operatörün işlettiği sunucular operatörün belgelenmiş saklama takvimini izler. Bu özellik, `ORGANIZE_FILES_LICENSE_SERVER_URL` ayarlanmadığı sürece etkin değildir. | Yayıncı veya operatör lisans sunucusu |
| İsteğe bağlı OpenTelemetry izleme (operatör tarafından yapılandırılmış) | `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT` ayarlandığında, otomasyon işi meta verileri (iş kimlikleri, korelasyon kimlikleri, hedef türü etiketleri, W3C izleme bağlamı) yapılandırılmış OTLP toplayıcıya aktarılır. Hiçbir dosya yolu veya dosya içeriği dahil edilmemiştir. Bu özellik varsayılan olarak etkin değildir ve açık operatör yapılandırması gerektirir. | Operatör tarafından yapılandırılan OTLP toplayıcı |
| İsteğe bağlı e-posta bildirimleri (etkinleştirildiğinde) | Çalışma durumu ve günlük alıntıları (dosya yolları içerebilir) operatör tarafından yapılandırılmış SMTP sunucusu üzerinden gönderilir | Operatör SMTP / e-posta sağlayıcısı |
| İsteğe bağlı otomasyon web kancaları (operatör tarafından yapılandırılır) | `ORGANIZE_FILES_AUTOMATION_WEBHOOK_URL` ayarlandığında, ilişkilendirme kimlikleri ve otomasyon durum dosyalarının dosya yollarını taşıyan iş yaşam döngüsü olayları | Operatör tarafından yapılandırılan web kancası uç noktası |
| Yürütme onayı için isteğe bağlı kimlik denetimi (işletmen tarafından yapılandırılır) | `ORGANIZE_FILES_APPROVE_OAUTH_JWKS_URL` ayarlıysa bir HTTPS GET imzalama anahtarlarını alır ve bir saat önbelleğe koyar; cihazdan hiçbir belirteç çıkmaz. `ORGANIZE_FILES_APPROVE_OAUTH_INTROSPECTION_URL` ayarlıysa işletmenin taşıyıcı belirtecinin kendisi doğrulama için o uç noktaya gönderilir (RFC 7662), yapılandırılmışsa HTTP Basic istemci kimlik bilgileriyle birlikte. Bu adreslerden biri ayarlanmadıkça etkin değildir. | İşletmenin yapılandırdığı kimlik sağlayıcı |
| Motor NAS yeniden deneme yardımcıları | Yapılandırılmış ağ yollarının ötesinde yok | NAS / KOBİ ana bilgisayarı |

Güncelleme kontrolleri **yalnızca sürüm meta verilerini** karşılaştırır. Masaüstü uygulaması, devre dışı bırakılmadığı sürece EULA'nın kabul edilmesinden sonra bu kontrolü günde bir kez çalıştırabilir.

## Yasal dayanaklar (GDPR tarzı çerçeveleme, hukuki tavsiye değil)

| İşleme | Tipik temel |
|---------------|----------------|
| Zaten seçilmiş olan klasörlerde yerel düzenleme/onarım | Sözleşmenin ifası / operatörün meşru menfaati |
| Yerel oturum, devam ve ilerleme dosyaları | Aynı, aracın sunulması için gerekli |
| Mağaza faturalandırması ve yetkilendirme | Platform mağazasıyla sözleşme |
| İsteğe bağlı güncelleme bildirimi kontrolü | Güvenlik güncellemelerine ilişkin meşru menfaat; ortam değişkeni aracılığıyla devre dışı bırakılabilir |
| Destek e-postası | İsteğiniz üzerine meşru menfaat / sözleşme öncesi adımlar |

## Uluslararası transferler

İsteğe bağlı güncelleme kontrolleri, Avrupa Ekonomik Alanı dışındaki sunuculara (örneğin, Amerika Birleşik Devletleri'ndeki GitHub) ulaşabilir. Mağaza faturalandırması her platformun şartlarına göre gerçekleştirilir.

## Denetleyici makam ve şikayetler

Geçerli yasa, veri sahibine haklar veriyorsa veya bir denetleyici makama şikayette bulunuluyorsa, öncelikle **razvan.gutulov@outlook.com** adresinden yayıncıyla iletişime geçin. AB/AEA'da ikamet edenler ayrıca yerel veri koruma makamlarına da şikayette bulunabilirler (Romanya için: ANSPDCP, https://www.dataprotection.ro).

## Üçüncü taraf işlemciler (bu özellikler kullanıldığında)

- **Microsoft Store / Google Play / Mac App Store** — faturalandırma ve yetkilendirme. Google Play, satın alma işlemlerini cihazda doğrular.
- **GitHub (veya bildirim ana bilgisayarı)** — HTTPS üzerinden isteğe bağlı JSON sürümü (sunucu günlüklerine istemci IP'sini içerebilir)
- **E-posta istemcisi** — mailto bağlantısı aracılığıyla destek ekibiyle iletişime geçtiğinizde

## Operatörün sorumlulukları (GDPR tarzı çerçeveleme)

Dosyalarınızın **içinde** kişisel veriler bulunabilir. Bu tür verileri işlerseniz siz (veya kuruluşunuz) **veri denetleyicisi** olabilirsiniz ve yasal bir temel seçmeli, saklamayı en aza indirmeli ve veri sahibinin taleplerine yanıt vermelisiniz.

## Saklama

Yerel dosyalar siz onları silene, uygulama verilerini temizleyene, uygulamayı kaldırana veya çıktı klasörlerinin üzerine yazana kadar kalır. Yayıncı, yalnızca yerel veriler için merkezi bir saklama planı uygulamaz.

Yayıncının tuttuğu veriler için:

- Destek e-postası ve yazışmalar: son anlamlı temastan sonra en fazla 24 ay; bir uyuşmazlık veya yasal yükümlülük daha uzun saklama gerektirmedikçe.
- Doğrudan satın alma, iade, vergi ve muhasebe kayıtları: vergi veya muhasebe hukuku gerektirdiğinde en fazla 7 yıl.
- Yayıncı tarafından işletilen lisans sunucusu hak kayıtları: hak aktif olduğu sürece ve sona erme veya iptalden sonra en fazla 24 ay.
- Yayıncı tarafından işletilen sunucu erişim/güvenlik günlükleri: güvenlik incelemesi, dolandırıcılık önleme veya hukuki talepler için daha uzun süre gerekmedikçe en fazla 90 gün.

## Haklarınız

Yayıncının elinde bulunan veriler için (ör. destek e-posta yazışmaları) **razvan.gutulov@outlook.com** ile iletişime geçin. Yalnızca cihazınızda depolanan veriler için, uygulama verilerinin çoğunu **Uygulama verilerini temizle**, yüklemeyi kaldır veya manuel dosya silme yoluyla silebilirsiniz. **Uygulama verilerini temizle** oturumları, günlükleri ve otomasyon taslaklarını kaldırır ancak lisans deneme bağlantılarını, ücretli yükleme işaretlerini ve isteğe bağlı lisans kontrolleri için kullanılan bir kurulum tanımlayıcıyı koruyabilir; devam etmeden önce uygulama içi onay metnine bakın. Uygulanabilir olduğu ölçüde erişim, düzeltme, silme, işlemenin kısıtlanması, işlemeye itiraz ve veri taşınabilirliği talep edebilir veya rızanızı geri çekebilirsiniz.

Yayıncı, doğrulanmış bir talepten sonra veri sahibi taleplerine **30 gün** içinde yanıt vermeyi hedefler (makul ölçüde gerekli olduğunda kimlik doğrulaması istenebilir).

## Çocuklar

13 yaşın (veya bölgenizde gerekli olan yaşın) altındaki çocuklara yönelik olmayan genel üretkenlik aracı.

## Değişiklikler

Önemli değişiklikler, yayınlanmadan önce mağaza listelerinde ve uygulama içi belgelerde görünmelidir.

## İlgili belgeler

- [EULA (İngilizce)](../en/eula.md)  
- [Gizlilik politikası (Rumence)](../ro/privacy-policy.md)  
- [Gizlilik politikası (Almanca)](../de/privacy-policy.md)  
- [Gizlilik politikası (Fransızca)](../fr/privacy-policy.md)

---

Bu çeviri eksik olduğunda İngilizce Gizlilik Politikası geçerlidir.
