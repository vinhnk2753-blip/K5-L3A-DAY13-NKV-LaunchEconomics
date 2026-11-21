# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: NKV · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated] toàn mẫu, gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); phạm vi noi_dia + hang_nang 3.414 đ, cộng cố định 4.599 đ [simulated] ([bang_chi_phi.md](bang_chi_phi.md) A2, A4) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại ±51,8% · 2. Tỉ lệ xem lại ±40,7% · 3. Lương nhân viên +23,1%; giá token chỉ ±5,6% [simulated] (B1, B2) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated]; theo loại: noi_dia 0,22×, hang_nang 0,69×, doi_tac 0,85×, quoc_te 1,88×. **Bất lợi:** xem lại 100% thì 0,98× (1,03× nếu làm lại 15,3 phút) [simulated] (A3, B4) | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử: chính 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177) · mở lại 7 ngày 4,25% (51/1.200), phạm vi 3,97%; 11 event có trace_id ([chi_so.md](chi_so.md)) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, 5 loại PAIR (4 Do người dùng · 5 Hệ thống · 4 Ngữ cảnh · 4 Giới hạn · 3 Ngầm; nhóm 1 thành viên tự gắn đủ 20/20 ca); bảng khắc phục 5 ca (9, 7, 18, 4, 17), mỗi ca có ngưỡng phát hiện và một vai trò; ca 7 và 20 (báo hoàn khi sổ cái lỗi, hoàn trùng) phải sửa trước pilot ([bang_loi.md](bang_loi.md)) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, ngẫu nhiên phân tầng theo depot; mde 0,06, n = 859/nhóm, ≥ 299 yêu cầu/nhân viên, DE 6,96; 3 luật dừng có ngưỡng, thời hạn, người dừng; quyết định 2027-01-05. **Bất lợi:** power chỉ 0,64 nếu tác động thật là 5 điểm ([pilot_plan.yaml](pilot_plan.yaml)) | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi → 6.787 đ (+51,8%); xem lại 100% → 11.743 đ (0,98×); khối lượng còn một nửa → cố định 2.370 đ/việc, 5.784 đ (0,48×) [simulated] ([chi_so.md](chi_so.md) E2) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot chỉ gồm noi_dia + hang_nang (loại quoc_te 1,88× và doi_tac 0,85× [simulated]). Lý do: phạm vi pilot rẻ hơn nhân viên (0,38× kể cả cố định [simulated]), nhưng lợi thế này mất nếu phải xem lại 100% (0,98×), và với 40 nhân viên pilot chỉ đủ mẫu để thấy mức chênh 6 điểm.

- Sửa khoá chống trùng (ca 20) và chỉ báo "đã hoàn" khi sổ cái trả ok (ca 7); đối soát mỗi giờ cho 0 ca lệch trong 3 ngày chạy thử nội bộ · Kỹ sư trưởng agent · kiểm tra 2026-11-30.
- Giám đốc vận hành ký chấp nhận mde 0,06 (power 0,64 ở mức 5 điểm) và ba luật dừng trong `pilot_plan.yaml` · Giám đốc vận hành LogiX-VN · kiểm tra 2026-11-30.
- Bật đủ 11 event có trace_id; thay phút simulated bằng phút xem lại, làm lại đo thật sau tuần 1, tính lại chi phí mỗi việc thành công · PM trợ lý hoàn phí · kiểm tra 2026-12-08.
- Kế hoạch giảm xem lại theo bậc (100% → 50% → 20% khi sua + bo < 15%), mục tiêu phút xem lại ≤ 5 phút (hoà vốn 5,1 phút) · Trưởng nhóm CSKH · kiểm tra 2026-12-15 (cuối bước rollout 0.25).
