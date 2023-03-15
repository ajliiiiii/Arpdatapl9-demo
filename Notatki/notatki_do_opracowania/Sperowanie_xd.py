# Warunki arytmetyczne
cost = 3.10
product = "cebula"

#instrukcja sterująca if

if cost >= 3:
    print("Nie kupuj bo za drogie!")

else:
    print("Kupuj bo tanio")

# Operatory: not, and, or

# and wszystkie warunki muszą byc spelnione, zeby calosc byla prawdziwa
# or przynajmniej jeden warunek

if product == "cebula" and cost < 3:
    print("Kupuj tę cebulę, Polaku")
else:
    print("Unikaj jak ognia, bo Panie jakie drogie")

# Operator in / not in (później) oraz przedziały
# Przypadek: Oceny są z zakresu 2.0 do 5.0
grade = 5.2
if 2 <= grade <= 5:
    print("Ocena prawidłowa")
else:
    print("Ocena nieprawidłowa")

# elif - sprawdza kolejny warunek, jesli poprzedni byl nieprawdziwy
if product == "cebula" and cost <= 3:
    print ("kupujesz cebule")
elif product == "marchewka"and cost <= 4.5:
    print("Kupujesz marchewke")
else:
    print("wychodzisz bez zakupów")
    elif product = "wódka" and cost <= 19.99
    print("Kupujesz alkohol")
else:
print("Wychodzisz bez zakupów")

