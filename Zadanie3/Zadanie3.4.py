def szescian(tekst):
    return float(tekst) ** 3


# testy
result = szescian("2")
expected_result = 8.0
assert result == expected_result

assert szescian("-3") == -27.0
assert szescian("0") == 0.0
assert szescian("1.5") == 3.375

# program właściwy
while True:
    x = input("Podaj liczbę (lub 'stop' aby zakończyć): ")
    if x.strip().lower() == "stop":
        break
    y = szescian(x)
    print(y)