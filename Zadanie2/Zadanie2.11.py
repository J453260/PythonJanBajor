slowo = "word"
output = ""
for i, znak in enumerate(slowo):
    if i == len(slowo) - 1:
        print(znak, end="")
        output = output + znak
    else:
        print(znak + "_", end="")
        output = output + znak + "_"

expected = "w_o_r_d"
assert output == expected
