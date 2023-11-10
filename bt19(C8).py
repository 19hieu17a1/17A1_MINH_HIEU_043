n = int(input("Nhập số lượng phần tử của dãy số:"))
day_so = list(range(1, n + 1))
print("Dãy số ban đầu: ", day_so)
dao_nguoc_day_so = list(reversed(day_so))
print("Dãy số sau khi đã đảo ngược: ", dao_nguoc_day_so)
print("Các số lẻ trong dãy số đã đảo ngược: ")
for y in dao_nguoc_day_so:
    if y % 2!= 0:
        print(y)