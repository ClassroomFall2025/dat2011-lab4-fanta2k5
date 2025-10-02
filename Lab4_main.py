import Lab4_module as m

def menu():
    print("""
+----------------------------------+
| 1. Tính tiền nước sinh hoạt      |
| 2. Tính nguyên liệu làm bánh     |
| 3. Lọc số chẵn trong dãy số      |
| 0. Kết thúc                      |
+----------------------------------+
""")

while True:
    menu()
    chon = input("Chọn chức năng (0-3): ").strip()

    if chon not in {'0','1','2','3'}:
        print("❌ Lỗi: Vui lòng nhập số từ 0 đến 3!\n")
        continue

    if chon == '0':
        print("👋 Tạm biệt!")
        break

    if chon == '1':
        try:
            sl = int(input("Nhập sản lượng nước (m³): "))
            if sl < 0:
                raise ValueError
        except ValueError:
            print("❌ Sản lượng phải là số nguyên không âm!\n")
            continue
        tien = m.tinh_tien_nuoc(sl)
        print(f"💧 Tiền nước phải trả: {tien:,} đồng\n")

    elif chon == '2':
        try:
            dx = int(input("Số bánh đậu xanh: "))
            tc = int(input("Số bánh thập cẩm: "))
            deo = int(input("Số bánh dẻo: "))
            if min(dx, tc, deo) < 0:
                raise ValueError
        except ValueError:
            print("❌ Số lượng bánh phải là số nguyên không âm!\n")
            continue
        kq = m.tinh_nguyen_lieu(dx, tc, deo)
        print("🍞 Nguyên liệu cần (kg):")
        print(f"- Đường: {kq['đường']:.2f} kg")
        print(f"- Đậu  : {kq['đậu']:.2f} kg\n")

    elif chon == '3':
        ds = m.nhap_day_so()
        chan = m.loc_so_chan(ds)
        print("📦 Dãy số ban đầu:", ds)
        print("✅ Các số chẵn   :", chan, "\n")
