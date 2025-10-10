# ================== QUẢN LÝ NHÂN VIÊN (asm.py) ==================
# Chạy được bằng: python asm.py
# Hoặc import từ Jupyter: from asm import menu_nhanvien; menu_nhanvien()

import json
from dataclasses import dataclass, asdict
from typing import List, Optional
from pathlib import Path

# --- Định vị file dữ liệu (nhanvien.json) cùng thư mục với asm.py hoặc notebook ---
try:
    BASE_DIR = Path(__file__).parent
except NameError:
    # Trường hợp chạy trong Jupyter, __file__ không có -> dùng thư mục hiện hành
    BASE_DIR = Path.cwd()
DATA_FILE = BASE_DIR / "nhanvien.json"

# ---------- Model ----------
@dataclass
class NhanVien:
    ma: str
    ho_ten: str
    luong_co_ban: float
    thuong: float = 0.0
    phat: float = 0.0

    @property
    def thu_nhap(self) -> float:
        return self.luong_co_ban + self.thuong - self.phat

# ---------- IO ----------
def load_ds() -> List[NhanVien]:
    if not DATA_FILE.exists():
        return []
    try:
        raw = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return [NhanVien(**nv) for nv in raw]
    except json.JSONDecodeError:
        print("File dữ liệu hỏng/không đúng định dạng. Khởi tạo danh sách rỗng.")
        return []

def save_ds(ds: List[NhanVien]) -> None:
    DATA_FILE.write_text(
        json.dumps([asdict(nv) for nv in ds], ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

# ---------- Helpers ----------
def fmt(v: float) -> str:
    return f"{v:,.0f}".replace(",", ".")

def find_by_ma(ds: List[NhanVien], ma: str) -> Optional[NhanVien]:
    for nv in ds:
        if nv.ma.lower() == ma.lower():
            return nv
    return None

def nhap_float(prompt: str) -> float:
    while True:
        s = input(prompt).strip().replace(",", "")
        try:
            return float(s)
        except ValueError:
            print("  ❗ Vui lòng nhập số.")

# ---------- Y1 ----------
def y1_nhap_luu(ds: List[NhanVien]) -> None:
    print("\nNhập danh sách nhân viên (bỏ trống MÃ để kết thúc):")
    while True:
        ma = input("  Mã NV: ").strip()
        if ma == "":
            break
        if find_by_ma(ds, ma):
            print("  ❗ Mã đã tồn tại, nhập mã khác.")
            continue
        ho_ten = input("  Họ tên: ").strip()
        luong = nhap_float("  Lương cơ bản: ")
        thuong = nhap_float("  Thưởng (0 nếu không): ")
        phat = nhap_float("  Phạt (0 nếu không): ")
        ds.append(NhanVien(ma, ho_ten, luong, thuong, phat))
        print(f"  ✅ Đã thêm {ho_ten} (Mã {ma}).")
    save_ds(ds)
    print("💾 Đã lưu vào file.")

# ---------- Y2 ----------
def y2_xuat(ds: List[NhanVien]) -> None:
    if not ds:
        print("\nDanh sách rỗng.")
        return
    print("\n===== DANH SÁCH NHÂN VIÊN =====")
    print(f"{'MÃ':<10}{'HỌ TÊN':<28}{'LƯƠNG':>12}{'THƯỞNG':>12}{'PHẠT':>12}{'THU NHẬP':>14}")
    for nv in ds:
        print(f"{nv.ma:<10}{nv.ho_ten:<28}{fmt(nv.luong_co_ban):>12}{fmt(nv.thuong):>12}{fmt(nv.phat):>12}{fmt(nv.thu_nhap):>14}")

# ---------- Y3 ----------
def y3_tim_ma(ds: List[NhanVien]) -> None:
    ma = input("Nhập mã cần tìm: ").strip()
    nv = find_by_ma(ds, ma)
    if nv:
        print(f"  ✅ {nv.ma} - {nv.ho_ten} | Lương: {fmt(nv.luong_co_ban)} | Thu nhập: {fmt(nv.thu_nhap)}")
    else:
        print("  ❌ Không tìm thấy.")

# ---------- Y4 ----------
def y4_xoa(ds: List[NhanVien]) -> None:
    ma = input("Nhập mã cần xóa: ").strip()
    nv = find_by_ma(ds, ma)
    if not nv:
        print("  ❌ Không tìm thấy.")
        return
    ds.remove(nv)
    save_ds(ds)
    print(f"  🗑️ Đã xóa {nv.ho_ten} (Mã {nv.ma}) và cập nhật file.")

# ---------- Y5 ----------
def y5_cap_nhat(ds: List[NhanVien]) -> None:
    ma = input("Nhập mã cần cập nhật: ").strip()
    nv = find_by_ma(ds, ma)
    if not nv:
        print("  ❌ Không tìm thấy.")
        return
    print("Để trống nếu muốn giữ nguyên.")
    ho_ten = input(f"  Họ tên [{nv.ho_ten}]: ").strip() or nv.ho_ten
    s = input(f"  Lương cơ bản [{nv.luong_co_ban}]: ").strip()
    if s != "": nv.luong_co_ban = float(s.replace(",", ""))
    s = input(f"  Thưởng [{nv.thuong}]: ").strip()
    if s != "": nv.thuong = float(s.replace(",", ""))
    s = input(f"  Phạt [{nv.phat}]: ").strip()
    if s != "": nv.phat = float(s.replace(",", ""))
    nv.ho_ten = ho_ten
    save_ds(ds)
    print("  ✅ Đã cập nhật và ghi file.")

# ---------- Y6 ----------
def y6_tim_khoang_luong(ds: List[NhanVien]) -> None:
    a = nhap_float("Lương tối thiểu: ")
    b = nhap_float("Lương tối đa: ")
    if a > b: a, b = b, a
    kq = [nv for nv in ds if a <= nv.luong_co_ban <= b]
    if not kq:
        print("  ❌ Không có nhân viên nào trong khoảng.")
        return
    print(f"\nNhân viên có lương cơ bản trong [{fmt(a)} .. {fmt(b)}]:")
    for nv in kq:
        print(f"  - {nv.ma:<8} {nv.ho_ten:<28} Lương: {fmt(nv.luong_co_ban)} | Thu nhập: {fmt(nv.thu_nhap)}")

# ---------- Y7 ----------
def y7_sort_theo_ho_ten(ds: List[NhanVien]) -> None:
    def key_name(nv: NhanVien):
        parts = nv.ho_ten.strip().split()
        ho = " ".join(parts[:-1]) if len(parts) > 1 else parts[0]
        ten = parts[-1]
        return (ten.lower(), ho.lower())
    ds.sort(key=key_name)
    save_ds(ds)
    print("  ✅ Đã sắp xếp theo HỌ TÊN (và lưu file).")

# ---------- Y8 ----------
def y8_sort_thu_nhap(ds: List[NhanVien]) -> None:
    ds.sort(key=lambda nv: nv.thu_nhap)
    save_ds(ds)
    print("  ✅ Đã sắp xếp tăng dần theo THU NHẬP (và lưu file).")

# ---------- Y9 ----------
def y9_top5(ds: List[NhanVien]) -> None:
    if not ds:
        print("Danh sách rỗng.")
        return
    top = sorted(ds, key=lambda nv: nv.thu_nhap, reverse=True)[:5]
    print("\nTOP 5 THU NHẬP CAO NHẤT:")
    for i, nv in enumerate(top, 1):
        print(f"{i}. {nv.ma:<8} {nv.ho_ten:<28} Thu nhập: {fmt(nv.thu_nhap)}")

# ---------- MENU (gọi được từ file khác) ----------
def menu_nhanvien():
    ds = load_ds()
    while True:
        print("""
======  QUẢN LÝ NHÂN VIÊN ======
Y1. Nhập & lưu danh sách
Y2. Đọc & xuất danh sách
Y3. Tìm theo MÃ
Y4. Xóa theo MÃ (cập nhật file)
Y5. Cập nhật theo MÃ (ghi file)
Y6. Tìm theo KHOẢNG LƯƠNG CƠ BẢN
Y7. Sắp xếp theo HỌ TÊN
Y8. Sắp xếp theo THU NHẬP
Y9. Top 5 THU NHẬP cao nhất
q. Thoát
""")
        ccc = input("Chọn chức năng: ").strip().lower()
        if ccc == "q":
            print("Tạm biệt!")
            break
        match ccc:
            case "y1": y1_nhap_luu(ds)
            case "y2": y2_xuat(ds)
            case "y3": y3_tim_ma(ds)
            case "y4": y4_xoa(ds)
            case "y5": y5_cap_nhat(ds)
            case "y6": y6_tim_khoang_luong(ds)
            case "y7": y7_sort_theo_ho_ten(ds)
            case "y8": y8_sort_thu_nhap(ds)
            case "y9": y9_top5(ds)
            case _:    print("❗ Chọn Y1..Y9 hoặc q để thoát.")

# Cho phép chạy trực tiếp file asm.py
if __name__ == "__main__":
    menu_nhanvien()
