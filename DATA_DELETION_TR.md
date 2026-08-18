> **Türkçe sürüm.** Herhangi bir çelişki durumunda [İngilizce](./DATA_DELETION.md) sürüm geçerlidir.

---

# Veri Silme — Organize Files

**Organize Files**, dosyalarınızı **cihazınızda yerel olarak** işler. Yayıncı bir
hesap sistemi **işletmez** ve normal düzenleme veya onarım işlemleri sırasında
dosyalarınızı kendi sunucularında **saklamaz**. Sunucu tarafında bir hesap
olmadığından, verilerinizin çoğu cihazınızdan asla ayrılmaz ve üzerlerinde tam
kontrolü elinizde tutarsınız.

Bu sayfa, uygulamanın cihazınızda sakladığı verileri ve yayıncının tutabileceği
sınırlı verileri nasıl sileceğinizi açıklar.

## Cihazınızda saklanan veriler

Uygulama; oturum anlık görüntüleri, devam durumu, isteğe bağlı günlükler,
deneme/lisans durumu ve — yalnızca e-posta bildirimlerini etkinleştirirseniz —
şifrelenmiş bir SMTP parolası gibi yerel çalışma verilerini saklar. Bunları
istediğiniz zaman kaldırabilirsiniz:

1. **Uygulama verilerini temizle** — uygulamayı açın ve **Uygulama verilerini
   temizle** seçeneğini kullanın. Bu; oturumları, günlükleri ve otomasyon
   taslaklarını kaldırır. Yerel lisans durumunu ve isteğe bağlı lisans kontrolleri
   için kullanılan anonim bir kurulum tanımlayıcısını koruyabilir; uygulama
   içindeki onay, tam olarak neyin korunduğunu açıklar.
2. **Uygulamayı kaldır** — uygulamayı kaldırmak, mobilde özel depolamasını siler.
   Masaüstünde profil klasörünü de manuel olarak silebilirsiniz:
   - Windows: `%LocalAppData%\OrganizeFilesCrossPlatform\`
   - Linux / macOS: kullanıcı dizininizdeki uygulama profil klasörü
3. **Çıktı klasörlerini sil** — oluşturduğunuz düzenlenmiş veya onarılmış dosyalar,
   siz silene kadar kalır.

## Yayıncının tutabileceği veriler

Yayıncı yalnızca etkin olarak gönderdiğiniz verileri tutar, örneğin:

- Destek ile iletişime geçerseniz **destek e-postası** yazışmaları
- Yalnızca yapınız için bir lisans sunucusu yapılandırılmışsa **lisans sunucusu
  kayıtları**

Bu verilerin silinmesini talep etmek için **razvan.gutulov@outlook.com** adresine
şunları belirterek yazın:

- Destek ile iletişime geçmek için kullandığınız e-posta adresi ve/veya
- Varsa lisans veya sipariş referansınız

Yayıncı, doğrulanmış bir talepten sonra **30 gün** içinde yanıt vermeyi hedefler.
Bazı kayıtlar, yasaların gerektirdiği durumlarda (örneğin vergi ve muhasebe
kayıtları) saklanabilir. Saklamayla ilgili tüm ayrıntılar için
[Gizlilik Politikası](./PRIVACY_POLICY_TR.md)'na bakın.

## Mağaza satın alımları

Satın alımlar ve faturalandırma, satın aldığınız mağaza (Microsoft Store, Google
Play veya Apple App Store) tarafından yönetilir. Mağazanın tuttuğu satın alma
verilerini yönetmek veya silmek için o mağazanın hesap ayarlarını kullanın.

---

© 2026 Razvan Constantin Gutulov. Tüm hakları saklıdır.
