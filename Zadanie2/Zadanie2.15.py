L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
string = ""
for i in L:
    string = string + str(i)

expected_result = "12345678910"
print(string)
assert string == expected_result