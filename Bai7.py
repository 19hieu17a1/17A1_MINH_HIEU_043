def phan_nguyen_phep_chia(a, b):
    if b == 0:
        raise ValueError
    return( a // b)
       

so_chia = int(input("mời nhập số chia: "))
so_chia_cho = int(input("mời nhập số bị chia: "))
ket_qua = phan_nguyen_phep_chia(so_chia, so_chia_cho)
print("Phần nguyên của", so_chia, "chia cho", so_chia_cho, "là: ",ket_qua)