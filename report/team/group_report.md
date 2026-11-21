# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: NKV
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Trả lời bốn câu hỏi của Gate 2a cho trợ lý hoàn phí LogiX-VN trên mẫu 1.200 yêu cầu / 1.624 lần chạy (dữ liệu giả lập): có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra được quyết định. Mọi con số do `src/lab13.py` tính; nhiệm vụ sau dùng lại số của nhiệm vụ trước (A → B → D → E).

## 3. Giải pháp

- **A · Mô hình chi phí** ([bang_chi_phi.md](bang_chi_phi.md)): viết ba hàm A1 (qua 3 phép thử 1,20 · 1,25 · 1,25) và `mo_hinh` tính token + tool trên mọi lần chạy, cộng phút xem lại/làm lại simulated, chia số việc thành công; tách theo `loai`; cộng chi phí cố định 40 triệu đ/tháng.
- **B · Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): gọi lại `mo_hinh` cho 9 kịch bản, 1 cặp, giới hạn 1/2/3 lần chạy và kịch bản xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): hai người gắn nhãn độc lập 20 ca theo 5 loại PAIR, so nhãn, bảng khắc phục 5 ca.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): tính cỡ mẫu cho ba cách chia trước khi chọn; chọn chia theo nhân viên 20 + 20, chấp nhận mde 0,06.
- **E · Chỉ số, rủi ro, hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): ba chỉ số tính thử, 11 event có trace_id, 4 dòng rủi ro kinh tế, hồ sơ 7 mục.

## 4. Kết quả

- Chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu; làm lại chiếm 51,8% [simulated].
- So với nhân viên tự làm: cả hệ thống 0,49× [simulated]; noi_dia 0,22×, hang_nang 0,69×, doi_tac 0,85×, quoc_te 1,88× [simulated] → pilot chỉ gồm noi_dia + hang_nang.
- Yếu tố nhạy nhất: số ca làm lại (±51,8%), tỉ lệ xem lại (±40,7%), lương (+23,1%) [simulated]. Giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ [simulated]). Xem lại 100% đẩy chi phí lên 0,98× (1,03× nếu làm lại 15,3 phút) [simulated].
- Cỡ mẫu: 1.251/nhóm nếu chia theo yêu cầu; theo nhân viên tối đa 1.000 < 1.251, nên chấp nhận mde 0,06 (859/nhóm, ≥ 299 yêu cầu/nhân viên); power ở 5 điểm chỉ 0,64.
- Chỉ số trong đợt chạy thử: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%.
- Đề xuất cuối: **Go có điều kiện** (4 điều kiện, xem `ho_so_launch_v0.md`).
- Kết quả duyệt chéo nhóm nhận được từ hội đồng: ...

## 5. Khó khăn và cách xử lý

- Cài đặt trên Windows: dùng `python -m venv .venv` trong `src/`, cài `requirements.txt`, kiểm tra in `san sang`; script chạy được với Python 3.15 và in tiếng Việt nhờ `sys.stdout.reconfigure(encoding='utf-8')`.
- So với 12.000 đ dễ sai: 4.472 đ chưa tính 222 ca nhân viên làm thay, nên nhóm dùng thêm chi phí cả hệ thống 5.865 đ/yêu cầu (0,49×) [simulated].
- Không cách chia theo cụm nào đủ mẫu cho mức chênh 5 điểm với 40 nhân viên; nhóm ghi rõ đánh đổi (mde 0,06, power 0,64 ở 5 điểm).
- Ngưỡng an toàn: tỉ lệ mở lại hiện tại 3,97% trong phạm vi, nên không dùng ngưỡng tuyệt đối 3% (sẽ dừng ngay tuần đầu) mà so với đối chứng +2 điểm kèm trần 6%.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Hai cột phút xem lại / làm lại là giả lập; mục 1, 2, 3, 7 của hồ sơ phải tính lại bằng phút đo thật sau tuần 1 pilot.
- Đợt chạy thử không có đối chứng nên chưa kết luận được trợ lý nâng chỉ số chính; pilot chỉ đủ power 0,8 cho mức chênh 6 điểm.
- ICC 0,02 là giả định; có thể kiểm tra bằng tỉ lệ thành công theo `staff_id` trong dữ liệu (phần làm thêm).

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", pair.withgoogle.com
- Tài liệu statsmodels, `NormalIndPower`, `proportion_effectsize`
- `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (số tự đối chiếu)
