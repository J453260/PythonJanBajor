line = ("Liczenie wyrazów "
         "w Pythonie.")
slowa = line.split()
liczba_slow = len(slowa)
print(liczba_slow)
expected = 4
assert liczba_slow == expected
