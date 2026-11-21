# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

> **Ghi chú nhóm 1 thành viên:** Nhóm NKV chỉ có 1 thành viên (Nguyễn Khánh Vinh) nên tự gắn nhãn đầy đủ 20 ca theo nguyên nhân gốc của Google PAIR (không có người gắn nhãn thứ 2 để so chéo độc lập). Cột `Nhãn thống nhất` giữ nguyên bộ nhãn đã gắn; bảng khắc phục 5 ca bên dưới khớp 100% với `Nhãn thống nhất`.

## Bộ nhãn của nhóm

Người gắn nhãn 1: Nguyễn Khánh Vinh · Người gắn nhãn 2: Không áp dụng (nhóm 1 thành viên)

| Ca | Tóm tắt ca (từ đề bài) | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- | --- |
| 1 | Khách nhập số tài khoản thiếu 2 chữ số, ngân hàng báo lỗi | Do người dùng | — | — | Do người dùng |
| 2 | Kiện 28 kg, tool tra giá hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ, khách mở lại | Hệ thống | — | — | Hệ thống |
| 3 | Thiết kế hoàn về ví LogiX, khách chờ tiền về ngân hàng nên báo "chưa được hoàn" | Ngữ cảnh | — | — | Ngữ cảnh |
| 4 | Chặng do hãng nước ngoài giao, không có dữ liệu; trợ lý chuyển nhân viên | Giới hạn hệ thống | — | — | Giới hạn hệ thống |
| 5 | Kiểm tra mẫu thấy 14 đơn có mã giảm giá hoàn theo giá trước giảm, không ai báo | Ngầm | — | — | Ngầm |
| 6 | Khách chọn "giao trễ" nhưng mô tả hàng vỡ; trợ lý xử lý luồng giao trễ và từ chối | Do người dùng | — | — | Do người dùng |
| 7 | API sổ cái lỗi 503, thử lại 3 lần vẫn báo khách "đã hoàn thành công" | Hệ thống | — | — | Hệ thống |
| 8 | Trích "Điều 7.2" không có trong chính sách hiện hành; số tiền vẫn đúng | Hệ thống | — | — | Hệ thống |
| 9 | Khách nhập mã đơn sàn TMĐT thay vì mã vận đơn; trợ lý báo không hợp lệ, không gợi ý | Do người dùng | — | — | Do người dùng |
| 10 | Từ chối hoàn do bão, đúng chính sách; app vẫn hiện "cam kết giao 24 giờ" | Ngữ cảnh | — | — | Ngữ cảnh |
| 11 | Khách gửi tin nhắn thoại 40 giây; trợ lý không xử lý được âm thanh | Giới hạn hệ thống | — | — | Giới hạn hệ thống |
| 12 | Tool depot D05 thiếu một trường, kết quả vẫn đúng nhưng token gấp 3 lần suốt 3 tuần | Ngầm | — | — | Ngầm |
| 13 | Hỏi hoàn phí bảo hiểm của đối tác, ngoài phạm vi; trợ lý trả lời chung chung | Giới hạn hệ thống | — | — | Giới hạn hệ thống |
| 14 | Khách bấm nhầm "Xác nhận đã nhận tiền", yêu cầu bị đóng | Do người dùng | — | — | Do người dùng |
| 15 | Trễ 26 giờ, chính sách hoàn 50%, trợ lý tính 100%; nhân viên bắt được | Hệ thống | — | — | Hệ thống |
| 16 | Gửi thông báo Zalo lúc 2:14 sáng theo thiết kế "gửi ngay"; khách bị làm phiền | Ngữ cảnh | — | — | Ngữ cảnh |
| 17 | Dùng bảng giá cũ trong bộ nhớ đệm, lệch 1.000–2.000 đ, 212 đơn/9 ngày, không ai mở lại | Ngầm | — | — | Ngầm |
| 18 | Tính đúng 15.000 đ nhưng không ghi cách tính; khách tưởng hoàn thiếu, mở lại | Ngữ cảnh | — | — | Ngữ cảnh |
| 19 | Đơn 14 tháng trước, trợ lý chỉ truy cập 12 tháng; nói rõ và chuyển nhân viên | Giới hạn hệ thống | — | — | Giới hạn hệ thống |
| 20 | Khách gửi lại sau 10 phút, trợ lý hoàn hai lần vì thiếu khoá chống trùng | Hệ thống | — | — | Hệ thống |

**Tỉ lệ đồng thuận:** Không áp dụng so 2 người (nhóm 1 thành viên; đã gắn đủ 20/20 ca: 4 Do người dùng · 5 Hệ thống · 4 Ngữ cảnh · 4 Giới hạn hệ thống · 3 Ngầm).

## Quy tắc phân biệt cho các ca dễ lẫn

Mỗi ca ranh giới ghi rõ một câu lý do chọn nhãn theo nguyên nhân gốc:

- Không có ca không trùng do nhóm chỉ có 1 người gắn nhãn.
- **Ca 6, 9 (`Do người dùng`):** Gốc lỗi do khách chọn sai luồng hoặc nhập sai mã sàn TMĐT thay vì mã vận đơn; việc trợ lý chưa gợi ý nằm ở phần khắc phục.
- **Ca 8, 15 (`Hệ thống`):** Sai sót (bịa điều khoản, tính sai 100% thay vì 50%) đã lộ ra ngay lúc xử lý, không phải lỗi `Ngầm`.
- **Ca 12 (`Ngầm`):** Kết quả vẫn đúng nhưng chi phí token tăng gấp 3 lần suốt 3 tuần không ai phát hiện — sai sót về chi phí cũng tính là lỗi `Ngầm`.
- **Ca 13 (`Giới hạn hệ thống`):** Hoàn phí bảo hiểm đối tác nằm ngoài phạm vi trợ lý; việc trả lời chung chung là cách xử lý giới hạn chưa tốt, không đổi nguyên nhân gốc.
- **Ca 18 (`Ngữ cảnh`):** Số tiền 15.000 đ tính đúng chính sách, chỉ thiếu câu giải thích nên khách hiểu lầm.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội". Event lấy từ danh sách trong `chi_so.md`. Nhóm phải kiểm tra lại cột "Loại lỗi" theo nhãn thống nhất sau khi so nhãn.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (lý do, mẫu mã nhập, trace_id); cảnh báo khi > 2% số yêu cầu trong ngày | Nhận diện định dạng mã của sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn tìm mã vận đơn kèm ảnh minh hoạ | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" không có `refund_ledger_write` kết quả ok cùng trace_id; ngưỡng 0 ca, có 1 ca là báo động | Chỉ gửi "đã hoàn" sau khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo "đang xử lý" và `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` với reason = so_tien mà kiểm tra thấy số tiền đúng, theo tuần; ngưỡng > 0,5% số yêu cầu | Mẫu tin nhắn luôn ghi cách tính, ví dụ "30.000 đ × 50% = 15.000 đ (trễ 24–48 giờ)" | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với reason = thieu_du_lieu, đếm theo loại yêu cầu mỗi tuần; quoc_te đang chỉ 27,3% thành công (A3) | Giữ cách chuyển nhân viên kèm tóm tắt; đưa quoc_te ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | `audit_sample_checked`: kiểm tra mẫu 100 đơn/tuần so với bảng giá hiện hành; ngưỡng > 1% đơn lệch tiền | Xoá bộ nhớ đệm khi có bảng giá mới; ghi phiên bản bảng giá vào trace để truy được đơn bị ảnh hưởng | Kế toán trưởng |
