print("Podaj liczbę kolumn: ")
x = int(input())
print("Podaj liczbę wierszy: ")
y = int(input())
linia_pozioma = "+" + "---+" * x + "\n"
linia_pionowa = "|" + "   |" * x + "\n"

wynik = ""
for i in range(y):
    wynik += linia_pozioma
    wynik += linia_pionowa
wynik += linia_pozioma

linie = wynik.split("\n")[:-1] # ostatni element po split to pusty string
assert len(linie) == 2 * y + 1 # y wierszy pól + y+1 linii poziomych... razem 2y+1
assert all(len(l) == 4 * x + 1 for l in linie) # każda linia ma tę samą szerokość
assert linie[0] == linie[-1] == linia_pozioma.strip("\n")  # góra i dół takie same
assert wynik.count("+") == (y + 1) * (x + 1) # liczba rogów/skrzyżowań
assert wynik.count("|") == y * (x + 1) # liczba pionowych kresek
assert wynik.endswith("\n")

print("Wszystkie testy przeszły poprawnie")
print()
print(wynik, end="")