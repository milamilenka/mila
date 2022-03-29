Waga = float(input("Podaj wage w kg"))
Wzrost = float(input ("Podaj wzrost "))

BMI= Waga/(Wzrost**2)

if BMI <20:
    print (f"Twoje BMI wynosi {BMI} --> Niedowaga")
elif BMI >=20 and BMI <25:
    print (f"Twoje BMI wynosi {BMI} --> Waga prawidlowa ")
elif BMI >=25 and BMI <30:
    print (f"Twoje BMI wynosi {BMI} --> Nadwaga")
else:
    print (f"Twoje  BMI wynosi {BMI} --> Otylosc")
