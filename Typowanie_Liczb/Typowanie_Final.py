#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Typowanie_Modul import ustawienia, losujliczby, pobierztypy, wyniki, zapisz_str, czytaj_str
from Typowanie_Modul import czytaj_json, zapisz_json 
import time

def main(args):
    # ustawienia gry
    nick, ileliczb, maksliczba, ilerazy = ustawienia() #rozpakowanie tupli

    # losujemy liczby
    liczby = losujliczby(ileliczb, maksliczba)

    # pobieramy typy użytkownika i sprawdzamy, ile liczb trafił
    for i in range(ilerazy):
        typy = pobierztypy(ileliczb, maksliczba)
        iletraf = wyniki(set(liczby), typy) 

    nazwapliku = nick + ".json" #nazwa pliku z historią losowań w .json
    nazwapliku1 = nick + ".txt" #nazwa pliku z historią losowań w .txt

    losowania = czytaj_json(nazwapliku)
    losowania_txt = czytaj_str(nazwapliku1)

    losowania.append({
        "czas": time.time(),
        "dane": (ileliczb, maksliczba),
        "wylosowane": liczby,
        "ile": iletraf
    })

    losowania_txt.append({
        "wylosowane": liczby, #tablica
        "dane": (ileliczb, maksliczba), #(int, int)
        "ile": iletraf, #int
        "czas": time.time() #float
    })

    zapisz_json(nazwapliku, losowania)
    zapisz_str(nazwapliku1,losowania_txt)

    print("\nLosowania:", liczby)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

"""
Cały program zawarty został w funkcji głównej main(). 
O tym, czy zostanie ona wykonana decyduje warunek if __name__ == '__main__':, 
który będzie prawdziwy, kiedy nasz skrypt zostanie uruchomiony jako główny. 
Wtedy nazwa specjalna __name__ ustawiana jest na __main__. 
Jeżeli korzystamy ze skryptu jako modułu, importując go, __main__ ustawiane jest na nazwę pliku, 
dzięki czemu kod się nie wykonuje.
"""

#Przykładowy return z Remik.json
#[{"czas": 1631043787.1202095, "dane": [1, 1], "wylosowane": [1], "ile": 1}, {"czas": 1631043857.316818, "dane": [1, 1], "wylosowane": [1], "ile": 1}]

#Przykładowy return z Remik.txt
#czas:1631043787.1202095;dane:[1, 1];wylosowane:[1];ile:1
#czas:1631043857.316818;dane:(1, 1);wylosowane:[1];ile:1

#{"czas":1631043787.1202095,"dane":[1, 1],"wylosowane":[1],"ile":1},
#{czas:1631043857.316818;dane:(1, 1);wylosowane:[1];ile:1}