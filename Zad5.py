bokA = int(input("Podaj bok A: "))
bokB = int(input("Podaj bok B: "))
bokC = int(input("Podaj bok C: "))
if bokA>bokB + bokC:
    print("Jest mozliwosc zbudowania trojkata")
elif bokB> bokC+bokA:
    print("Jest mozliwosc zbudowania trojkata")
elif bokC>bokA + bokB:
    print("Jest mozliwosc zbudowania trojkata")
else:
    print("Nie ma mozliwosci zbudowania trojkata")
    