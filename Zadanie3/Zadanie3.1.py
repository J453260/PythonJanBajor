"""
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
for i in "axby": if ord(i) < 100: print (i)
for i in "axby": print (ord(i) if ord(i) < 100 else i)
"""


"""
Powyższy kod nie jest poprawny, ponieważ po for i in "axby": if powinien być w następnej
linii.

Poprawiony kod:
"""

x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
for i in "axby":
    if ord(i) < 100: print (i)
for i in "axby": print (ord(i) if ord(i) < 100 else i)