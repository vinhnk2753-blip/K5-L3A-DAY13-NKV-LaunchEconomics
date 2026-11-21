# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py` (chạy `python lab13.py` trong `src/`). Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 · ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 · ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 · ĐẠT (= 1/p, k triệt tiêu giữa tử và mẫu) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` (mọi 1.624 lần chạy, kể cả lần lỗi) | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` (5.600 lần gọi × 15 đ) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút × 2.000 đ) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút × 2.000 đ) | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` = `thanh_cong` | |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? **16,3 lần** (4.472 ÷ 274,7) [simulated]: hoá đơn token bỏ qua giờ nhân viên và chia cho cả 222 yêu cầu không thành công.
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại, 51,8%** [simulated], kế đến xem lại 40,7% [simulated]; giờ nhân viên chiếm 92,5% [simulated], token + tool chỉ 7,5%.
- So với nhân viên tự làm phải cộng 222 ca không thành công (148 `chuyen_nhan_vien` + 74 `lam_lai`): (4.373.585 + 222 × 12.000) ÷ 1.200 = **5.865 đ/yêu cầu = 0,49×** [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× [simulated] |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× [simulated] |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× [simulated] |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× [simulated] |

Tỉ lệ `status = ok` theo lần thử (đo từ trace): quoc_te 30,0% → 11,4% → 2,2%; doi_tac 51,5% → 18,2% → 14,8%; noi_dia 91,0% → 75,7% → 38,9%.

- Loại nào không đáng để trợ lý xử lý? **quoc_te**: 1,88× chi phí nhân viên [simulated], chỉ 27,3% thành công dù chạy 2,32 lần/yêu cầu. Chạy lại không giúp: lần 2 chỉ đúng 11,4%, lần 3 chỉ 2,2%, vì lỗi lặp lại trên cùng yêu cầu (thiếu dữ liệu chặng nước ngoài), nên chỉ tốn thêm tiền.
- doi_tac sát ngưỡng (0,85× [simulated], thành công 54,4%) và có điều khoản riêng, nên cũng loại khỏi phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Trong phạm vi: 982 yêu cầu, 900 việc thành công, tổng 3.072.513 đ → 3.414 đ/việc thành công [simulated]. Việc thành công mỗi tháng = 45.000 × 900 ÷ 1.200.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× [simulated] |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× [simulated] |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không đổi ở 45.000 yc/tháng (0,38×) hay một nửa (0,48×) [simulated]; nhưng cố định tỉ lệ nghịch với khối lượng. Tính tay: hoà vốn khi cố định = 12.000 − 3.414 = 8.586 đ/việc, tức 40.000.000 ÷ 8.586 ≈ 4.660 việc/tháng (~14% khối lượng) [simulated].

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ [simulated]. Tất cả số trong bảng là simulated.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

Tự kiểm tra: mỗi kịch bản "giảm một nửa" giảm đúng nửa mức tăng của "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9).

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated], đúng bằng tổng hai tác động riêng (+5,6% + 40,7%) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **Số ca làm lại** (±51,8%) · 2. **Tỉ lệ xem lại** (±40,7%) · 3. **Lương nhân viên** (+23,1% khi tăng 25%). Giá token chỉ ±5,6% [simulated].

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay). Tất cả là simulated.

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ (rẻ nhất)** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn nào rẻ nhất cho công ty? **2 lần**: 6.901.220 đ [simulated], rẻ hơn 3 lần 136.365 đ. Không trùng với giới hạn có chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ), vì giới hạn 1 lần đẩy thêm 85 việc sang nhân viên (319 so với 234).

## B4 · Nếu phải xem lại tất cả

Phạm vi noi_dia + hang_nang: 982 yêu cầu, 948 có ít nhất một lần chạy ok × 5 phút = 9.480.000 đ; 48 ca lam_lai × 9 phút = 864.000 đ; token + tool 224.513 đ; tổng 10.568.513 đ ÷ 900 việc thành công.

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: **11.743 đ = 0,98×** [simulated]. Nếu làm lại mất 15,3 phút như trung bình dữ liệu (trung vị 14,5) thì **12.414 đ = 1,03×** [simulated], đắt hơn nhân viên tự làm. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (làm lại 9 phút) hoặc ≤ 4,8 phút (làm lại 15,3 phút).
- Kết quả này nói gì về thứ pilot cần học được? Xem lại chiếm ~90% chi phí (9,48 / 10,57 triệu đ) [simulated], nên xem lại 100% gần như xoá hết tiết kiệm. Pilot phải đo được tỉ lệ xem lại giảm an toàn tới mức nào và thời gian mỗi lần xem lại có dưới 5 phút không.
