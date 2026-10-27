def fibonacci(n):
    n_tyWyraz = 0
    #tab = []
    tab = [0] * n
    tab[0] = 0
    if n > 1:
        tab[1] = 1
    for i in range(2, n):
        tab[i] = tab[i-1] + tab[i-2]

    n_tyWyraz = tab[n-1]
    return n_tyWyraz

wynik = fibonacci(8)
print(wynik)
expected = 13
assert wynik == expected