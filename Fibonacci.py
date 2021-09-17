#Zmień funkcje tak, aby zwracały poprawne wartości przy założeniu, że dwa pierwsze wyrazy ciągu równe są 1 (bez zera).

from functools import lru_cache # LRU Cache = Least Recently Used Cache
def fib_iter1(n):  # definicja funkcji
    """
        Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
        aż do wyrazu n-tego, który zwraca.
        Wersja iteracyjna z pętlą while.
    """
    pwyrazy = (0, 1)  # dwa pierwsze wyrazy ciągu zapisane w tupli
    a, b = pwyrazy    # Przypisanie wielokrotne, rozpakowanie tupli
    print(a, end=" ") # WYŚWIETL PIERWSZY WYRAZ ( 0_ )
    while n > 1:
        print (b, end=" ") # WYŚWIETL AKTUALNY WYRAZ
        a, b = b, a + b    # Przypisanie wielokrotne   |  do "a" przypisz "b" (wyraz aktualny),  do "b" przypisz sume (a,b) (wyrazu aktualnego i poprzedniego)
        n -= 1

def fib_iter11(n):
    pwyrazy = (1, 1)
    a, b = pwyrazy
    print(a, end=" ")
    while n > 1:
        print (b, end=" ")
        a, b = b, a + b  # przypisanie wielokrotne
        n -= 1

def fib_iter2(n):
    """
        Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
        aż do wyrazu n-tego, który zwraca.
        Wersja iteracyjna z pętlą for.
    """
    a, b = 0, 1
    print("wyraz", 1, a)
    print("wyraz", 2, b)
    for i in range(1, n - 1): #Dla "5" i=> [1,2,3]
        # wynik = a + b
        a, b = b, a + b
        print("wyraz", i + 2, b)

    print()  # wiersz odstępu
    return b

#                                   INNA WERSJA 

def fib_iter2_1(n):
    """
        Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
        aż do wyrazu n-tego, który zwraca.
        Wersja iteracyjna z pętlą for.
    """
    a, b = 0, 1
    print("wyraz", 1, a)
    print("wyraz", 2, b)
    for i in range(3, n + 1): #Dla "5" i=> [1,2,3,4,5]
        # wynik = a + b
        a, b = b, a + b
        print("wyraz", i , b)

    print()  # wiersz odstępu
    return b

def fib_iter22(n):
    """
        Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
        aż do wyrazu n-tego, który zwraca.
        Wersja iteracyjna z pętlą for.
    """
    a, b = 1, 1
    print("wyraz", 1, a)
    print("wyraz", 2, b)
    for i in range(1, n - 1):  
        # wynik = a + b
        a, b = b, a + b
        print("wyraz", i + 2, b)

    return b

def fib_rek(n):
    """
        Funkcja zwraca n-ty wyraz ciągu Fibonacciego.
        Wersja rekurencyjna.
    """
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib_rek(n - 1) + fib_rek(n - 2) 

def fib_rek_11(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        return fib_rek_11(n - 1) + fib_rek_11(n - 2)

    # nth term is the sum of (n-1)th and (n-2)th term.
    #                                                fibonacci(5) = fibonacci (4) + fibonacci (3)
    #                                                   = fibonacci(3) + fibonacci(2) + fibonacci(2) + fibonacci(1)
    #         = fibonacci(2) + fibonacci(1) + fibonacci(2) + fibonacci(1) + fibonacci(1)
    # Funkcja słabo działa dla większej ilości liczb

#Napisz funkcję, która wyświetli 100 wyrazów ciągu Fibonacciego

#                                                        MEMOIZACJA
# Memoizacja to technika optymalizacyjna stosowana przede wszystkim w celu przyspieszenia programów komputerowych poprzez 
# zapisywanie wyników kosztownych wywołań funkcji i zwracanie wyników z pamięci podręcznej, gdy te same wejścia wystąpią ponownie.

# Idea: Cache values. Przechowuj wartości dla ostatnich wywołań funkcji, aby przyszłe wywołania nie musiały powtarzać pracy

# 1. Zaimplementuj zapamiętywanie jawne
# 2. Użyj narzędzia Pythona, które sprawia, że zapamiętywanie staje się banalne

fibonacci_cache = {} # Pamięć podręczna Fibonacciego, która będzie przechowywała ostatnie wywołania 

def fibonacci(n): #Funkcja Fibonacciego, aby używać wartości z pamięci

    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Otherwise: compute the Nth term. We will first compute the value, cache it, then return it
    # Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

@lru_cache(maxsize= 1000)
def fibonacciLRU(n):
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)    

def main(args):

    print("=" * 80)

    n = int(input("Podaj ilość wyrazów: "))

    print("=" * 40)

    ################################################
    print("Fibonacci z pętlą while i pwyraz (0,1): ")
    fib_iter1(n)
    ################################################

    print()                #Przejście do nowej linii

    ################################################
    print("Fibonacci z pętlą while i pwyraz (1,1): ")
    fib_iter11(n)
    ################################################

    print()               

    print("=" * 40)

    ################################################
    print("Fibonacci z pętlą for i pwyraz (0,1): ")
    fib_iter2(n)
    ################################################

    ###########Inny sposób na to samo###############
    print("Fibonacci z pętlą for i pwyraz (0,1): ")
    fib_iter2_1(n)
    ################################################

    ################################################
    print("Fibonacci z pętlą for i pwyraz (1,1): ")
    fib_iter22(n)
    ################################################

    print("=" * 40)

    ################################################################################################
    print("Rekurencyjnie zwracam ostatni wyraz: Dla pwyraz (0,1): Wyraz", n, ":", fib_rek(n-1))
    print("Rekurencyjnie zwracam ostatni wyraz: Dla pwyraz (1,1): Wyraz", n, ":", fib_rek_11(n))
    ################################################################################################

    print("=" * 40)

    ################################################################################################
    print("Memoizacja: Wyświetlam ciąg Fibonacciego dla: 100 wyrazów:")
    for n in range(1,101):
        print(n, ":", fibonacci(n))
    ################################################################################################

    print()
    print("=" * 40)
    print()

    ################################################################################################
    print("LRU_CACHE: Wyświetlam ciąg Fibonacciego dla: 100 wyrazów:")
    for n in range(1,101):
        print(n, ":", fibonacciLRU(n))
    ################################################################################################

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))