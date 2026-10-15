line = "Programowanie w Pythonie jest fajne"

words = line.split()

pierwsze_znaki = "".join([w[0] for w in words])

ostatnie_znaki = "".join([w[-1] for w in words])

print("Pierwsze znaki:", pierwsze_znaki)
print("Ostatnie znaki:", ostatnie_znaki)
pierwsze_expected = "PwPjf"
ostatnie_expected = "ewete"
assert pierwsze_expected == pierwsze_znaki
assert ostatnie_expected == ostatnie_znaki