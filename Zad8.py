import random 

a=int(input("Poczatek zakresu: "))
b=int(input("Podaj koniec zakresu: "))

for i in range(6):
    print (random.randint(a,b))