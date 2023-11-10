a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
print("Phương trình: ", a, "*x", "+", b, "=0")
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b/a
    print("Nghiệm của x = ", x)