import random 

losowanie = []
strzaly = []

for i in range(6):
    a=random.randint(1,50)
    losowanie.append(a)
    b=int(input(f'Podaj liczbe {i+1} z 6:'))
    while b>50 or b<1:
        print("Podaj liczbe z zakresu od 1 do 50.")
        b= int(input(f"Podaj liczbe {i+1} z 6 : "))
    else:
        strzaly.append(b)

print("Wylosowane liczby: ")
print(*losowanie, sep=',')
print("Twoje liczby: ")
print(*strzaly, sep=',')

trafione = set(losowanie)&set(strzaly)

if len(trafione)>0:
    print(f"Trafiles{len(trafione)} z 6 liczb. Oto one: {trafione}")
else:
    print("Nie trafiles zadnej z liczb.")