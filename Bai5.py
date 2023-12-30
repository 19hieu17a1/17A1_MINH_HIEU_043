def tinh_A(n,x):
    A = (x*x + x + 1)**n + (x*x - x + 1)**n
    return A

n = int(input("Mời nhập n: "))
x = int(input("Mời nhập x: "))
print("kết quả A là: ", tinh_A(n,x))