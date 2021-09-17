# ZADANIE: Pobierz od użytkownika n liczb wylosowanych i zapisz je w liście. 
# Wydrukuj: elementy listy i ich indeksy, elementy w odwrotnej kolejności, posortowane elementy. 
# Usuń z listy pierwsze wystąpienie elementu podanego przez użytkownika. 
# Usuń z listy element o podanym indeksie. 
# Podaj ilość wystąpień oraz indeks pierwszego wystąpienia podanego elementu.
# Wybierz z listy elementy od indeksu i do j.

from random import randint
import random

n = int(input("Ile liczb chcesz wylosować? (zakres liczby to 0:100): "))

lista = []

#Dodawanie do listy n-elementowej randomowych liczb z zakresu 0:100
for i in range(0,n):
    lista.append(random.randint(0, 100))
print("Elementy listy: ", lista)

print("Dodawanie elementów na koniec listy")
for i in range(0, 3):
    liczba = int(input("Podaj liczbę: "))
    lista.append(liczba)
print("Lista teraz wygląda tak: ", lista)

#Wyświetlanie indeksów elementów listy ([indeks] wartość) kolejno w nowych liniach
print("Zawartość listy ([indeks] wartość):")
for i, v in enumerate(lista):
    print("[", i, "]", v,)

print("Elementy w odwróconym porządku: ")
for e in reversed(lista):
    print(e, end=" ")

print()

print("Elementy posortowane rosnąco: ")
for e in sorted(lista):
    print(e, end=" ")

print()

print("Elementy posortowane malejąco: ")
for d in sorted(lista, reverse=True):
    print(d, end=" ")

print()
e = int(input("Którą liczbę usunąć? "))
lista.remove(e)
print(lista)

print("Wstawianie elementów do listy")
i, a = eval(input("Podaj indeks i element oddzielony przecinkiem: "))
lista.insert(i, a)
print(lista)

print("Wyszukiwanie i zliczanie elementu w liście")
e = int(input("Podaj liczbę: "))
print("Liczba wystąpień: ")
print(lista.count(e))
print("Indeks pierwszego wystąpienia: ")
if lista.count(e):
    print(lista.index(e))
else:
    print("Brak elementu w liście")

print("Pobieramy ostatni element z listy: ")
print(lista.pop())
print(lista)

print("Część listy (notacja wycinkowa):")
#Gdy tablica to np. [69,56,59,1] i podamy i=1, j=3 to wydrukuje nam [56,59] czyli od i do j-1
i, j = eval(input("Podaj indeks początkowy i końcowy oddzielone przecinkiem: "))
print(lista[i:j])

print()
#Tupla to lista niemodyfikowalna
#Próba zmiany tupli generuje błąd np. tupla[0] = 100
tupla = tuple(lista)
print(tupla)

# .insert(i, x) – wstawia x przed indeksem i
# .reverse() – sortuje listę w odwróconym porządku.

# Tupla to niemodyfikowalna lista. Wykorzystywana jest do zapamiętywania i przekazywania wartości, których nie powinno się zmieniać. 
# Tuple tworzymy podając wartości 
# w nawiasach okrągłych, np. tupla = (1, 'a') 
# lub z listy za pomocą funkcji: tuple(lista). 
# Tupla może powstać również poprzez spakowanie wartości oddzielonych przecinkami, np. 
# tupla = 1, 'a'. Próba zmiany wartości w tupli generuje błąd.

# Funkcja eval() interpretuje swój argument jako kod Pythona. 
# W instrukcji a, i = eval(input("Podaj element i indeks oddzielone przecinkiem: ")) 
# podane przez użytkownika liczby oddzielone przecinkiem interpretowane są jako tupla, 
# która następnie zostaje rozpakowana, czyli jej elementy zostają przypisane do zmiennych z lewej strony.

#x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#x[2:] ---> ['c', 'd', 'e', 'f', 'g', 'h', 'i'] (wyświetlenie od indeksu nr.2)
#x[:4] ---> ['a', 'b', 'c', 'd'] (x[:n] wyświetla do n-1 indeksu, w tym przypadku do 4 elementu)
#x[-2] ---> 'h', 2-gi ostatni element
#x[-2:] ---> ['h', 'i'], od drugiego ostatniego elementu do końca