line = "Programowanie w Pythonie jest fajne"

words = line.split()
dlugosci = [len(slowo) for slowo in words]
indeks = dlugosci.index(max(dlugosci))
najdluzsze_expected = "Programowanie"
dl_expected = 13
print(f"Najdłuższe słowo: {words[indeks]}, Długość: {dlugosci[indeks]}")
assert words[indeks] == najdluzsze_expected
assert dlugosci[indeks] == dl_expected