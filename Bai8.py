def kt_so_hoan_hao(n):
    if n <= 1:
        return False
    tong_uoc = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            tong_uoc += i
            if i != n // i:
                tong_uoc += n // i
    return tong_uoc == n

n = int(input("Mời nhập n: "))
if kt_so_hoan_hao(n):
    print(n,": Là 1 số hoàn hảo")
else: 
    print(n,": Không phải là số hoàn hảo")
