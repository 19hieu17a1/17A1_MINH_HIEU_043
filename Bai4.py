def tinh_S(n,x):
    S = (x*x + 1)**n
    return S
    


x = int(input("Mời nhập x: "))
n = int(input("Mời nhập y: "))
print("Kết quả của S là: ",tinh_S(n,x))