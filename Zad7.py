import math
A= int(input("Podaj liczbe A: "))
B= int(input("Podaj liczbe B: "))
#Dodawanie
hypot=math.hypot(A,B)
print("Suma wynosi")
Suma = A+B
print (Suma)
#Odejmowanie
Roznica = A-B
print ("Roznica wynosi")
print (Roznica)
#Iloczyn
Iloczyn = A * B
print ("Iloczyna wynosi")
print (Iloczyn)
#Iloraz

if B == 0:    
    print("Nie dziel przez 0")
else:
    Iloraz = A/B

print ("Iloraz wynosi")
print (Iloraz)

print("potega wynosi")
print (hypot)
