# Słownik zawierający obce wyrazy oraz ich możliwe znaczenia. 
# Pobieramy od użytkownika dane w formacie: wyraz obcy: znaczenie1, znaczenie2, ... itd. 
# Pobieranie danych kończy wpisanie słowa “koniec”. Podane dane zapisujemy w pliku. 
# Użytkownik ma możliwość dodawania nowych i zmieniania  oraz usuwania zapisanych danych.

# Jest możliwość uczenia się zapisanych w słowniku słówek. 
# Program wyświetla kolejne słowa obce i pobiera od użytkownika możliwe znaczenia. 
# Następnie wyświetla, które z nich są poprawne.

# POJĘCIA: słownik, odczyt i zapis plików, formatowanie napisów, format csv.

# Format csv polega na zapisywaniu wartości oddzielonych separatorem, czyli domyślnie przecinkiem. 
# Jeżeli wartość zawiera znak separatora, jest cytowana domyślnie za pomocą cudzysłowu. 
# W naszym wypadku przykładowa linia pliku przyjmie postać: wyraz obcy,znaczenie1,znaczenie2,...

import os
import csv

slownik = {}  # pusty słownik

sPlik = "slownik.txt"  # nazwa pliku zawierającego wyrazy i ich tłumaczenia
sFile = "slownik.csv"

#                                           ODCZYT TXT
def otworz_txt(plik):
    """Funkcja zwraca ilość elementów w liście"""
    if os.path.isfile(sPlik):  # czy istnieje plik słownika?
        with open(sPlik, "r") as pliktxt:  # otwórz plik do odczytu
            for line in pliktxt:  # przeglądamy kolejne linie
                # rozbijamy linię na wyraz obcy i tłumaczenia
                t = line.split(":")                                         # ['nerd', 'kujon,medrzec\n']
                wobcy = t[0]                                                # nerd
                # usuwamy znaki nowych linii
                znaczenia = t[1].replace("\n", "")                          # kujon,medrzec            
                znaczenia = znaczenia.split(",")  # tworzymy listę znaczeń  # ['kujon', 'medrzec']
                # dodajemy do słownika wyrazy obce i ich znaczenia  
                slownik[wobcy] = znaczenia                                  # {'nerd': ['kujon', 'medrzec']}
    return len(slownik)  # zwracamy ilość elementów w słowniku              # 1

#                                             ZAPIS TXT
def zapisz_txt(slownik):
    # otwieramy plik do zapisu, istniejący plik zostanie nadpisany(!)
    pliktxt = open(sPlik, "w")
    for wobcy in slownik:
        # "sklejamy" znaczenia przecinkami w jeden napis
        znaczenia = ",".join(slownik[wobcy])                                # kujon,medrzec
        # wyraz_obcy:znaczenie1,znaczenie2,...
        linia = ":".join([wobcy, znaczenia])                                # nerd:kujon,medrzec
        pliktxt.write(linia + "\n")  # zapisujemy w pliku kolejne linie     # nerd:kujon,medrzec\n
        # można też tak:
        #print(linia, file=pliktxt, end="\n")
    pliktxt.close()  # zamykamy plik

#                                            ODCZYT CSV
def otworz_csv(plik):
    """Funkcja zwraca ilość elementów w liście"""
    if os.path.isfile(sFile):                        # czy istnieje plik słownika?
        with open(sFile, newline='') as plikcsv:     # otwórz plik do odczytu
            tresc = csv.reader(plikcsv)              # interpretuje podany plik jako zapisany w formacie csv i każdą linię zwraca w postaci listy elementów.
            for linia in tresc:                      # przeglądamy kolejne linie
                slownik[linia[0]] = linia[1:]        # zapisuje dane w słowniku, kluczem jest wyraz obcy (1 element listy), wartościami – lista znaczeń.
    return len(slownik)                              # zwracamy ilość elementów w słowniku

#                                            ZAPIS CSV
def zapisz_csv(slownik):
    # otwieramy plik do zapisu, istniejący plik zostanie nadpisany(!)
    with open(sFile, "w", newline='') as plikcsv:
        tresc = csv.writer(plikcsv)
        for wobcy in slownik:
            lista = list(slownik[wobcy])             # kujon,medrzec
            lista.insert(0, wobcy)  
            tresc.writerow(lista)                    # nerd,kujon,medrzec

def oczysc(str):
    str = str.strip()  # usuń początkowe lub końcowe białe znaki
    str = str.lower()  # zmień na małe litery
    return str

def zapisz(wybor):
        if wybor == 'csv':
            zapisz_csv(slownik)
        if wybor == 'txt':
            zapisz_txt(slownik)

def drukuj(slownik):
    print("=" * 50)
    print("Uzupełniony słownik w pliku, który wybrałeś: \n", slownik)

    print("=" * 50)
    print("{0: <15}{1: <40}".format("Wyraz obcy", "Znaczenia")) # Na wyraz obcy zarezerwuj 15 miejsc, a na wyraz obcy 40 (liczone od początku linii)
    print("=" * 50)
    for wobcy in slownik:
        print("{0: <15}{1: <40}".format(wobcy, ",".join(slownik[wobcy])))
    print("=" * 50)

def ile_tafione(znaczenia, typy):
    """Funkcja porównuje podane słowa ze znaczeniami słówka obecego"""
    typy = set(typy)
    trafione = set(znaczenia) & typy
    if trafione:
        print("\nPodałeś: %s z %s poprawnych znaczeń słówka obcego." %(len(trafione), len(znaczenia)))
        trafione = ", ".join(map(str, trafione)) #Funkcja map() pozwala na zastosowanie jakiejś innej funkcji, w tym wypadku str(czyli konwersji na napis)
                                                 #Metoda napisów join() pozwala połączyć elementy listy (muszą być typu string) podanymi znakami, np. przecinkami (", ")
        print("Trafione znaczenia: %s" % trafione)
        print()
    else:
        print("Brak trafień. Spróbuj jeszcze raz!")
        print()

def main(args):

    option = input("Chcesz uczyć się wyrazów obcych czy wprowadzić dane? (uczyc/wprowadzic): ")

    if option == 'wprowadzic':
        print("""Podaj dane w formacie:
        wyraz obcy: znaczenie1, znaczenie2
        Aby zakończyć wprowadzanie danych, napisz "koniec".
        """)

        wybor = input(("""Z jakich plików korzystamy? Wybierz między:
        txt/csv: """))

        # wobce = set() # pusty zbiór wyrazów obcych
        # zmienna oznaczająca, że użytkownik uzupełnił lub zmienił słownik
        nowy = False

        if wybor == 'txt':
            ileWyrazow = otworz_txt(sPlik) 
        elif wybor == 'csv':
            ileWyrazow = otworz_csv(sFile)
        else:
            print("Błędne dane!!!!") 
        
        print("Wpisów w bazie:", ileWyrazow)

        # główna pętla programu
        while True:
            dane = input("Podaj dane: ")                                    # nerd: kujon, medrzec
            t = dane.split(":")                                             # ['nerd', ' kujon, medrzec']
            wobcy = t[0].strip().lower()                                    # nerd
            if wobcy == 'koniec':
                break
            elif dane.count(":") == 1:                                      # sprawdzamy poprawność danych
                if wobcy in slownik:
                    print("Wyraz: ", wobcy, " - jest już w słowniku.")
                    op = input("Zastąpić wpis (t/n)? ")
                # czy wyrazu nie ma w słowniku? a może chcemy go zastąpić?
                if wobcy not in slownik or op == "t":
                    znaczenia = t[1].split(",")                             # [' kujon', ' medrzec']
                    znaczenia = list(map(oczysc, znaczenia))                # ['kujon', 'medrzec']
                    slownik[wobcy] = znaczenia                              # {'nerd': ['kujon', 'medrzec']}
                    nowy = True
            else:
                print("Błędny format!")

        if nowy:
            zapisz(wybor)

        drukuj(slownik)

        opcja = input("Chcesz usunąć jakiś wyraz obcy ze słownika? (tak/nie): ")
        if opcja == 'tak':
            wyrazobcy = input("Który wyraz?: ")
            del slownik[wyrazobcy]
            drukuj(slownik)

            if wybor == 'csv':
                f = open(sFile, "w+")
                f.close()
            elif wybor == 'txt':
                f = open(sPlik, "w+")
                f.close()
            else:
                raise TypeError("Błędny wybór! Musisz wybrać między (tak/nie).")

            zapisz(wybor)
           
    elif option == 'uczyc':
        print("Rozpoczynam naukę wyrazów obcych.")
        op_uczyc = input("Z którego pliku chcesz się uczyć? (txt/csv)?: ")

        if op_uczyc == 'txt':
            ileWyrazow = otworz_txt(sPlik) 
        elif op_uczyc == 'csv':
            ileWyrazow = otworz_csv(sFile)
        else:
            raise TypeError("Błędny wybór! Musisz wybrać między (txt/csv).")

        print("Wpisów w bazie:", ileWyrazow)

        print("Wyświetlam kolejno słowa obce, podaj oddzielając przecinkiem ich możliwe znaczenia: ")
    
        if op_uczyc == 'txt':
            with open(sPlik, "r") as pliktxt:  # otwórz plik do odczytu
                for line in pliktxt:  # przeglądamy kolejne linie
                    # rozbijamy linię na wyraz obcy i tłumaczenia
                    t = line.split(":")                                         # ['nerd', 'kujon,medrzec\n']
                    wobcy = t[0]                                                # nerd
                    # usuwamy znaki nowych linii
                    znaczenia = t[1].replace("\n", "")                          # kujon,medrzec            
                    znaczenia = znaczenia.split(",")  # tworzymy listę znaczeń  # ['kujon', 'medrzec']
                    # dodajemy do słownika wyrazy obce i ich znaczenia  
                    slownik[wobcy] = znaczenia                                  # {'nerd': ['kujon', 'medrzec']}

                    podane_slowa = input('{0}:'.format(t[0])).split(",")

                    if podane_slowa == znaczenia:
                        print("Bardzo dobrze! Wszystkie znaczenia są poprawne.")
                    else:
                        ile_tafione(znaczenia, podane_slowa)
            
        elif op_uczyc == 'csv':
            if os.path.isfile(sFile):                        # czy istnieje plik słownika?
                with open(sFile, newline='') as plikcsv:     # otwórz plik do odczytu
                    tresc = csv.reader(plikcsv)              # interpretuje podany plik jako zapisany w formacie csv i każdą linię zwraca w postaci listy elementów.
                    for linia in tresc:                      # przeglądamy kolejne linie
                        slownik[linia[0]] = linia[1:]        # zapisuje dane w słowniku, kluczem jest wyraz obcy (1 element listy), wartościami – lista znaczeń.    

                        podane_slowa = input('{0}:'.format(linia[0])).split(",")   

                        if podane_slowa == linia[1:]:
                            print("Bardzo dobrze! Wszystkie znaczenia są poprawne.")
                        else:
                            znaczenia = linia[1:]
                            ile_tafione(znaczenia, podane_slowa)                       

            print("Koniec nauki, nie ma już kolejnych słówek obcych w słowniku.")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

"""
slownik = { 'go':['iść','pojechać'] } – utworzenie 1-elementowego słownika;
slownik['make'] = ['robić','marka'] – dodanie nowego elementu;
slownik['go'] – odczyt elementu.
"""