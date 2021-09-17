#Komentowanie bloku kodu: CTRL + K + C lub CTRL + /

"""
ZADANIE: Napisz program, który na podstawie danych pobranych od użytkownika, czyli długości boków, 
sprawdza, czy da się zbudować trójkąt i czy jest to trójkąt prostokątny. 
Jeżeli da się zbudować trójkąt, należy wydrukować jego obwód i pole, w przeciwnym wypadku komunikat, 
że nie da się utworzyć trójkąta.
"""

import math

op = "t"
while op != "n":
    dane = input("Podaj 3 boki trójkąta oddzielone przecinkami: ")

    # lista = []
    # for x in dane.split(","):
    #     lista.append(int(x))
    # a, b, c = lista #rozpakowanie listy

    #wyrażenie listowe, które może zamienić kod 16:19
    a, b, c = [int(x) for x in dane.split(",")]

    print("Podano boki: ", a, b, c)

    if a + b > c and a + c > b and b + c > a:
        print("Z podanych boków da się zbudować trójkąt.")
        #Czy boki spełniają warunki trójkąta prostokątnego?
        if (a**2 + b**2 == c**2 or
                a**2 + c**2 == b**2 or
                b**2 + c**2 == a**2):
            print("Do tego prostokątny!")      

        # na wyjściu możemy wyprowadzać wyrażenia
        print("Obwód wynosi:", (a + b + c))
        p = 0.5 * (a + b + c)  # obliczmy współczynnik wzoru Herona
        # liczymy pole ze wzoru Herona
        P = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Pole wynosi:", P)
        op = "n"  # ustawiamy zmienną na "n", aby wyjść z pętli while
    else:
        print("Z podanych odcinków nie można utworzyć trójkąta prostokątnego.")
        op = input("Spróbujesz jeszcze raz (t/n): ")

print("Do zobaczenia...")