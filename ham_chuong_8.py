import math
#HÀM TÌM SỐ NHỎ NHẤT VÀ LỚN NHẤT
def tim_max_min(x):
    print("số lớn nhất là: ", max(x))
    print("Số nhỏ nhất là: ", min(x))



#HÀM TÌM GIÁ TRỊ TUYỆT ĐỐI CỦA X
def tim_gia_tri_tuyet_doi(x):
    print("Giá trị tuyệt đối của x là: ",abs(x))




#HÀM GIẢI PT BẬC NHẤT: ax + b = 0
def giai_pt_bac_1(a,b):
    if a == 0:
        if b == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -b / a
        print("Nghiệm là: ",x)
    


#HÀM TÍNH DIỆN TÍCH TAM GIÁC THEO CÔNG THỨC HERON
def tinh_dien_tich_tam_giac(a,b,c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("Diện tích tam giác là", s)
    



#HÀM KIỂM TRA NĂM NHUẬN
def kt_nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return True
    else:
        return False
    


#HÀM COUNT DOWN 
def count_down(x):
    while n <= 10:
        print(n)
        n-=1
        if n == 0:
            break
    print("Start!!!")



#HÀM TÍNH BIỂU THỨC S
def tinh_bieu_thuc_S(n,x):
    S = (x*x + 1)**n
    print("Biểu thức S là: ",S)




#HÀM TÍNH BIỂU THỨC A
def tinh_bieu_thuc_A (x,n):
    A = (pow(x,2)+x + 1)**n + (pow(x,2) - x + 1)**n
    print("Biểu thức A là: ",A)



#HÀM KIỂM TRA SỐ NGUYÊN TỐ
def kt_so_nguyen_to(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


#HÀM TÍNH TỔNG N SÓ NGUYÊN NHẬP VÀO
def tinh_tong_so_nguyen_n(a,b,c):
    S = a + b + c
    print("Tổng các số nguyên là: ",S)

#HÀM KIỂM TRA SỐ HOÀN HẢO
def kt_so_hoan_hao(number):
    if number <= 0:
        return False

    divisor_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisor_sum == number

#HÀM TÌM ƯCLN
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)













