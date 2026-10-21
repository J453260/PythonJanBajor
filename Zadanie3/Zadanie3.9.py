def sumy(dane):
    return [sum(seq) for seq in dane]

result = sumy([[], [4], (1, 2), [3, 4], (5, 6, 7)])
print(result)
expected_result = [0, 4, 3, 7, 18]
assert result == expected_result