class sinhvien:
    #các thuộc tính 
    # ten_sv = ""
    # nam_sinh = ""
    # diem = ""

    #các phương thức
    def __init__(self, ten_sv, nam_sinh, diem, hoclaptrinh):
        self.ten_sv = ten_sv
        self.nam_sinh = nam_sinh
        self.diem = diem
        self.hoclaptrinh = hoclaptrinh
    def hien_sv(self):
        print(f"Tên sinh viên: {self.ten_sv}")
        print(f"Năm sinh: {self.nam_sinh}")
        print(f"Điểm: {self.diem}")
        print(f"Học lập trình: {self.hoclaptrinh}")

    


# sv1 = sinhvien()
# sv1.them_sv("Nguyễn Văn A", "2000", "8.5")
# sv1.hien_sv()
class svxldl(sinhvien):
    def __init__(self, ten_sv, nam_sinh, diem, hoclaptrinh):
        super().__init__(ten_sv, nam_sinh, diem)
        self.hoclaptrinh = hoclaptrinh



    def __str__(self):
        return f"{super().__str__()} và học lập trình {self.hoclaptrinh}"
    
    sv1 = svxldl("Nguyen Van A", 2000, 8.5, "Co")
    sv1.hien_sv()