Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lai_suat_1_nam = input("Lãi suất 1 năm (%): ")
Lãi suất 1 năm (%): 5.3
>>> so_tien_gui = input("Số tiền gửi: ")
Số tiền gửi: 5000000
>>> so_thang_gui = input("Số tháng gửi: ")
Số tháng gửi: 7
>>> tien_lai = (int(so_tien_gui)*int(so_thang_gui)*(float(lai_suat_1_nam)/12))
>>> print("Tiền lãi: ", tien_lai)
Tiền lãi:  15458333.333333332
>>> tong_so_tien = int(so_tien_gui) + float(tien_lai)
>>> print("Tổng số tiền: ", tong_so_tien)
Tổng số tiền:  20458333.333333332
