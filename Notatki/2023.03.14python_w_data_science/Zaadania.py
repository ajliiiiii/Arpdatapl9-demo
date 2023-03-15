# Program przyjmuje od użytkownika dwie liczby:
#     1. Liczba prawidłowych odpowiedzi (int)
#     2. Liczba pytań (int)
# Następnie program wyświetla odpowiedni komunikat na konsoli zależnie od % prawidłowych odpowiedzi:
#     100% - 90% : 5.0, 89% - 76% : 4.5, 75% - 70% : 4.0
#     69% - 60% : 3.5, 59% - 50% : 3.0, 49% - 0% : 2.0

# Napisz funkcję o nazwie show_temp_status, która przyjmuje jeden argument typu float
# Następnie zwraca str (nie wykonuje print!) zależnie od wartości podanego argumentu:
#     Poniżej 36.4 - wychłodzenie
#     <36.4 36.8> - norma
#     <36.9, 37.0> - stan podgorączkowy
#     Powyżej 3.71 - gorączka

dobre_odp = int(input("Podaj liczbę prawidłowych odpowiedzi: "))
l_pytan = int(input("Podaj liczbę pytań:"))

if 0.90 * l_pytan <= dobre_odp <= 1.0 * l_pytan:
    print("Otrzymujesz 5.0")
elif 0.76 * l_pytan <= dobre_odp <= 0.89 * l_pytan:
    print("Otrzymujesz 4.5")
elif  0.70 * l_pytan <= dobre_odp <= 0.75 * l_pytan:
    print("Otrzymujesz 4.0")
elif 0.50 * l_pytan <= dobre_odp <= 0.59 * l_pytan:
    print("Otrzymujesz 3.5")
elif 0.70 * l_pytan <= dobre_odp <= 0.75 * l_pytan:
    print("Otrzymujesz 3.0")
elif 0.0 * l_pytan <= dobre_odp <= 0.49 * l_pytan:
    print("Otrzymujesz 2.0")
else:
    print("jesteś gapa")


def show_temp_status(temperature):
    if temperature < 36.4:
        return "Wychłodzenie"
    elif 36.4 <= temperature <= 36.8:
        return "Norma"
    elif 36.9 <= temperature <= 37.0:
        return "Stan podg"
    else:
        return "Gorączka"

print(show_temp_status(32))




