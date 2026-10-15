liczba = 1210390940192049409019000442211
string = str(liczba)
licznik = 0
for i in range(len(string)):
    if string[i] == '0':
        licznik += 1

print(licznik)
expected = 9
assert licznik == expected