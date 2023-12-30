import math
while True:
    a = int(input("Mời nhập a: "))
    b = int(input("Mời nhập b: "))
    c = int(input("Mời nhập c: "))
    delta = b*b - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("2 nghiệm phân biệt là: X1 = ",x1, "và: x2 = ",x2)
    elif delta == 0:
        x3 = -((b)/(2*a))
        print("nghiệm kép là", x3)
    elif delta < 0:
        print("Phương trình vô nghiệm")
