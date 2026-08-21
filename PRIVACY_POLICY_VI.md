> **Bản dịch máy không chính thức — không phải tư vấn pháp lý.** [EULA tiếng Anh](./EULA_EN.md) và [Chính sách quyền riêng tư tiếng Anh](./PRIVACY_POLICY_EN.md) sẽ chi phối nếu bản dịch này xung đột với chúng. Tham khảo ý kiến ​​​​tư vấn có trình độ trong khu vực pháp lý của bạn.

---

# Chính sách quyền riêng tư - Sắp xếp tệp

**Nhà xuất bản:** Guțulov Răzvan Constantin PFA  
**Địa chỉ đăng ký:** Str. Republicii nr. 33B, bl. N3, sc. A, et. 1, ap. 3, Breaza de Sus, 105400 Breaza, jud. Prahova, România  
**Đăng ký kinh doanh:** F2026004513003 (EUID ROONRC.F2026004513003)  
**Mã số thuế:** 53610310  
**Liên hệ:** razvan.gutulov@outlook.com  
**Ngày có hiệu lực:** 28-05-2026  
**URL công khai:** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_VI.md`

---

## Tóm tắt

Tổ chức Tệp xử lý tệp **cục bộ trên thiết bị**. Nội dung tệp **không được tải lên máy chủ của chính nhà xuất bản** cho các hoạt động sắp xếp hoặc sửa chữa thông thường. Ứng dụng **ghi các tệp cục bộ** trên thiết bị (ảnh chụp nhanh phiên, trạng thái tiếp tục, nhật ký tùy chọn) như được mô tả bên dưới.

## Dữ liệu được xử lý cục bộ

| Dữ liệu | Nơi lưu trữ | Mục đích |
|------|-------|----------|
| Các tập tin và thư mục bạn chọn | Chỉ thiết bị của bạn | Sắp xếp, loại bỏ trùng lặp, sửa chữa, xóa tùy chọn |
| Ảnh chụp nhanh phiên giao diện người dùng (`last-ui-session.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (máy tính để bàn) hoặc bộ nhớ riêng của ứng dụng (Android) | Khôi phục không gian làm việc: đường dẫn, tiện ích mở rộng, tùy chọn |
| Sắp xếp sơ yếu lý lịch + tạp chí di chuyển tùy chọn | Xuất `_OrganizeMediaLogs` hoặc thư mục phiên | Bỏ qua các nước đi đã hoàn thành; siêu dữ liệu khôi phục (đường dẫn được mã hóa) |
| Tùy chọn chạy nhịp tim JSON | Đầu ra `_OrganizeMediaLogs` | Bộ đếm tiến độ cho các công cụ bên ngoài |
| Trạng thái dùng thử / giấy phép | Thư mục hồ sơ trong Dữ liệu ứng dụng cục bộ | Thực thi quyền dùng thử hoặc quyền lưu trữ |
| Trạng thái kiểm tra cập nhật | Thư mục hồ sơ | Kiểm tra bảng kê khai phiên bản tùy chọn của ga |
| Dàn dựng SAF của Android | Thư mục phiên trong bộ nhớ ứng dụng | Sao chép cây `content://` để công cụ có thể đọc chúng |
| Mật khẩu SMTP tùy chọn cho thông báo email | Được lưu mã hóa trong tùy chọn phiên trên thiết bị (AES-GCM với tệp khóa theo hồ sơ). Khi nâng cấp, nếu trường này tồn tại, mọi mật khẩu SMTP cũ lưu không dùng AES-GCM sẽ được ghi lại một lần sang AES-GCM. Tệp khóa AES-GCM nằm trong thư mục hồ sơ ứng dụng và tài khoản người dùng OS đang đăng nhập có thể đọc; nó bảo vệ việc đọc JSON tùy chọn một cách tình cờ, không phải kho phần cứng. | Chỉ khi bật thông báo email và nhập thông tin SMTP |

## Những gì nhà xuất bản không nhận được theo mặc định

- Nội dung tệp từ các lần tổ chức/sửa chữa  
- Danh bạ, vị trí, micrô hoặc máy ảnh (không được sử dụng)  
- SDK phân tích được gói trong cây nguồn mở  

## Sử dụng mạng tùy chọn

| Hoạt động | Dữ liệu được gửi | Người nhận |
|----------|-------------|----------|
| Kiểm tra cập nhật tùy chọn | HTTPS NHẬN bản kê khai phiên bản. Máy chủ (ví dụ GitHub) nhận được địa chỉ IP yêu cầu, Tác nhân người dùng `OrganizeFiles-UpdateCheck/1.0` và siêu dữ liệu TLS. Không có đường dẫn tệp hoặc nội dung tệp nào được gửi. Tắt bằng `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Máy chủ phân phát tệp kê khai JSON |
| Cửa hàng mua / giấy phép | API thanh toán nền tảng | Microsoft, Google hoặc Apple (mỗi kênh) |
| Máy chủ cấp phép tùy chọn (được định cấu hình bởi nhà điều hành) | ID cài đặt liên tục ngẫu nhiên (GUID được lưu trữ trong `license_installation_id.txt`) được gửi đến máy chủ cấp phép do nhà xuất bản hoặc nhà điều hành định cấu hình tại `ORGANIZE_FILES_LICENSE_SERVER_URL`. ID cài đặt là mã nhận dạng thiết bị theo GDPR Recital 30. Cơ sở hợp pháp: thực hiện hợp đồng. Lưu giữ do nhà phát hành vận hành: hồ sơ quyền trong thời gian hoạt động cộng thêm tối đa 24 tháng sau khi hết hạn/thu hồi để ngăn lạm dụng và xử lý tranh chấp; hồ sơ kế toán có thể được lưu tối đa 7 năm khi luật yêu cầu. Máy chủ do nhà điều hành vận hành tuân theo lịch lưu giữ đã được nhà điều hành ghi nhận. Tính năng này không hoạt động trừ khi `ORGANIZE_FILES_LICENSE_SERVER_URL` được đặt. | Máy chủ cấp phép nhà xuất bản hoặc nhà điều hành |
| Theo dõi OpenTelemetry tùy chọn (được định cấu hình bởi nhà điều hành) | Khi `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT` được đặt, siêu dữ liệu công việc tự động hóa (ID công việc, ID tương quan, thẻ loại mục tiêu, ngữ cảnh theo dõi W3C) được xuất sang bộ thu thập OTLP đã định cấu hình. Không có đường dẫn tệp hoặc nội dung tệp nào được bao gồm. Tính năng này không hoạt động theo mặc định và yêu cầu cấu hình toán tử rõ ràng. | Bộ thu thập OTLP do nhà điều hành định cấu hình |
| Thông báo email tùy chọn (khi bật) | Trạng thái chạy và đoạn nhật ký (có thể gồm đường dẫn tệp) gửi qua máy chủ SMTP do nhà điều hành cấu hình | SMTP / nhà cung cấp thư của nhà điều hành |
| Webhook tự động hóa tùy chọn (do người vận hành cấu hình) | Khi đặt `ORGANIZE_FILES_AUTOMATION_WEBHOOK_URL`, các sự kiện vòng đời công việc kèm mã tương quan và đường dẫn tệp trạng thái tự động hóa | Điểm cuối webhook do người vận hành cấu hình |
| Người trợ giúp thử lại NAS động cơ | Không có gì ngoài đường dẫn mạng được cấu hình | Máy chủ NAS / SMB |

Kiểm tra cập nhật so sánh **chỉ siêu dữ liệu phiên bản**. Ứng dụng dành cho máy tính để bàn có thể chạy kiểm tra này một lần mỗi ngày sau khi chấp nhận EULA trừ khi bị tắt.

## Cơ sở pháp lý (đóng khung theo kiểu GDPR, không phải tư vấn pháp lý)

| Đang xử lý | Cơ sở điển hình |
|----------||-------|
| Tổ chức/sửa chữa cục bộ trên các thư mục đã được chọn | Thực hiện hợp đồng/lợi ích hợp pháp của nhà điều hành |
| Các tập tin phiên, sơ yếu lý lịch và nhịp tim cục bộ | Tương tự — cần thiết để cung cấp công cụ |
| Lưu trữ thanh toán và quyền lợi | Hợp đồng với cửa hàng nền tảng |
| Kiểm tra bảng kê khai cập nhật tùy chọn | Lợi ích hợp pháp đối với các bản cập nhật bảo mật; có thể bị vô hiệu hóa thông qua biến môi trường |
| Email hỗ trợ | Lãi suất hợp pháp/các bước trước hợp đồng theo yêu cầu của bạn |

## Chuyển khoản quốc tế

Kiểm tra cập nhật tùy chọn có thể đến các máy chủ bên ngoài Khu vực Kinh tế Châu Âu (ví dụ: GitHub ở Hoa Kỳ). Việc thanh toán tại cửa hàng được xử lý theo các điều khoản của từng nền tảng.

## Thẩm quyền giám sát và khiếu nại

Nếu luật hiện hành cấp quyền đối với chủ thể dữ liệu hoặc khiếu nại lên cơ quan giám sát, trước tiên hãy liên hệ với nhà xuất bản theo địa chỉ **razvan.gutulov@outlook.com**. Cư dân EU/EEA cũng có thể khiếu nại với cơ quan bảo vệ dữ liệu địa phương của họ (đối với Romania: ANSPDCP, https://www.dataprotection.ro).

## Bộ xử lý của bên thứ ba (khi sử dụng các tính năng này)

- **Microsoft Store / Google Play / Mac App Store** — thanh toán và quyền lợi. Google Play sử dụng Thanh toán trên thiết bị; danh sách sản xuất phải thêm tính toàn vẹn của Play và/hoặc xác minh phía máy chủ theo chính sách của Google.
- **GitHub (hoặc máy chủ lưu trữ tệp kê khai)** — phiên bản JSON tùy chọn qua HTTPS (có thể bao gồm IP máy khách trong nhật ký máy chủ)
- **Ứng dụng email** — khi liên hệ với bộ phận hỗ trợ qua liên kết mailto

## Trách nhiệm của người vận hành (đóng khung theo kiểu GDPR)

Dữ liệu cá nhân có thể tồn tại **bên trong** tệp của bạn. Nếu xử lý dữ liệu đó, bạn (hoặc tổ chức của bạn) có thể là **người kiểm soát dữ liệu** và phải chọn cơ sở hợp pháp, giảm thiểu việc lưu giữ và phản hồi các yêu cầu của chủ thể dữ liệu.

## Giữ chân

Các tệp cục bộ vẫn còn cho đến khi bạn xóa chúng, xóa dữ liệu ứng dụng, gỡ cài đặt ứng dụng hoặc ghi đè các thư mục đầu ra. Nhà xuất bản không vận hành lịch trình lưu giữ tập trung cho dữ liệu chỉ cục bộ.

Đối với dữ liệu do nhà phát hành nắm giữ:

- Email hỗ trợ và thư từ: tối đa 24 tháng sau lần liên hệ có ý nghĩa cuối cùng, trừ khi tranh chấp hoặc nghĩa vụ pháp lý yêu cầu lưu giữ lâu hơn.
- Hồ sơ mua trực tiếp, hoàn tiền, thuế và kế toán: tối đa 7 năm khi luật thuế hoặc kế toán yêu cầu.
- Hồ sơ quyền trên máy chủ giấy phép do nhà phát hành vận hành: trong thời gian quyền còn hoạt động cộng thêm tối đa 24 tháng sau khi hết hạn hoặc bị thu hồi.
- Nhật ký truy cập và bảo mật trên máy chủ do nhà phát hành vận hành: tối đa 90 ngày, trừ khi cần lâu hơn cho điều tra bảo mật, phòng chống gian lận hoặc khiếu nại pháp lý.

## Quyền của bạn

Đối với dữ liệu mà nhà xuất bản lưu giữ (ví dụ: hỗ trợ thư từ qua email), hãy liên hệ **razvan.gutulov@outlook.com**. Đối với dữ liệu chỉ được lưu trữ trên thiết bị của bạn, bạn có thể xóa hầu hết dữ liệu ứng dụng thông qua **Xóa dữ liệu ứng dụng**, gỡ cài đặt hoặc xóa tệp thủ công. **Xóa dữ liệu ứng dụng** xóa phiên, nhật ký và bản nháp tự động hóa nhưng có thể giữ lại các neo dùng thử giấy phép, điểm đánh dấu cài đặt trả phí và mã nhận dạng cài đặt ẩn danh được sử dụng để kiểm tra giấy phép tùy chọn — hãy xem văn bản xác nhận trong ứng dụng trước khi bạn tiếp tục.

## Trẻ em

Công cụ năng suất chung không hướng tới trẻ em dưới 13 tuổi (hoặc độ tuổi được yêu cầu tại khu vực pháp lý của bạn).

## Thay đổi

Những thay đổi quan trọng sẽ xuất hiện trong danh sách cửa hàng và tài liệu trong ứng dụng trước khi phát hành.

## Tài liệu liên quan

- [EULA (tiếng Anh)](./EULA_EN.md)  
- [Chính sách quyền riêng tư (tiếng Romania)](./PRIVACY_POLICY_RO.md)  
- [Chính sách quyền riêng tư (tiếng Đức)](./PRIVACY_POLICY_DE.md)  
- [Chính sách quyền riêng tư (tiếng Pháp)](./PRIVACY_POLICY_FR.md)

---

Khi bản dịch này chưa đầy đủ, Chính sách quyền riêng tư tiếng Anh sẽ được áp dụng.

## Bên kiểm soát và liên hệ

Đối với dữ liệu cá nhân do nhà phát hành xử lý, bên kiểm soát là **Guțulov Răzvan Constantin PFA**. Liên hệ: **razvan.gutulov@outlook.com**.

## Lưu giữ (hồ sơ của nhà phát hành)

Đối với dữ liệu do nhà phát hành giữ:

- Email hỗ trợ và thư từ: tối đa 24 tháng sau lần liên hệ có ý nghĩa cuối cùng, trừ khi tranh chấp hoặc nghĩa vụ pháp lý yêu cầu lưu giữ lâu hơn.
- Hồ sơ mua trực tiếp, hoàn tiền, thuế và kế toán: tối đa 7 năm khi luật thuế hoặc kế toán yêu cầu.
- Hồ sơ quyền trên máy chủ giấy phép do nhà phát hành vận hành: trong thời gian quyền còn hoạt động cộng thêm tối đa 24 tháng sau khi hết hạn hoặc bị thu hồi.
- Nhật ký truy cập và bảo mật trên máy chủ do nhà phát hành vận hành: tối đa 90 ngày, trừ khi cần lâu hơn cho điều tra bảo mật, phòng chống gian lận hoặc khiếu nại pháp lý.

## Quyền của bạn (thời gian phản hồi)

Nhà phát hành đặt mục tiêu phản hồi yêu cầu của chủ thể dữ liệu trong vòng **30 ngày** sau khi yêu cầu được xác minh (có thể yêu cầu xác minh danh tính khi cần thiết hợp lý).
