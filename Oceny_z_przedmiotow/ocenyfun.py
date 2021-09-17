import math

def drukuj(co, kom="Sekwencja zaweira: "):
    print(kom)
    for i in co:
        print(i, end=" ")

def srednia(oceny):
    suma = sum(oceny)
    return suma / float(len(oceny))

def mediana(oceny):
    """
    Jeżeli ilość ocen jest parzysta, medianą jest średnia arytmetyczna
    dwóch środkowych ocen. Jesli ilość  jest nieparzysta mediana równa
    się elementowi środkowemu ouporządkowanej rosnąco listy ocen.
    """
    oceny.sort()
    if len(oceny) % 2 == 0:  # parzysta ilość ocen
        half = int(len(oceny) / 2) # wylicza nam indeks drugiego ze środkowych elementów.
        # można tak:
        # return float(oceny[half-1]+oceny[half]) / 2.0
        # albo tak:
        return float(sum(oceny[half - 1:half + 1])) / 2.0
    else:  # nieparzysta ilość ocen
        return oceny[int(len(oceny) / 2)] # zaokrągla w dół do jedności

def wariancja(oceny, srednia):
    """
    Wariancja to suma kwadratów różnicy każdej oceny i średniej
    podzielona przez ilość ocen:
    sigma = (o1-s)+(o2-s)+...+(on-s) / n, gdzie:
    o1, o2, ..., on - kolejne oceny,
    s - średnia ocen,
    n - liczba ocen.
    """
    sigma = 0.0
    for ocena in oceny:
        sigma += (ocena - srednia)**2
    return sigma / len(oceny)

def odchylenie(oceny, srednia):  # pierwiastek kwadratowy z wariancji
    w = wariancja(oceny, srednia)
    return math.sqrt(w)

# W konsoli Pythona utwórz listę wyrazy zawierającą elementy: abrakadabra i kordoba. 
# Utwórz zbiór w1 poleceniem set(wyrazy[0]). Oraz zbiór w2 poleceniem set(wyrazy[1]). 
# Wykonaj kolejno polecenia ilustrujące użycie klasycznych operatorów na zbiorach, 
# czyli: różnica (-) , suma (|), przecięcie (część wspólna, &) i elementy unikalne (^):

# slowa = 'abrakadabra', 'kordoba'
# wyrazy = []
# for i in slowa:
#     wyrazy.append(i)

# w1 = set(wyrazy[0]) # {'a', 'b', 'd', 'k', 'r'}
# w2 = set(wyrazy[1]) # {'a', 'b', 'd', 'k', 'o', 'r'}

# print(w2 - w1) # Różnica
# print(w1 | w2) # Suma
# print(w1 & w2) # Część wspólna
# print(w1 ^ w2) # Elementy unikalne