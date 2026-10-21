rzym = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#rzym = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
#rzym = dict([("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)])

def roman2int(s):
    suma = 0
    for i in range(len(s)):
        wartosc = rzym[s[i]]
        if i + 1 < len(s) and wartosc < rzym[s[i + 1]]:
            suma -= wartosc
        else:
            suma += wartosc
    return suma


assert roman2int("III") == 3
assert roman2int("IV") == 4
assert roman2int("IX") == 9
assert roman2int("LVIII") == 58
assert roman2int("MCMXCIV") == 1994
assert roman2int("MMXXVI") == 2026
print("Wszystkie testy przeszły poprawnie")