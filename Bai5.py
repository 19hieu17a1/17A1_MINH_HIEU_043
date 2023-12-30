my_list = []
while True:
    nhap_phan_tu = input("Mời nhập phần tử (ấn x để kết thúc): ")
    if nhap_phan_tu.lower() == "x":
        break
    my_list.append(nhap_phan_tu)
    print(my_list)
    def kiem_tra_so_nguyen_to(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    def in_so_nguyen_to_trong_list(my_list):
        so_nguyen_to = [x for x in my_list if kiem_tra_so_nguyen_to(x)]
        print("Các số nguyên tố trong danh sách:", so_nguyen_to)
        print(in_so_nguyen_to_trong_list(my_list))
