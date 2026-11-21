# Báo cáo cá nhân — NguyenKhanhVinh-2A202603390

## 1. Thông tin thành viên

- Họ tên: Nguyễn Khánh Vinh
- MSSV: 2A202603390
- Email: vinh.nk.2753@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Nhóm 1 thành viên (đảm nhiệm cả 4 vai trò: người viết code, người kiểm số, người gắn nhãn, người giữ hồ sơ)

## 2. Phần việc phụ trách

- Thiết lập môi trường Python (`src/.venv`) và chạy kiểm chứng toàn bộ `src/lab13.py`.
- Thực hiện Nhiệm vụ A (mô hình chi phí, tách theo loại yêu cầu, chi phí cố định), Nhiệm vụ B (độ nhạy, giới hạn chạy lại, xem lại 100%), Nhiệm vụ D (`pilot_plan.yaml`), Nhiệm vụ E (`chi_so.md`, `ho_so_launch_v0.md`) và `group_report.md`.
- Thực hiện Nhiệm vụ C (`bang_loi.md`) với bộ nhãn tự gắn theo khung Google PAIR.

## 3. Đóng góp cụ thể

- Viết và chạy `src/lab13.py`: đạt 3 phép thử A1 (`1,20`, `1,25`, `1,25`) và tính toàn bộ số liệu A2, A3, A4, B1–B4, D1, D3, E1 trên dữ liệu `logix_runs.csv` và `logix_requests.csv`.
- Lập `report/team/bang_chi_phi.md` với đầy đủ bảng số liệu, gắn nhãn `simulated` cho các số từ hai cột `_simulated`, và trả lời ngắn gọn ≤ 3 dòng có số.
- Lập `report/team/pilot_plan.yaml` chọn phương án chia theo nhân viên (20 + 20, `mde = 0,06`, `n = 859/nhóm`, `m ≥ 299`), nêu rõ đánh đổi `power = 0,64` ở mức 5 điểm và 3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`.
- Lập `report/team/chi_so.md` (5 chỉ số, 11 event có `trace_id`, 4 dòng rủi ro kinh tế) và tổng hợp thành 1 trang `report/team/ho_so_launch_v0.md` với đề xuất **Go có điều kiện**.

## 4. Bằng chứng

- File code: `src/lab13.py` (chạy `python lab13.py` trong `src/` in `Ba phép thử đáp án biết trước: ĐẠT` và các bảng đối chiếu khớp `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`).
- Các file hồ sơ trong `report/team/`: `bang_chi_phi.md`, `pilot_plan.yaml` (đọc hợp lệ bằng `yaml.safe_load`, 0 dấu `?` ngoài chú thích), `chi_so.md`, `ho_so_launch_v0.md`, `group_report.md`, `bang_loi.md`.

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý AI (Antigravity) để đọc tổng hợp yêu cầu từ các file `.md`, rà soát rubric, kiểm tra hợp lệ YAML/quy tắc nhãn `simulated` và quy tắc 5 của `README.md`, hỗ trợ định dạng bảng và file báo cáo.
- Cách tự kiểm tra: trực tiếp chạy `src/.venv/Scripts/python.exe lab13.py` để đối chiếu từng con số với bảng đáp án trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; chạy `yaml.safe_load` kiểm tra `pilot_plan.yaml`; chạy kiểm tra không dùng từ cấm theo quy tắc 5 của `README.md` và không để AI bịa nhãn lỗi trong `bang_loi.md` hay kết quả duyệt chéo trong `phieu_cham.md`.

## 6. Tự đánh giá

- Hoàn thành cả 5 nhiệm vụ A, B, C, D, E (định lượng, gắn nhãn 20 ca lỗi theo khung Google PAIR, đặc tả chỉ số và thiết kế pilot), khớp số đối chiếu và đáp ứng đầy đủ các ràng buộc của rubric; phần duyệt chéo (`phieu_cham.md`) chờ ghép nhóm hoặc ghi nhận trạng thái làm cá nhân.
