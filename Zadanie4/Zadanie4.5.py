def odwracanie(L, left, right):
    L = L[:]
    L[left:right] = L[left:right][::-1]
    return L

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
left = 0
right = 5
wynik = odwracanie(L, left, right)
print(wynik)
expected = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
assert wynik == expected