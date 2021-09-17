#ZADANIE: Pobierz od użytkownika trzy liczby, sprawdź, która jest najmniejsza i wydrukuj ją na ekranie.

# Sprawdź, co się stanie, jeśli podasz liczby oddzielone przecinkiem lub podasz za mało liczb. 
# Zmień program tak, aby poprawnie interpretował dane oddzielane przecinkami.

op = "t"

while op == "t":
    while True:
        try:
            data = a, b, c = input("Podaj trzy liczby oddzielone spacjami: ").split(",")
            #Metoda split(separator) pozwala rozbić napis na składowe (w tym wypadku liczby).
        except ValueError:
            if len(data) != 3:
                print("Podałeś złą ilość liczb, spróbujmy jeszcze raz")
                continue
        else:
            break

    print("Wprowadzono liczby:", a, b, c)
    print("\nNajmniejsza:")

    if a < b:
        if a < c:
            najmniejsza = a
        else:
            najmniejsza = c
    elif b < c:
        najmniejsza = b
    else:
        najmniejsza = c

    print(najmniejsza)

    op = input("Jeszcze raz (t/n)? ")

print("Koniec.")