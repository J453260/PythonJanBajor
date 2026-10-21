print("Pętla for")
wynik_for = []
for i in range(30):
    if i % 3 != 0:
        print(i)
        wynik_for.append(i)

print("Pętla while")
wynik_while = []
j = 0
while j < 30:
    if j % 3 != 0:
        print(j)
        wynik_while.append(j)

    j += 1

# testy
expected_result = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17,
                   19, 20, 22, 23, 25, 26, 28, 29]

assert wynik_for == expected_result
assert wynik_while == expected_result
assert wynik_for == wynik_while