import io
from contextlib import redirect_stdout


def rysuj(dlugosc):
    print(0, end="")
    for i in range(dlugosc):
        if i + 1 <= 9:
            print("   ", i + 1, end="")

        if (i + 1 >= 10 and i + 1 <= 99):
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


# testy: tylko ciąg generowany przez rysuj()
assert przechwyc(0) == "0"
assert przechwyc(1) == "0    1"
assert przechwyc(3) == "0    1    2    3"
assert przechwyc(9) == "0    1    2    3    4    5    6    7    8    9"
assert przechwyc(10) == "0    1    2    3    4    5    6    7    8    9   10"
assert przechwyc(12).endswith("   10   11   12")

# liczby 3- i 4-cyfrowe
assert przechwyc(100).endswith("   99  100")
assert przechwyc(1000).endswith("  999 1000")

# każda liczba zajmuje 5 znaków, więc długość to 1 + 5 * dlugosc
for n in (0, 1, 9, 10, 99, 100, 999, 1000):
    assert len(przechwyc(n)) == 1 + 5 * n

# program właściwy
print("Podaj długość")
dlugosc = int(input())
print("|", end="")
for i in range(dlugosc):
    print("....|", end="")

print()
rysuj(dlugosc)
