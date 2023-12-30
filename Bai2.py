try:
    while True:
            list_n = []
            n = int(input("Nhập số nguyên dương: "))
            if n == 0:
                break
            elif n < 0:
                raise ValueError ("Lỗi số âm!!!!!!")
            elif not n % 2:
                 raise ValueError ("lỗi nhập chẵn !!!")
            if len(list_n) >= 4 and list_n[-4:] == [n,n,n,n]:
                 raise ValueError ("Lỗi nhập lặp lại !!!")
            list_n.append(n)
            
            
except ValueError as a:
    print(a)
    print(list_n)