def kt_so_nguyen_to(x):
    if x <= 1:
        return False
    elif x % 2== 0:
        return False
    elif x == 2:
        return True
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


x = int(input("Mời nhập số cần kiểm tra: "))
if kt_so_nguyen_to(x):
    print(x,": là 1 số nguyên tố")
else:
    print(x,": không phải là 1 số nguyên tố")
