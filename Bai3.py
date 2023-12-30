def tinh_chi_so_bmi(can_nang,chieu_cao):
    bmi = can_nang / (chieu_cao ** 2)
    print(bmi)
    if bmi < 18.5:
        print("Gầy")
    elif bmi >18.5 and bmi < 24.99:
        print("Bình thường")
    elif bmi >= 25:
        print("Thừa cân")

can_nang = float(input("Mời nhập chỉ số cân nặng: "))
chieu_cao = float(input("Mời nhập chỉ số chiều cao: "))
tinh_chi_so_bmi(can_nang, chieu_cao)