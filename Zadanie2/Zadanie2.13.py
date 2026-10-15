line = "Programowanie w Pythonie jest fajne"

words = line.split()
dlugosci = [len(slowo) for slowo in words]
print(sum(dlugosci))
expected = 31
assert expected == sum(dlugosci)