"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
from statistics import NormalDist

import pandas as pd

try:  # in được tiếng Việt trên console Windows
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000   # chi phí cố định của trợ lý mỗi tháng
YC_THANG = 45_000            # số yêu cầu hoàn phí mỗi tháng ở quy mô đầy đủ
PHAM_VI = ['noi_dia', 'hang_nang']


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')
    print(f'  so_lan_chay_ky_vong(0.8, 2)               = {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'  so_lan_chay_ky_vong(0.8)                  = {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'  he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) = {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # Bỏ các lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn coi như chuyển nhân viên.
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (công thức z, làm tròn lên)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    n = (za * math.sqrt(2 * pb * (1 - pb))
         + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2
    return math.ceil(n)


def he_so_thiet_ke(m, icc):
    return 1 + (m - 1) * icc


def tieu_de(chu):
    print(f'\n=== {chu} ===')


def nhiem_vu_A(runs, reqs):
    # A2
    tieu_de('A2 · Mô hình chi phí từ trace (xem_lai, lam_lai, tong, cps: simulated)')
    a2 = mo_hinh(runs, reqs)
    for ten, gia_tri in a2.items():
        print(f'{ten:16s} {gia_tri:>14,.1f}')
    print(f'Số lần gọi tool: {runs.tool_calls.sum():,} · phút xem lại: {reqs.phut_xem_lai_simulated.sum():,}'
          f' · phút làm lại: {reqs.phut_lam_lai_simulated.sum():,}')
    print(f'cps / hoá đơn mỗi yêu cầu = {a2["cps"] / a2["hoa_don_moi_yc"]:.1f} lần')
    for k in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f'  tỉ trọng {k:8s} {a2[k] / a2["tong"] * 100:5.1f}%')
    print(f'  giờ nhân viên (xem lại + làm lại) {(a2["xem_lai"] + a2["lam_lai"]) / a2["tong"] * 100:.1f}%')
    khong_tc = len(reqs) - a2['thanh_cong']
    he_thong = (a2['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống / yêu cầu = ({a2["tong"]:,.0f} + {khong_tc} × 12.000) / {len(reqs)}'
          f' = {he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× [simulated]')
    print('Phân bố ket_qua:', reqs.ket_qua.value_counts().to_dict())

    # A3
    tieu_de('A3 · Tách theo loại yêu cầu (cps: simulated)')
    print(f'{"loai":10s} {"so_yc":>6s} {"ti_le_tc":>9s} {"lan/yc":>7s} {"cps":>9s} {"so_12k":>7s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs.loai == loai]
        kq = mo_hinh(runs, r)
        so_lan = runs.request_id.isin(r.request_id).sum() / len(r)
        print(f'{loai:10s} {len(r):6d} {kq["thanh_cong"] / len(r) * 100:8.1f}% {so_lan:7.2f}'
              f' {kq["cps"]:9,.0f} {kq["cps"] / BASELINE:6.2f}×')
    tl_ok = (runs.merge(reqs[['request_id', 'loai']], on='request_id')
             .assign(ok=lambda d: (d.status == 'ok').astype(float))
             .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    so_run = (runs.merge(reqs[['request_id', 'loai']], on='request_id')
              .pivot_table(index='loai', columns='attempt', values='run_id', aggfunc='count'))
    print('Tỉ lệ status == ok theo lần thử (%):')
    print((tl_ok * 100).round(1).to_string())
    print('Số lần chạy theo lần thử:')
    print(so_run.to_string())

    # A4
    tieu_de('A4 · Chi phí cố định, phạm vi noi_dia + hang_nang (simulated)')
    pv = reqs[reqs.loai.isin(PHAM_VI)]
    kq_pv = mo_hinh(runs, pv)
    print(f'Phạm vi: {len(pv)} yêu cầu, {kq_pv["thanh_cong"]} việc thành công, tổng {kq_pv["tong"]:,.0f} đ,'
          f' cps {kq_pv["cps"]:,.0f} đ')
    for nhan, he_so in [('45.000 yc/tháng', 1.0), ('Một nửa khối lượng', 0.5)]:
        tc_thang = YC_THANG * he_so * kq_pv['thanh_cong'] / len(reqs)
        co_dinh = CO_DINH_THANG / tc_thang
        tong_viec = kq_pv['cps'] + co_dinh
        print(f'{nhan:20s} việc TC/tháng {tc_thang:>9,.0f} · cố định/việc {co_dinh:>7,.0f} đ'
              f' · cps + cố định {tong_viec:>7,.0f} đ = {tong_viec / BASELINE:.2f}×')
    return a2


def nhiem_vu_B(runs, reqs):
    # B1
    tieu_de('B1 · Đổi từng yếu tố (simulated)')
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }
    goc = mo_hinh(runs, reqs)['cps']
    print(f'{"Gốc (A2)":30s} {goc:8,.0f}')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:30s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')

    # B2
    tieu_de('B2 · Đổi một cặp (simulated)')
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'Giá token × 2 và xem lại × 2: {cap:,.0f} đ ({(cap / goc - 1) * 100:+.1f}%)')

    # B3
    tieu_de('B3 · Giới hạn chạy lại và chi phí cả hệ thống (simulated)')
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        he_thong = kq['tong'] + khong_tc * BASELINE
        print(f'{k} lần: tổng trợ lý {kq["tong"]:>11,.0f} · không TC {khong_tc:4d} · cả hệ thống {he_thong:>11,.0f}'
              f' · cps {kq["cps"]:7,.0f}')

    # B4
    tieu_de('B4 · Xem lại 100% cho noi_dia + hang_nang (simulated)')
    pv = reqs[reqs.loai.isin(PHAM_VI)]
    runs_pv = runs[runs.request_id.isin(pv.request_id)]
    co_ok = runs_pv[runs_pv.status == 'ok'].request_id.nunique()
    so_lam_lai = int((pv.ket_qua == 'lam_lai').sum())
    tc = int((pv.ket_qua == 'thanh_cong').sum())
    token_tool = (runs_pv.tokens_in / 1000 * GIA_VAO + runs_pv.tokens_out / 1000 * GIA_RA
                  + runs_pv.tool_calls * GIA_TOOL).sum()
    phut_lam_lai_tb = reqs.loc[reqs.ket_qua == 'lam_lai', 'phut_lam_lai_simulated']
    print(f'{len(pv)} yêu cầu · {co_ok} có ít nhất 1 lần ok · {so_lam_lai} ca lam_lai · {tc} thành công'
          f' · token + tool {token_tool:,.0f} đ')
    for nhan, phut_ll in [('làm lại 9 phút (đề cho)', 9), (f'làm lại {phut_lam_lai_tb.mean():.1f} phút (TB dữ liệu)',
                                                            phut_lam_lai_tb.mean())]:
        xem = co_ok * 5 * LUONG_PHUT
        lam = so_lam_lai * phut_ll * LUONG_PHUT
        tong = xem + lam + token_tool
        hoa_von = (BASELINE * tc - token_tool - lam) / (co_ok * LUONG_PHUT)
        print(f'{nhan:32s} xem lại {xem:>10,.0f} · làm lại {lam:>10,.0f} · tổng {tong:>11,.0f}'
              f' · cps {tong / tc:7,.0f} đ = {tong / tc / BASELINE:.2f}× · hoà vốn khi xem lại ≤ {hoa_von:.1f} phút')
    print(f'Phút làm lại trên các ca lam_lai: TB {phut_lam_lai_tb.mean():.1f}, trung vị {phut_lam_lai_tb.median():.1f}')


def nhiem_vu_D(reqs):
    tieu_de('D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02)')
    icc = 0.02
    n_a = co_mau(0.70, 0.75)
    print(f'a) Chia theo yêu cầu: {n_a:,} yêu cầu mỗi nhóm')
    de_b = he_so_thiet_ke(75, icc)
    n_b = math.ceil(n_a * de_b)
    nv_b = math.ceil(n_b / 75)
    print(f'b) Theo nhân viên, m = 75: DE = {de_b:.2f}; n = {n_b:,} mỗi nhóm → {nv_b} nhân viên mỗi nhóm,'
          f' tổng {2 * nv_b} > 40 → không đủ người')
    print(f'c) 20 nhân viên mỗi nhóm: n hiệu dụng tối đa = 20 / {icc} = {20 / icc:,.0f} < {n_a:,} → không đạt')
    print(f'd) 6 depot mỗi nhóm: n hiệu dụng tối đa = 6 / {icc} = {6 / icc:,.0f}')
    n_e = co_mau(0.70, 0.76)
    m_e = math.ceil(n_e * (1 - icc) / (20 - n_e * icc))
    print(f'e) Mức chênh 6 điểm: {n_e} mỗi nhóm; 20 nhân viên → m ≥ {m_e} yêu cầu mỗi người'
          f' (DE {he_so_thiet_ke(m_e, icc):.2f}; n hiệu dụng {20 * m_e / he_so_thiet_ke(m_e, icc):.0f})')
    try:
        from statsmodels.stats.power import NormalIndPower
        from statsmodels.stats.proportion import proportion_effectsize
        es5 = proportion_effectsize(0.75, 0.70)
        print(f'   statsmodels, 5 điểm: n = {NormalIndPower().solve_power(es5, alpha=0.05, power=0.8):.0f} mỗi nhóm'
              f' (arcsine); power ở 5 điểm nếu n = {n_e}: {NormalIndPower().power(es5, nobs1=n_e, alpha=0.05):.2f}')
    except ImportError:
        print('   (chưa cài statsmodels: bỏ qua phần kiểm tra power)')

    tieu_de('D3 · Tỉ lệ mo_lai_trong_7_ngay hiện tại')
    pv = reqs[reqs.loai.isin(PHAM_VI)]
    print(f'Toàn mẫu: {reqs.mo_lai_trong_7_ngay.mean() * 100:.2f}% ({reqs.mo_lai_trong_7_ngay.sum()}/{len(reqs)})'
          f' · noi_dia + hang_nang: {pv.mo_lai_trong_7_ngay.mean() * 100:.2f}%'
          f' ({pv.mo_lai_trong_7_ngay.sum()}/{len(pv)})')
    print(f'Tỉ lệ lam_lai trong phạm vi: {(pv.ket_qua == "lam_lai").mean() * 100:.1f}%'
          f' · được xem lại trong phạm vi: {pv.duoc_xem_lai.mean() * 100:.1f}%')


def nhiem_vu_E(reqs):
    tieu_de('E1 · Ba chỉ số tính thử trên 1.200 yêu cầu')
    chinh = (reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0)
    xem = reqs[reqs.duoc_xem_lai == 1]
    bo_qua = xem.quyet_dinh_xem_lai.isin(['sua', 'bo'])
    an_toan = reqs.mo_lai_trong_7_ngay == 1
    print(f'Chính  : {chinh.mean() * 100:.2f}% ({chinh.sum()}/{len(reqs)})')
    print(f'Dùng   : {bo_qua.mean() * 100:.2f}% ({bo_qua.sum()}/{len(xem)})'
          f' · phân bố {xem.quyet_dinh_xem_lai.value_counts().to_dict()}')
    print(f'An toàn: {an_toan.mean() * 100:.2f}% ({an_toan.sum()}/{len(reqs)})')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    nhiem_vu_A(runs, reqs)   # CP1 · A2, A3, A4
    nhiem_vu_B(runs, reqs)   # CP2 · B1–B4
    nhiem_vu_D(reqs)         # CP4 · D1, tỉ lệ mở lại
    nhiem_vu_E(reqs)         # CP5 · E1
