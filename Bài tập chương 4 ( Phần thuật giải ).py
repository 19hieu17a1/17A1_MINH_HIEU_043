Câu 1: VIết thuật giải nhập 1 số từ bàn phím và in ra bình phương của số đó nếu số đó
là số dương.
# Nhập một số từ bàn phím
so = float(input("Nhập một số: "))

# Kiểm tra xem số đó có phải là số dương hay không
if so > 0:
    # Tính bình phương của số và in ra
    binh_phuong = so**2
    print(f"Bình phương của {so} là {binh_phuong}")
else:
    print(f"{so} không phải là số dương.")
    
Câu 2: Viết thuật giải nhập từ bàn phím một số tự nhiên N và in ra các số nguyên
trong phạm vi từ 1 đến N.
# Nhập số tự nhiên N từ bàn phím
N = int(input("Nhập một số tự nhiên N: "))

# Kiểm tra xem N có phải là số tự nhiên không âm
if N < 1:
    print("N phải là một số tự nhiên không âm.")
else:
    # In ra các số nguyên từ 1 đến N
    for i in range(1, N + 1):
        print(i)
        
Câu 3: Viết thuật giải nhập vào từ bàn phím 2 số tự nhiên m,n(m<n) và in ra màn hình
hình các số chia hết cho m trong khoảng từ 1 đến n.
# Nhập hai số tự nhiên m và n từ bàn phím
m = int(input("Nhập số tự nhiên m: "))
n = int(input("Nhập số tự nhiên n (n lớn hơn m): "))

# Kiểm tra xem m và n có phù hợp
if m >= n:
    print("Vui lòng nhập n lớn hơn m.")
else:
    # In ra các số chia hết cho m trong khoảng từ 1 đến n
    for i in range(1, n + 1):
        if i % m == 0:
            print(i)

Câu 4: Viết thuật giải nhập 3 số từ bàn phím và in ra số lớn nhất trong 3 số đó.
so1 = float(input("Nhập số thứ nhất: "))
so2 = float(input("Nhập số thứ hai: "))
so3 = float(input("Nhập số thứ ba: "))

# Tìm số lớn nhất trong 3 số
so_lon_nhat = max(so1, so2, so3)

# In ra số lớn nhất
print("Số lớn nhất trong ba số là:", so_lon_nhat)

Câu 5: Viết thuật giải nhập 2 số từ bàn phím và in ra BCNN của 2 số đó.
# Hàm tính UCLN (Ước chung lớn nhất)
def UCLN(a, b):
    while b:
        a, b = b, a % b
    return a

# Nhập hai số từ bàn phím
so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))

# Tính BCNN sử dụng công thức
bcnn = (so1 * so2) // UCLN(so1, so2)

# In ra BCNN của hai số
print("BCNN của", so1, "và", so2, "là:", bcnn)

Câu 6: Biểu diễn giải thuật giải các bài toán sau bằng sơ đồ khối và giải mã:
  - Giải hệ phương trình bậc nhất
  
    1. Bắt đầu.
    2. Nhập hệ số a, b và hằng số c từ người dùng.
    3. Tính giá trị của x bằng cách sử dụng công thức x = (c - b) / a.
    4.In ra giá trị của x là nghiệm của phương trình.
    5. Kết thúc.
    
  - Tính số ngày của 1 tháng trong năm nào đó.
    1. Bắt đầu.
    2. Nhập tháng và năm từ người dùng.
    3. Kiểm tra xem tháng có phải là tháng 1, 3, 5, 7, 8, 10 hoặc 12 (có 31 ngày) hay không.
       Nếu đúng, in ra "Tháng này có 31 ngày."
    4. Kiểm tra xem tháng có phải là tháng 4, 6, 9 hoặc 11 (có 30 ngày) hay không.
       Nếu đúng, in ra "Tháng này có 30 ngày."
    5. Kiểm tra xem tháng có phải là tháng 2 (có 28 hoặc 29 ngày) hay không.
       Nếu đúng, kiểm tra xem năm đó là năm nhuận hay không.
       Nếu là năm nhuận, in ra "Tháng 2 có 29 ngày."
       Nếu không phải là năm nhuận, in ra "Tháng 2 có 28 ngày."
    6. Kết thúc.

  - Giải thuật tìm số ước chung lớn nhất(UCLN)
    1. Bắt đầu.
    2. Nhập hai số a và b từ người dùng.
    3.Lặp cho đến khi bằng 0:
       a. Gán a = b.
       b. Gán b = a % b.
    4. In ra giá trị của a là ước số chung lớn nhất (UCLN) của a và b.
    5. Kết thúc.
Câu 7: Hãy xây dựng giải thuật để tính tổng các chữ số của một số nguyên N bất kỳ.
def tinh_tong_chu_so(N):
    # Khởi tạo biến tổng
    tong = 0
    
    # Chuyển số N thành một chuỗi để dễ dàng trích xuất từng chữ số
    chuoi_N = str(N)
    
    # Lặp qua từng chữ số trong chuỗi
    for chu_so in chuoi_N:
        # Chuyển chữ số thành số nguyên và cộng vào biến tổng
        tong += int(chu_so)
    
    return tong

  
    

