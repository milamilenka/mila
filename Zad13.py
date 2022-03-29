import random

liczba=random.randint(1,20)
strzal= int(input("Jaka liczbe wylosowal komputer?"))

proby = []
proby.append(strzal)

if strzal==liczba and len(proby)==1:
    print(f"Brawo. Do odgadniecia liczby potrzebowales {len(proby)}prob")
else:
    while strzal!=liczba:
        proby.append(strzal)
        strzal = int (input("Sprobuj jeszcze raz. Jaka liczbe wylosowal komputer"))
    if strzal==liczba:
        print(f"Brawo. Do odgadniecia liczby potrzebowales {len(proby)}]prob")
        