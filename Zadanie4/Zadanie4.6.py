def sum_seq(sequence):
    suma = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            suma += sum_seq(item)
        else:
            suma += item
    return suma

wynik = sum_seq([1, 2, 3])
print(wynik)
expected = 6
assert wynik == expected

wynik2 = sum_seq([1, [2, 3], (4, [5, 6]), 7])
expected = 28
print(wynik2)
assert wynik2 == expected