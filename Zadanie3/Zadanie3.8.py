def wspolne_i_wszystkie(x, y):
    wspolne = []
    for el in x:
        if el in y and el not in wspolne:
            wspolne.append(el)

    wszystkie = []
    for el in x + y:
        if el not in wszystkie:
            wszystkie.append(el)

    return wspolne, wszystkie


# testy
result = wspolne_i_wszystkie([1, 2, 3, 2], [2, 3, 4])
expected_result = ([2, 3], [1, 2, 3, 4])
assert result == expected_result

result = wspolne_i_wszystkie(list("abracadabra"), list("banan"))
expected_result = (["a", "b"], ["a", "b", "r", "c", "d", "n"])
assert result == expected_result

# program właściwy
x = list(map(int, input("1 sekwencja: ").split()))
y = list(map(int, input("2 sekwencja: ").split()))
wspolne, wszystkie = wspolne_i_wszystkie(x, y)
print("Wspólne:", wspolne)
print("Wszystkie:", wszystkie)