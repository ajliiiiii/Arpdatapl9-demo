number = 9
if number % 2 == 0:
    print("Podana liczba jest parzysta")
else:
    print("podana liczba jest nieparzysta")

number = 15
if number % 3 == 0 and number % 5 == 0:
    print("Pif paf")
elif number % 3 == 0 and number % 5 != 0:
    print("pif")
elif number % 3 != 0 and number % 5 == 0:
    print("Paf")
else:
    print("Twoja liczba to:", number)

