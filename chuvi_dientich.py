# Code lab 6 bài 1 ở đây


class ChuNhat:
    def __init__(self, rong, dai):
        self.rong = rong
        self.dai = dai

    def get_chu_vi(self):
        return (self.rong + self.dai) * 2

    def get_dien_tich(self):
        return self.rong * self.dai

    def xuat(self):
        print(f"--- Hình Chữ Nhật ---")
        print(f"Chiều rộng: {self.rong}")
        print(f"Chiều dài: {self.dai}")
        print(f"Diện tích: {self.get_dien_tich()}")
        print(f"Chu vi: {self.get_chu_vi()}")


class Vuong(ChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)

    def xuat(self):
        print(f"Hình Vuông")
        print(f"Cạnh: {self.rong}")
        print(f"Diện tích: {self.get_dien_tich()}")
        print(f"Chu vi: {self.get_chu_vi()}")