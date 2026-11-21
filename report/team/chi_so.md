# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Số tính bằng `src/lab13.py` (hàm `nhiem_vu_E`, `nhiem_vu_B`).

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177: 41 sua + 7 bo) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200); phạm vi noi_dia + hang_nang 3,97% (39/982) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm trợ lý được nhân viên mở bằng trợ lý | Số `refund_request_created` (arm = tro_ly) có ít nhất một `agent_suggestion_shown` cùng trace_id, chia số `refund_request_created` của arm tro_ly | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm tra trong tuần (100 đơn/tuần) | Không cần tính |

Chỉ số chính trong đợt chạy thử là 82,83%. Không viết "trợ lý đã nâng chỉ số từ 0,70": đợt chạy thử không có nhóm đối chứng, và mẫu gồm cả các ca nhân viên xem lại hoặc làm thay.

## Danh sách event

Mười một event, mỗi event có `trace_id` để nối với trace của agent (`logix_runs.csv`).

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, depot, staff_id, arm (tro_ly / doi_chung), trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status (ok / loi), trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu / sua / bo), phut_xem_lai (đo thật), trace_id | Khi bấm gửi / sửa / bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua (ok / loi), trace_id | Khi ghi sổ hoàn tiền |
| `handoff_to_staff` | Agent | reason (thieu_du_lieu / ngoai_pham_vi / het_lan_chay), tom_tat, trace_id | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | created_at, closed_at, trace_id | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần, 100 đơn ngẫu nhiên |
| `input_validation_failed` | Agent | truong_loi (ma_don / so_tai_khoan / dinh_dang), mau_nhap, trace_id | Khi đầu vào của khách không hợp lệ (dùng cho bảng lỗi, ca 9) |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chính: `ticket_closed` (closed_at − created_at ≤ 24 giờ) và không có `ticket_reopened` trong 7 ngày, chia `refund_request_created`. Đo được.
- Dùng (bỏ qua gợi ý): `staff_review_decision` với quyet_dinh ∈ {sua, bo}, chia tổng `staff_review_decision`. Đo được.
- An toàn (lỗi lọt đến khách): `ticket_reopened` trong 7 ngày, chia `refund_request_created`. Đo được; hoàn trùng đếm bằng hai `refund_ledger_write` ok cho cùng request_id.
- Dùng (tự đề xuất): `agent_suggestion_shown` nối với `refund_request_created` theo trace_id và arm. Đo được.
- An toàn (tự đề xuất): `audit_sample_checked`. Đo được.
- Chi phí mỗi việc thành công (dùng trong luật dừng): `agent_run_completed` (token, tool) + `staff_review_decision.phut_xem_lai` + `staff_rework_completed.phut_lam_lai`, chia số việc thành công. Đo được, và thay được hai cột `_simulated` bằng phút đo thật.

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy (`bang_chi_phi.md`). Mọi số chi phí là simulated.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, chi phí mỗi việc thành công lên 6.787 đ [simulated] (B1) | Tỉ lệ `staff_rework_completed` theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi noi_dia + hang_nang) | Thu hẹp về noi_dia, rà 20 trace làm lại gần nhất, sửa prompt/tool trước khi mở lại hang_nang | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× (12.414 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu) [simulated] (B4) | % yêu cầu được xem lại còn > 50% vào cuối bước rollout 0.25, hoặc phút xem lại trung bình > 5 phút (hoà vốn 5,1 / 4,8 phút) | Giảm xem lại theo bậc (100% → 50% → 20%) khi tỉ lệ sua + bo < 15%; đo phút xem lại thật từ `staff_review_decision` | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yc/tháng, +2.370 đ/việc nếu còn một nửa (5.784 đ = 0,48×) [simulated] (A4) | Số việc thành công theo tuần < 50% kế hoạch (kế hoạch: 33.750 việc/tháng ở quy mô đầy đủ) | Không mở rộng pilot; xem lại hợp đồng chi phí cố định với nhà cung cấp | PM trợ lý hoàn phí |
| Lương nhân viên tăng | +23,1% khi lương tăng 25%, lên 5.506 đ [simulated] (B1) | Điều chỉnh đơn giá phút nhân viên trong kỳ ngân sách | Cập nhật mô hình chi phí; ưu tiên giảm phút xem lại để bù | Giám đốc vận hành LogiX-VN |
