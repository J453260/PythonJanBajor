line = "Język Python został stworzony przez GvR."

nowy_line = line.replace("GvR", "Guido van Rossum")

assert "GvR" not in nowy_line
assert "Guido van Rossum" in nowy_line

print(nowy_line)