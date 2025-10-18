# =========================
# Module cho LAB4
# =========================

# Bài 1: Tính tiền nước sinh hoạt
gia_ban_nuoc = (7500, 8800, 12000, 24000)  # theo m3 cho từng bậc

def tinh_tien_nuoc(san_luong: int) -> int:
    """Tính tiền nước theo bậc thang."""
    tien = 0
    if san_luong <= 10:
        tien = san_luong * gia_ban_nuoc[0]
    elif san_luong <= 20:
        tien = 10 * gia_ban_nuoc[0] + (san_luong - 10) * gia_ban_nuoc[1]
    elif san_luong <= 30:
        tien = (10 * gia_ban_nuoc[0] +
                10 * gia_ban_nuoc[1] +
                (san_luong - 20) * gia_ban_nuoc[2])
    else:
        tien = (10 * gia_ban_nuoc[0] +
                10 * gia_ban_nuoc[1] +
                10 * gia_ban_nuoc[2] +
                (san_luong - 30) * gia_ban_nuoc[3])
    return tien


# Bài 2: Tính nguyên liệu làm bánh (đường, đậu) theo kg
# Cấu trúc từng tuple: (đường, đậu)
banh_dau_xanh = (0.04, 0.07)
banh_thap_cam = (0.06, 0.07)
banh_deo      = (0.05, 0.02)

def tinh_nguyen_lieu(so_dau_xanh: int, so_thap_cam: int, so_deo: int) -> dict:
    """Tính tổng lượng đường/đậu (kg) cần cho hộp bánh."""
    duong = (so_dau_xanh * banh_dau_xanh[0] +
             so_thap_cam * banh_thap_cam[0] +
             so_deo * banh_deo[0])

    dau = (so_dau_xanh * banh_dau_xanh[1] +
           so_thap_cam * banh_thap_cam[1] +
           so_deo * banh_deo[1])

    return {"đậu": dau, "đường": duong}


# Bài 3: Lọc số chẵn trong dãy số nguyên
def nhap_day_so() -> list[int]:
    """Nhập dãy số nguyên từ bàn phím, gõ 's' để dừng."""
    my_list = []
    print("Nhập dãy số nguyên (gõ 's' hoặc 'S' để dừng):")
    while True:
        n = input("Nhập số: ")
        if n.lower() == 's':
            break
        try:
            my_list.append(int(n))
        except ValueError:
            print("Lỗi: Bạn phải nhập số nguyên!")
    return my_list

def loc_so_chan(ds: list[int]) -> list[int]:
    """Trả về danh sách các số chẵn trong ds."""
    return list(filter(lambda x: x % 2 == 0, ds))
