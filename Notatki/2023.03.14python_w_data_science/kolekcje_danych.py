txt = "Ala ma kota."

if "kot" in txt:
    print("Ala ma kota.")

# Metody dla str

# Ilość znaków
print(len(txt))
print(txt.upper())
print(txt.lower())
print(txt)
print(txt.isalnum())
print(txt * 10)

# isalnum nie jest bo ma kropki i spacje, same literki byłyby twierdzące


# Indeksowanie | 0..(len - 1)
print(txt[0])       # Wyświetl 1 znak.
print(txt[:4])      # <0, 4) | <0, 3>
print(txt[2:8])     # <2, 8) | <2, 7>
print(txt[3:])      # <3, len) | <3, len-1>
print(txt[2:8:2])   # <2,7> co drugi = <2,4,6>
print(txt[::3])     # <cały tekst> co trzeci
print(txt[::-1])    # Od końca

#  H  E  L  L  O
#  0  1  2  3  4
# -5 -4 -3 -2 -1

# print(txt[::-1]) odbicie lustrzane

# Napisz funkcję, która zwróci "odwrotny" idndeks wybranego indeksu i tekstu
# Przyjmowane argumenty:
# - łańcuch znakowy
# - indeks (z przedziału podanego tekstu)
# Zwraca:
# - odwrotny indeks
#
# Przykładowo:
#  fun("Ala ma kota", 10) zwraca -1
#  fun("HELLO", 2) zwraca -3

# spojrzec na funkcje len i relacje pomiedzy wartosciami
# -1 zawsze pokaze nam ostatni znak

txt = "W końcu wszystko pojmę"

print(txt[-1])
# ok czyli kumam, chodzi o ten przykład z HELLO z plusami i minusami jak ja pokaze 2 to musi mi pokazac -3 czyli to co niżej
#kurwa, kto by to skumał
txt = "W końcu wszystko pojmę"

def reverse_idx(text, index):
    if 0 <= index <= (len(text) - 1):
        return index - len(text)
    else:
        return -999
# zawsze jest - 1 bo liczymy razem z 0

# LISTY zawsze zaznaczona kwadratowym nawiasem, tylko dla jednego typu danych
# animals to jeden typ znakow str
animals = ["Kot", "Pies", "Słoń", "Żółw", "Chomik", "Papuga"]
numbers = [2, 5, 10, 3]
values = [1, "lol", "xd", True]

# Metody / Funkcje listy
# Pusta lista: empty = [] ;ub empty = list()
print(len(animals))
print(animals[0], animals[-1], animals[2:4])
print(sum(numbers), max(numbers), min(numbers))

#Dodawanie
animals.append("Szynszyla")
print(animals)
animals.extend(["Mysz", "Kanarek"])
print(animals)
# append jest tylko dla jednego argumentu, a extend dla wielu i podaje je się w liście[]
animals.insert(1, "Krokodyl")
print(animals)

#Usuwanie
animals.remove("Szynszyla")

print(animals)
#jeśli byłby dwa razy szynszyla, to najpierw usuneloby pierwszą od lewej, a potem kolejne jeśli byłyby takie polecenia.
animals.pop() #jeśli nie podamy idx to usunie ostatni z listy
print(animals)
animals.pop(2)
print(animals)

deleted_args = []
deleted_args.append(animals.pop())
print(animals)
deleted_value = animals.pop(0)
print(animals)
deleted_args.append(deleted_value)
print(animals, deleted_args)


# Modyfikacja
animals[0] = "Mrówka"
print(animals)
print(animals)

# Napisz funkcję manage_list, która przyjmuje dwa argumenty:
#  - Opcja: dodaj, usun
#  - Wartosc
#  Jeżeli wybraliśmy dodaj, wykonany jest append
# Jeżeli usuń, to wykonujemy pop()
# Funkcja niczego nie zwraca



ingrid = ["Butter", "Milk", "Eggs", "Water", "Salt", "Sugar"]


def manage_list(opcja, x):
    if opcja == add:
        ingrid.append(x)
    elif opcja == ded:
        ingrid.pop(x)

print(manage_list(add, "Pepper"))










