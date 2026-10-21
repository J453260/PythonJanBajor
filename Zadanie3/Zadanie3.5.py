import io
from contextlib import redirect_stdout


def rysuj(dlugosc):
    print("|", end="")
    for i in range(dlugosc):
        print("....|", end="")

    print()
    print(0, end="")
    for i in range(dlugosc):
        if i+1<=9:
            print("   ", i + 1, end="")

        if(i+1>=10 and i+1<=99):
            print("  ", i + 1, end="")

        if (i + 1 >= 100 and i + 1 <= 999):
            print(" ", i + 1, end="")

        if (i + 1 >= 1000 and i + 1 <= 9999):
            print("", i + 1, end="")


def przechwyc(dlugosc):
    bufor = io.StringIO()
    with redirect_stdout(bufor):
        rysuj(dlugosc)
    return bufor.getvalue()


# testy
result = przechwyc(3)
expected_result = "|....|....|....|\n0    1    2    3"
assert result == expected_result

assert przechwyc(0) == "|\n0"
assert przechwyc(1) == "|....|\n0    1"

# liczby 2-cyfrowe: końcówka dopasowana do kreski
assert przechwyc(10).split("\n")[1].endswith("    9   10")

# każda liczba zajmuje 5 znaków, więc obie linie mają tę samą długość
for n in (5, 12, 100, 1000):
    gora, dol = przechwyc(n).split("\n")
    assert len(gora) == len(dol) == 1 + 5 * n

# program właściwy
print("Podaj długość")
dlugosc = int(input())
rysuj(dlugosc)