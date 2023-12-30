i = (input("Mời nhập mã: "))
if len(i) == 6:
    print("Mã zip code hợp lệ")
elif len(i) != 6:
    print("Mã zipcode không hợp lệ")
elif not i.isdigit():
    print("Mã zipcode không hợp lệ")