def flatSequence(sequence):
    wynik = []

    for item in sequence:
        if isinstance(item, (list, tuple)):
            wynik.extend(flatSequence(item))
        else:
            wynik.append(item)

    return wynik

lista = [1,(2,3),[],[4,(5,6,7)],8,[9]]
wynik1 = flatSequence(lista)
print(wynik1)
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wynik1 == expected