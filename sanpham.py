class sampham: 
    def __init__(self, tensp, giamgiasp, giasp):
        self.giasp = giasp
        self.tensp = tensp
        self.giamgiasp = giamgiasp
        #self.__giamgiasp = giamgiasp

    # def DocGiamGia(self):
    #     return self.__giamgiasp)
        
    def thuenhapkhau(self):
        return self.giasp * 0.1
    
    def nhap_thong_tin_sp(self):
        self.tensp = input("Nhập tên sản phẩm: ")
        self.giasp = float(input("Nhập giá sản phẩm: "))
        self.giamgiasp = float(input("Nhập giảm giá sản phẩm: "))
    def xuat_thong_tin_sp(self):
        print(f"Sản Phẩm {self.tensp} Giá: {self.giasp} Giảm giá: {self.giamgiasp} Thuế nhập khẩu: {self.thuenhapkhau()}")
       # def __str__(self):
    #     return f"Sản Phẩm{self.ten_sp} Giá: {self.gia} Giảm giá: {self.__giam_gia} Thuế nhập khẩu: {self.thue_nhap_khau()}"


    
    # def xuat_thong_tin_sp(self):
    #     print(f"Tên sản phẩm là {self.tensp} có giá sản phẩm là {self.giasp} được giảm giá {self.giamgiasp} và thuế nhập khẩu là {self.thuenhapkhau()} và tổng giá sau thuế {self.giasp + self.thuenhapkhau()}")


# print(sp1.DocGiamGia())

#print(f" tên sản phấm {sp1.tensp} giá sản phẩm {sp1.giasp} giảm giá sản phẩm {sp1.__giamgiasp} thuế nhập khẩu {sp1.thuenhapkhau()} tổng giá sau thuế {sp1.giasp + sp1.thuenhapkhau()}" )
# sp1.xuat_thong_tin_sp()
