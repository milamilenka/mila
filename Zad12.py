zespoly=['AC&DC','Abba','Elektryczne gitary',' Metalica' ]

#wyswietlanie listy za pomoca petli
print("Lista zespolow: ")
for i in zespoly:
    print(i)

#wyswietlanie listy z uzyciem*
print("Lista zespolow: ")
print(*zespoly)

#wyswietlanie listy z uzyciem * i separatora, 
print ("Lista zespolow: ")
print(*zespoly, sep = ", ")


#wyswietlanie listy z uzyciem * i separatora (nowej lini)
print ("Lista zespolow: ")
print(*zespoly, sep = " ")

#wyswietlanie listy z uzyciem 
print("Lista zespolow: ")
print(' '.join(zespoly))
