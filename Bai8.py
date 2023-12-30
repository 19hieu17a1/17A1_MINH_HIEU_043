def kiem_tra_may_man(danh_sach):
    return any(so % 7 == 0 for so in danh_sach)

# Ví dụ sử dụng
danh_sach_so = [15, 21, 30, 42, 50]

if kiem_tra_may_man(danh_sach_so):
    print("Danh sách là may mắn.")
else:
    print("Danh sách không may mắn.")
