"""
ZADANIE: Wydrukuj alfabet w porządku naturalnym, 
a następnie odwróconym w formacie: “mała => duża litera”. 
W jednym wierszu trzeba wydrukować po pięć takich grup.
"""

"""
            #   PIERWSZA WERSJA   #
print("Alfabet w porządku naturalnym:")
x = 0
for i in range(65, 91):
    litera = chr(i) #chr(kod_ascii) – zwraca znak odpowiadający podanemu kodowi ASCII;
    x += 1 #Zacznij od 1
    tmp = litera + " => " + litera.lower()
    if i > 65 and x % 5 == 0:
        x = 0
        tmp += "\n" #Po piątym wyrazie alfabetu przejdź do nowej linii

    if x == 0:
        print(tmp, end="")
    else:
        print(tmp, end=" ")#Oddziel sekwencje "X => x" wyrazem białym (jedna linia)
    #print(tmp) #gdyby było tak => otrzymujemy na wyjściu A => a i przechodzimy do następnej linii
"""

#Uprość warunek w pierwszej pętli for drukującej alfabet w porządku naturalnym tak, aby nie używać operatora modulo.

'''
            #   DRUGA WERSJA   #
print("Alfabet w porządku naturalnym:")
x = -1
for i in range(65, 91, +1):
    litera = chr(i) #chr(kod_ascii) – zwraca znak odpowiadający podanemu kodowi ASCII;
    x += 1 #Zacznij od 0
    if x == 5:
        x = 0
        print("\n", end= "")
    print(litera, "=>", litera.lower(), end=" ")
'''

#Wydrukuj co n-tą grupę liter alfabetu, przy czym wartość n podaje użytkownik. Wskazówka: użyj opcjonalnego, trzeciego argumentu funkcji range().

            #   TRZECIA WERSJA   #
n = int(input("Podaj ile chcesz mieć grup (mała => duża litera) alfabetu w jednej linii: "))
print("Alfabet w porządku naturalnym:")
x = -1
for i in range(65, 91, +1):
    litera = chr(i) #chr(kod_ascii) – zwraca znak odpowiadający podanemu kodowi ASCII;
    x += 1 #Zacznij od 0
    if x == n:
        x = 0
        print("\n", end= "")
    print(litera, "=>", litera.lower(), end=" ")

print("\nAlfabet w porządku odwróconym:")
x = -1
for i in range(122, 96, -1):
    litera = chr(i)
    x += 1
    if x == 5:
        x = 0
        print("\n", end="")
    print(litera.upper(), "=>", litera, end=" ")

# list(range(0, 100)) # wydrukuje liste wartości od 0 do 99(!)
# list(range(0,100,+2)) #skok = 2
# list(range(122,96,-1)) # wydrukuje liste wartości od 122 do 97(!)
