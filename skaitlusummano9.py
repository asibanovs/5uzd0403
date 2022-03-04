a = int(input("Līdz kuram skaitlim: "))
b = 0
for i in range(9, a+1):
 b = i + b
if a<9:
  print("Error")
else:
 print("Summa ir",b)