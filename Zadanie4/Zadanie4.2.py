# Zadanie3.5:

def rysuj(dlugosc):
    wynik = "0"
    for i in range(dlugosc):
        n = i + 1
        if n <= 9:
            wynik += "    " + str(n)      # 4 spacje + cyfra = 5 znaków
        if 10 <= n <= 99:
            wynik += "   " + str(n)       # 3 spacje + 2 cyfry
        if 100 <= n <= 999:
            wynik += "  " + str(n)        # 2 spacje + 3 cyfry
        if 1000 <= n <= 9999:
            wynik += " " + str(n)         # 1 spacja + 4 cyfry
    return wynik


def ZadaniePiate():
    # testy
    assert rysuj(0) == "0"
    assert rysuj(1) == "0    1"
    assert rysuj(3) == "0    1    2    3"
    assert rysuj(9) == "0    1    2    3    4    5    6    7    8    9"
    assert rysuj(10) == "0    1    2    3    4    5    6    7    8    9   10"
    assert rysuj(12).endswith("   10   11   12")

    # liczby 3- i 4-cyfrowe
    assert rysuj(100).endswith("   99  100")
    assert rysuj(1000).endswith("  999 1000")

    # każda liczba zajmuje 5 znaków, więc długość to 1 + 5 * dlugosc
    for n in (0, 1, 9, 10, 99, 100, 999, 1000):
        assert len(rysuj(n)) == 1 + 5 * n

    # program właściwy
    print("Podaj długość")
    dlugosc = int(input())
    print("|" + "....|" * dlugosc)
    print(rysuj(dlugosc))




# Zadanie3.6:
def prostokat(x, y):
    linia_pozioma = "+" + "---+" * x + "\n"
    linia_pionowa = "|" + "   |" * x + "\n"

    wynik = ""
    for i in range(y):
        wynik += linia_pozioma
        wynik += linia_pionowa
    wynik += linia_pozioma
    return wynik


def sprawdz(x, y):
    wynik = prostokat(x, y)
    linia_pozioma = "+" + "---+" * x

    linie = wynik.split("\n")[:-1]                    # ostatni element po split to pusty string
    assert len(linie) == 2 * y + 1                    # y linii pionowych + (y+1) poziomych
    assert all(len(l) == 4 * x + 1 for l in linie)    # każda linia ma tę samą szerokość
    assert linie[0] == linie[-1] == linia_pozioma     # góra i dół takie same
    assert wynik.count("+") == (y + 1) * (x + 1)      # liczba rogów/skrzyżowań
    assert wynik.count("|") == y * (x + 1)            # liczba pionowych kresek
    assert wynik.endswith("\n")


def ZadanieSzoste():
    # testy
    assert prostokat(4, 2) == (
        "+---+---+---+---+\n"
        "|   |   |   |   |\n"
        "+---+---+---+---+\n"
        "|   |   |   |   |\n"
        "+---+---+---+---+\n"
    )
    assert prostokat(1, 1) == "+---+\n|   |\n+---+\n"
    assert prostokat(2, 0) == "+---+---+\n"

    for x, y in [(1, 1), (4, 2), (3, 5), (10, 1), (2, 0)]:
        sprawdz(x, y)

    print("Wszystkie testy przeszły poprawnie")
    print()

    # program właściwy
    print("Podaj liczbę kolumn: ")
    x = int(input())
    print("Podaj liczbę wierszy: ")
    y = int(input())
    print(prostokat(x, y), end="")


ZadaniePiate()
ZadanieSzoste()