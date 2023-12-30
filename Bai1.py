try:
    while True:
        a = float(input("Mời nhập cạnh a: "))
        if a <= 0:
            print("Giá trị nhập vào không hợp lệ")  
            break
        b = float(input("Mời nhập cạnh b: "))
        if b <= 0:
            print("Giá trị nhập vào không hợp lệ")
        c = float(input("Mời nhập cạnh c: "))
        if c <= 0:
            print("Giá trị nhập vào không hợp lệ")
        elif c < a + b:
            print("Sai điều kiện")
except:
    print("Nhập sai giá trị")
    