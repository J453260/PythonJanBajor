line = "Programowanie w Pythonie jest fajne"

words = line.split()

alfabetycznie = sorted(words)

po_dlugosci = sorted(words, key=len)

print("Alfabetycznie:", alfabetycznie)
print("Po długości:", po_dlugosci)

expected_length = ['Programowanie', 'Pythonie', 'fajne', 'jest', 'w']
assert alfabetycznie == expected_length

expected_length = ['w', 'jest', 'fajne', 'Pythonie', 'Programowanie']
assert po_dlugosci == expected_length