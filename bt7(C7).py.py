a = 500000
b = 200000
c = 100000
d = 50000
so_tien_muon_doi = 1375000
print("Số tiền muốn đổi:", so_tien_muon_doi)
so_to_500000 = (so_tien_muon_doi // a)
print("Số tờ 500000: ", so_to_500000)
so_tien_con_lai = (so_tien_muon_doi % a)
so_to_200000 = (so_tien_con_lai // b)
print("Số tờ 200000: ", so_to_200000)
so_tien_con_lai = (so_tien_con_lai % b)
so_to_100000 = (so_tien_con_lai // c)
print("Số tờ 100000: ", so_to_100000)
so_tien_con_lai = (so_tien_con_lai % c)
so_to_50000 = (so_tien_con_lai // d)
print("Số tờ 50000: ", so_to_50000)
so_tien_con_lai = (so_tien_con_lai % d)
print("Số tiền còn lại: ", so_tien_con_lai)

