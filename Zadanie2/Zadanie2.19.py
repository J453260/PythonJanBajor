L = [1, 22, 333]
string = ""
expected = "001102222333"
for i in L:
    if i > 0 and i < 99:
        string += str(i).zfill(3)

    string += str(i)

print(string)
assert string == expected