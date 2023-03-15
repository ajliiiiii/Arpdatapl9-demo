# Napisz funkcję manage_list, która przyjmuje dwa argumenty:
#  - Opcja: dodaj, usun
#  - Wartosc
# Jeżeli wybraliśmy dodaj, wykonany jest append
# Jeżeli usuń, to wykonujemy pop()
# Funkcja niczego nie zwraca





ingrid = ["Butter", "Milk", "Eggs", "Water", "Salt", "Sugar"]

def manage_list(opcja, wartosc):
  if opcja == "dodaj":
   return ingrid.append(wartosc)
  elif opcja == "usun":
   return ingrid.pop()

print(manage_list("dodaj", "Avocado"))
print(manage_list("usun", "Eggs"))
print(ingrid)
