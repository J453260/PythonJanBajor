"""
L = [3, 5, 4] ; L = L.sort()
x, y = 1, 2, 3
X = 1, 2, 3 ; X[1] = 4
X = [1, 2, 3] ; X[3] = 4
X = "abc" ; X.append("d")
L = list(map(pow, range(8)))
"""

# Przypisanie 3 liczb do 2 zmiennych
# X[1] = 4 jest niepoprawne
# X[3] = 4 wychodzi poza zakres
# L = list(map(pow, range(8))), pow potrzebuje 2 argumentów

# Poprawiony kod:

L = [3, 5, 4]
L.sort()
x, y = 1, 2
X = 1, 2, 3
X = (X[0], 4, X[2])
Y = [1, 2, 3]
Y[2] = 4
Z = "abc"
Z += "d"
L = list(map(pow, range(8), [2]*8))

print(Z)
print(L)
