a = float(input("Cạnh a của tam giác: "))
b = float(input("Cạnh b của tam giác: "))
c = float(input("Cạnh c của tam giác: "))
p = (a+b+c)/2
s = (p*(p-a)*(p-b)*(p-c))
can_bac_2 = 1/2
S = s**(can_bac_2)
print("Diện tích tam giác là: ", S)
