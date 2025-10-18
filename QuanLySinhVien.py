import SinhVienPoly as svpl

class QuanLySinhVien:
    # khởi tạo danh sách sinh viên ban đầu rỗngg
    def __init__(self):
        self.dssv = []
        
    # phương thức nhập danh sách sinh viên
    def nhap_danh_sach_sinh_vien(self):
        while True:
            ho_ten_sv = input("Nhập họ tên sinh viên:")
            nganh_hoc = input("Nhập ngành học sinh viên")
            if nganh_hoc.lower() == "it":
                java = float(input("Điểm java:"))
                html = float(input("điểm html:"))
                css = float(input("điểm css:"))
                sv = svpl.SinhVienIT(ho_ten_sv, nganh_hoc, java, html, css)
                self.dssv.append(sv)
            elif nganh_hoc.lower() == "biz":
                marketing = float(input("Điểm marketing:"))
                sales = float(input("Điểm sales:"))
                sv = svpl.SinhVienBiz(ho_ten_sv, nganh_hoc, marketing, sales)
                self.dssv.append(sv)
            elif nganh_hoc.lower() == "exit":
                print("Kết thúc nhập tt sinh viên")
                break
            else:
                print("Nhập chưa đúng yêu cầu!")
        return self.dssv

    def Xuat_danh_sach_sinh_vien(self):
        if not self.dssv: 
            print("Danh sách viên rỗng!")
        else:
            print(f'{"Tên Sinh viên"},{"Ngành Học"},{"Điểm"},{"Học Lực"}')
            for sv in self.dssv:
                sv.xuat()

    def xuat_dssv_gioi(self):
        if not self.dssv:
            print("Danh sách viên rỗng!")
        else:
            print("Danh sách sinh viên học lực giỏi!")
            dssv_gioi = [sv for sv in self.dssv if sv.get_hoc_luc() == "Giỏi"]
            print(f'{"Tên Sinh viên":<20} {"Ngành Học":<10} {"Điểm":<10} {"Học lực":<10}')
            for sv in dssv_gioi:
                sv.xuat()

    def sap_xep_dssv(self):
        if not self.dssv:
            print("Danh sách viên rỗng!")

        print("Danh sách sinh viên điểm số tăng dần")
        dssv_sapxep = sorted(self.dssv, key = lambda z : z.get_diem())
        print(f'{"Tên Sinh viên":<20} {"Ngành Học":<10} {"Điểm":<10} {"Học lực":<10}')
        for sv in dssv_sapxep:
            sv.xuat()