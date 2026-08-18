> **Resmi olmayan makine çevirisi — yasal tavsiye değildir.** Bu çevirinin kendileriyle çelişmesi durumunda [İngilizce EULA](./EULA_EN.md) ve [İngilizce Gizlilik Politikası](./PRIVACY_POLICY_EN.md) geçerlidir. Yetki alanınızdaki nitelikli danışmana danışın.

---

# Gizlilik Politikası — Dosyaları Düzenleyin

**Yayıncı:** Razvan Constantin Gutulov  
**İletişim:** razvan.gutulov@outlook.com  
**Geçerlilik tarihi:** 2026-05-28  
**Genel URL:** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_TR.md`

---

## Özet

Dosyaları Organize Et, dosyaları **cihazda yerel olarak** işler. Dosya içerikleri normal düzenleme veya onarım işlemleri için **yayıncının kendi sunucularına yüklenmez**. Uygulama, aşağıda açıklandığı gibi cihaza **yerel dosyalar** yazar (oturum anlık görüntüleri, devam etme durumu, isteğe bağlı günlükler).

## Veriler yerel olarak işlendi

| Veri | Nerede saklanıyor | Amaç |
|----------|-----|-----------|
| Seçtiğiniz dosya ve klasörler | Yalnızca cihazınız | Organize edin, tekilleştirin, onarın, isteğe bağlı olarak silin |
| Kullanıcı arayüzü oturumu anlık görüntüsü (`last-ui-session.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (masaüstü) veya uygulamaya özel depolama (Android) | Çalışma alanını geri yükleyin: yollar, uzantılar, seçenekler |
| Özgeçmiş + isteğe bağlı taşıma günlüğü düzenleyin | `_OrganizeMediaLogs` veya oturum klasörünün çıktısını alın | Tamamlanan hamleleri atlayın; kurtarma meta verileri (kodlanmış yollar) |
| İsteğe bağlı çalıştırma kalp atışı JSON | Çıktı `_OrganizeMediaLogs` | Harici araçlar için ilerleme sayaçları |
| Deneme / lisans durumu | Yerel Uygulama Verileri altındaki Profil klasörü | Deneme veya mağaza yetkilendirmesini zorunlu kılın |
| Güncelleme-kontrol durumu | Profil klasörü | İsteğe bağlı sürüm manifest kontrollerini kısın |
| Android SAF evreleme | Uygulama depolama alanı altındaki oturum klasörü | Motorun okuyabilmesi için `content://` ağaçlarını kopyalayın |
| E-posta bildirimleri için isteğe bağlı SMTP parolası | Cihazdaki oturum tercihlerinde şifreli saklanır (profil başına anahtar dosyasıyla AES-GCM). Yükseltmede alan varsa, AES-GCM olmadan saklanmış eski SMTP parolası bir kez AES-GCM olarak yeniden yazılır. AES-GCM anahtar dosyası uygulama profil klasöründe kalır ve oturum açmış OS kullanıcı hesabı tarafından okunabilir; tercih JSON dosyasının gündelik okunmasına karşı korur, donanım kasası değildir. | Yalnızca e-posta bildirimleri etkinleştirilip SMTP bilgileri girilirse |

## Yayıncının varsayılan olarak almadığı şey

- Düzenleme/onarım çalıştırmalarından dosya içerikleri  
- Kişiler, konum, mikrofon veya kamera (kullanılmıyor)  
- Açık kaynak ağacında paketlenmiş Analytics SDK'ları  

## İsteğe bağlı ağ kullanımı

| Etkinlik | Veri gönderildi | Alıcı |
|----------|---------------|-----------|
| İsteğe bağlı güncelleme kontrolü | HTTPS GET'i bir sürüm bildirimine aktarın. Ana bilgisayar (örneğin GitHub) istek IP adresini, Kullanıcı Aracısı 'OrganizeFiles-UpdateCheck/1.0' ve TLS meta verilerini alır. Hiçbir dosya yolu veya dosya içeriği gönderilmez. 'ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1' ile devre dışı bırakın. | JSON bildirimini sunan ana makine |
| Mağaza satın alma / lisanslama | Platform faturalandırma API'leri | Microsoft, Google veya Apple (kanal başına) |
| İsteğe bağlı lisans sunucusu (operatör tarafından yapılandırılmış) | Rastgele bir kalıcı kurulum kimliği ('license_installation_id.txt'de saklanan GUID), 'ORGANIZE_FILES_LICENSE_SERVER_URL' adresindeki yayıncı tarafından işletilen veya operatör tarafından yapılandırılan bir lisans sunucusuna gönderilir. Kurulum kimliği, GDPR Beyannamesi 30 kapsamında bir cihaz tanımlayıcısıdır. Yasal dayanak: sözleşmenin yerine getirilmesi. Yayıncı tarafından işletilen saklama: hak kayıtları aktifken artı sona erme/iptalden sonra en fazla 24 ay (kötüye kullanım önleme ve uyuşmazlık); muhasebe kayıtları yasanın gerektirdiği yerde en fazla 7 yıl saklanabilir. Operatörün işlettiği sunucular operatörün belgelenmiş saklama takvimini izler. Bu özellik, `ORGANIZE_FILES_LICENSE_SERVER_URL` ayarlanmadığı sürece etkin değildir. | Yayıncı veya operatör lisans sunucusu |
| İsteğe bağlı OpenTelemetry izleme (operatör tarafından yapılandırılmış) | `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT` ayarlandığında, otomasyon işi meta verileri (iş kimlikleri, korelasyon kimlikleri, hedef türü etiketleri, W3C izleme bağlamı) yapılandırılmış OTLP toplayıcıya aktarılır. Hiçbir dosya yolu veya dosya içeriği dahil edilmemiştir. Bu özellik varsayılan olarak etkin değildir ve açık operatör yapılandırması gerektirir. | Operatör tarafından yapılandırılan OTLP toplayıcı |
| İsteğe bağlı e-posta bildirimleri (etkinleştirildiğinde) | Çalışma durumu ve günlük alıntıları (dosya yolları içerebilir) operatör tarafından yapılandırılmış SMTP sunucusu üzerinden gönderilir | Operatör SMTP / e-posta sağlayıcısı |
| Motor NAS yeniden deneme yardımcıları | Yapılandırılmış ağ yollarının ötesinde yok | NAS / KOBİ ana bilgisayarı |

Güncelleme kontrolleri **yalnızca sürüm meta verilerini** karşılaştırır. Masaüstü uygulaması, devre dışı bırakılmadığı sürece EULA'nın kabul edilmesinden sonra bu kontrolü günde bir kez çalıştırabilir.

## Yasal dayanaklar (GDPR tarzı çerçeveleme, hukuki tavsiye değil)

| İşleme | Tipik temel |
|---------------|----------------|
| Zaten seçilmiş olan klasörlerde yerel düzenleme/onarım | Sözleşmenin ifası / operatörün meşru menfaati |
| Yerel oturum, özgeçmiş ve kalp atışı dosyaları | Aynı — aracı sağlamak için gerekli |
| Mağaza faturalandırması ve yetkilendirme | Platform mağazasıyla sözleşme |
| İsteğe bağlı güncelleme bildirimi kontrolü | Güvenlik güncellemelerine ilişkin meşru menfaat; ortam değişkeni aracılığıyla devre dışı bırakılabilir |
| Destek e-postası | İsteğiniz üzerine meşru menfaat / sözleşme öncesi adımlar |

## Uluslararası transferler

İsteğe bağlı güncelleme kontrolleri, Avrupa Ekonomik Alanı dışındaki sunuculara (örneğin, Amerika Birleşik Devletleri'ndeki GitHub) ulaşabilir. Mağaza faturalandırması her platformun şartlarına göre gerçekleştirilir.

## Denetleyici makam ve şikayetler

Geçerli yasa, veri sahibine haklar veriyorsa veya bir denetleyici makama şikayette bulunuluyorsa, öncelikle **razvan.gutulov@outlook.com** adresinden yayıncıyla iletişime geçin. AB/AEA'da ikamet edenler ayrıca yerel veri koruma makamlarına da şikayette bulunabilirler (Romanya için: ANSPDCP, https://www.dataprotection.ro).

## Üçüncü taraf işlemciler (bu özellikler kullanıldığında)

- **Microsoft Store / Google Play / Mac App Store** — faturalandırma ve yetkilendirme. Google Play, cihazda Faturalandırmayı kullanır; üretim listelerinde Google politikası uyarınca Play Bütünlüğü ve/veya sunucu tarafı doğrulaması bulunmalıdır.
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

Yayıncının elinde bulunan veriler için (ör. destek e-posta yazışmaları) **razvan.gutulov@outlook.com** ile iletişime geçin. Yalnızca cihazınızda depolanan veriler için, uygulama verilerinin çoğunu **Uygulama verilerini temizle**, yüklemeyi kaldır veya manuel dosya silme yoluyla silebilirsiniz. **Uygulama verilerini temizle** oturumları, günlükleri ve otomasyon taslaklarını kaldırır ancak lisans deneme bağlantılarını, ücretli yükleme işaretlerini ve isteğe bağlı lisans kontrolleri için kullanılan anonim bir kurulum tanımlayıcıyı koruyabilir; devam etmeden önce uygulama içi onay metnine bakın.

## Çocuklar

13 yaşın (veya bölgenizde gerekli olan yaşın) altındaki çocuklara yönelik olmayan genel üretkenlik aracı.

## Değişiklikler

Önemli değişiklikler, yayınlanmadan önce mağaza listelerinde ve uygulama içi belgelerde görünmelidir.

## İlgili belgeler

- [EULA (İngilizce)](./EULA_EN.md)  
- [Gizlilik politikası (Rumence)](./PRIVACY_POLICY_RO.md)  
- [Gizlilik politikası (Almanca)](./PRIVACY_POLICY_DE.md)  
- [Gizlilik politikası (Fransızca)](./PRIVACY_POLICY_FR.md)

---

Bu çeviri eksik olduğunda İngilizce Gizlilik Politikası geçerlidir.

## Veri sorumlusu ve iletişim

Yayıncı tarafından işlenen kişisel veriler için veri sorumlusu **Razvan Constantin Gutulov**'dur. İletişim: **razvan.gutulov@outlook.com**.

## Saklama (yayıncı kayıtları)

Yayıncının tuttuğu veriler için:

- Destek e-postası ve yazışmalar: son anlamlı temastan sonra en fazla 24 ay; bir uyuşmazlık veya yasal yükümlülük daha uzun saklama gerektirmedikçe.
- Doğrudan satın alma, iade, vergi ve muhasebe kayıtları: vergi veya muhasebe hukuku gerektirdiğinde en fazla 7 yıl.
- Yayıncı tarafından işletilen lisans sunucusu hak kayıtları: hak aktif olduğu sürece ve sona erme veya iptalden sonra en fazla 24 ay.
- Yayıncı tarafından işletilen sunucu erişim/güvenlik günlükleri: güvenlik incelemesi, dolandırıcılık önleme veya hukuki talepler için daha uzun süre gerekmedikçe en fazla 90 gün.

## Haklarınız (yanıt süresi)

Yayıncı, doğrulanmış bir talepten sonra veri sahibi taleplerine **30 gün** içinde yanıt vermeyi hedefler (makul ölçüde gerekli olduğunda kimlik doğrulaması istenebilir).
