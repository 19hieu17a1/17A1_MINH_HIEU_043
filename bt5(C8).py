year = int(input("Nhập năm: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Là năm nhuận")
else:
    print("ko là năm nhuận")
    