def factorial(n):
    wynik = 1
    for i in range(1, n+1):
        wynik *= i

    return wynik

wynik = factorial(5)
print("5! = ", wynik)
expected = 120
assert wynik == expected