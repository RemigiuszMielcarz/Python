#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import os
import json

def ustawienia():
    """Funkcja pobiera nick użytkownika, ilość losowanych liczb, maksymalną
    losowaną wartość oraz ilość typowań. Ustawienia zapisuje."""

    nick = input("Podaj nick: ")
    nazwapliku = nick + ".ini"              #Tworzenie pliku inicjalizującego
    gracz = czytaj_ust(nazwapliku)          #Przyjmuje return z czytaj_ust
    odp = None
    if gracz:                               #Jeśli pobrało ustawienia
        print("Twoje ustawienia:\nLiczb: %s\nZ Maks: %s\nLosowań: %s" %
              (gracz[1], gracz[2], gracz[3]))
        odp = input("Zmieniasz (t/n)? ")

    if not gracz or odp.lower() == "t":     #Jeżeli brak ustawień lub użytkownik chce je zmienić | odp.lowe() - zmiana na małe litery
        while True:
            try:
                ile = int(input("Podaj ilość typowanych liczb: "))
                maks = int(input("Podaj maksymalną losowaną liczbę: "))
                if ile > maks:
                    print("Błędne dane!")
                    continue
                ilelos = int(input("Ile losowań: "))
                break
            except ValueError:
                print("Błędne dane!")
                continue
        gracz = [nick, str(ile), str(maks), str(ilelos)]
        zapisz_ust(nazwapliku, gracz)

    return gracz[0:1] + [int(x) for x in gracz[1:4]]
    #Ponieważ w programie głównym oczekujemy, że funkcja ustawienia() zwróci dane typu napis, liczba, liczba, liczba 
    # – używamy konstrukcji: return gracz[0:1] + [int(x) for x in gracz[1:4]], ponieważ gracz to napis, a reszta to liczby

def czytaj_ust(nazwapliku):
    if os.path.isfile(nazwapliku):      #Jeśli istnieje taki plik (.isfile)
        plik = open(nazwapliku, "r")    #Otwórz go czytając
        linia = plik.readline()         #Odczytanie pojedynczej linii tekstu
        plik.close()                    #Zamknij plik
        if linia:                       #Jeśli istnieje linijka tekstu
            return linia.split(";")     #Rozbijanie tekstu wg podanego znaku na elementy listy
                                        #Zwraca nam nick;ile_liczb;maks_liczba;ile_prob
    return False                        #Jeśli nie ma takiego pliku zwróć Fałsz

def zapisz_ust(nazwapliku, gracz):
    plik = open(nazwapliku, "w")        #Otwórz plik z opcją Write
    plik.write(";".join(gracz))         #Złączanie elementów listy za pomocą podanego znaku

    plik.close()

def losujliczby(ile, maks):
    """Funkcja losuje ile unikalnych liczb całkowitych od 1 do maks"""
    liczby = []
    i = 0
    while i < ile:
        liczba = random.randint(1, maks)
        if liczby.count(liczba) == 0: #Jeśli liczby się nie powtarzają
            liczby.append(liczba)
            i = i + 1
    return liczby


def pobierztypy(ile, maks):
    """Funkcja pobiera od użytkownika jego typy wylosowanych liczb"""
    print("Wytypuj %s z %s liczb: " % (ile, maks))
    typy = set()
    i = 0
    while i < ile:
        try:
            typ = int(input("Podaj liczbę %s: " % (i + 1)))
        except ValueError:
            print("Błędne dane!")
            continue

        if 0 < typ <= maks and typ not in typy:
            typy.add(typ)
            i = i + 1
    return typy

def wyniki(liczby, typy):
    """Funkcja porównuje wylosowane i wytypowane liczby,
    zwraca ilość trafień"""
    trafione = set(liczby) & typy
    if trafione:
        print("\nIlość trafień: %s" % len(trafione))
        trafione = ", ".join(map(str, trafione)) #Funkcja map() pozwala na zastosowanie jakiejś innej funkcji, w tym wypadku str(czyli konwersji na napis)
                                                 #Metoda napisów join() pozwala połączyć elementy listy (muszą być typu string) podanymi znakami, np. przecinkami (", ")
        print("Trafione liczby: %s" % trafione)
    else:
        print("Brak trafień. Spróbuj jeszcze raz!")

    print("\n" + "x" * 40 + "\n")  # wydrukuj 40 znaków x

    return len(trafione)

def czytaj_json(nazwapliku):
    """Funkcja odczytuje dane w formacie json z pliku"""
    dane = []
    if os.path.exists(nazwapliku):
        with open(nazwapliku, "r") as plik:
            dane = json.load(plik)   #Zawartość podanego pliku dekodujemy do listy
    return dane

def zapisz_json(nazwapliku, dane):
    """Funkcja zapisuje dane w formacie json do pliku"""
    with open(nazwapliku, "w") as plik:
        json.dump(dane, plik)

def czytaj_str(nazwapliku):
    #Funkcja powinna zwracać tablicę słowników
    dane = []
    if os.path.exists(nazwapliku):
        with open(nazwapliku, "r") as plik:
            for linia in plik: 
                fields = [field.split(":") for field in linia.split(";")]
                result = { name: eval(value) for name,value in fields}
                dane.append(result)
    return dane

#wylosowane:[4, 5, 7];dane:(3, 10);ile:0;czas:1434482711.67

#[{"czas": 1631043787.1202095, "dane": [1, 1], "wylosowane": [1], "ile": 1}, {"czas": 1631043857.316818, "dane": [1, 1], "wylosowane": [1], "ile": 1}]

def zapisz_str(nazwapliku, dane):
    #Funkcja zapisuje dane w formacie txt do pliku
    with open(nazwapliku, "w+") as plik:
        for slownik in dane:
            linia = [tekst + ":" + str(wartosc) for tekst, wartosc in slownik.items()]
            linia = ";".join(linia)
            plik.write(linia+"\n")

#ZADANIE 0
#Uzupełnijmy program tak, aby był nieco odporniejszy na niepoprawne dane

#ZADANIE 1
# Przenieś kod powtarzany w pętli for (linie 17-24) do funkcji zapisanej w module programu.
# Wywołanie funkcji: iletraf = wyniki(set(liczby), typy) umieść w linii 17 programu głównego.

#ZADANIE 2
# Załóżmy, że jednak chcielibyśmy zapisywać historię losowań w pliku tekstowym, 
# którego poszczególne linie zawierałyby dane jednego losowania, np.: wylosowane:[4, 5, 7];dane:(3, 10);ile:0;czas:1434482711.67

#ZADANIE 3
#Napisz funkcję czytaj_str() odczytującą tak zapisane dane. Funkcja powinna zwrócić listę słowników.