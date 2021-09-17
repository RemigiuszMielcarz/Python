def silnia_iter(n):
    """Obliczanie silni iteracyjnie"""
    silnia_tmp=1 #zmienna pomocnicza

    if n in (0,1):  #gdy n = 0 lub 1 zwroc 1
        return 1
    else:
        for i in range(2,n+1):  #gdy n>1 mnoz przez kolejne liczby od 2 do n
            silnia_tmp = silnia_tmp*i
        return silnia_tmp

def main(args):
    n = int(input("Prosze podac liczbe: "))

    obliczona_silnia = silnia_iter(n) #wypakowanie returna z funkcji silnia_iter

    print("Obliczona silnia z liczby %s to: %s" % (n, obliczona_silnia))

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))