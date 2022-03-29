a = int (input("Podaj liczbe: "))

def czyParzysta(a):
    if a%2==0:
        return True 
    else:
            return False

wynik=czyParzysta(a)

if wynik == True:
    print (f"podana przez Ciebie liczba {a} jest parzysta")
else:
    print(f"Podana przez Ciebie liczba {a} nie jest parzysta ")