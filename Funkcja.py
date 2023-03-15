# Funkcja zbiór instrukcji
# Prosta funkcja
# funkcje print() input() jak po nazwie jest nawias to funkcja
def show_sum(a, b):
    print("Suma:", a + b, "Sum:", a + b)

show_sum(1, 1)
show_sum(2, 8)
show_sum(99, 1.01)
print(show_sum(1, 1))

y = show_sum(1, 1)
print(y)

def add(a, b):
    return a + b

x = add(1, 9)
print(x)
print(add(99, 101))

print("Koniec gry")
print("\a")
print("lODY!" *10)