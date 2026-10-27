X = "qwerty"

def func1():
    print("X: ", X)

func1()
# X tutaj jest zmienną globalną



Y = "qwerty"

def func2():
    Y = "abc"

func2()
print("Y: ", Y)
# Y = "abc" jest zmienną lokalną i nie ulega zmianie wewnątrz funkcji


Z = "qwerty"

def func3():
    global Z
    Z = "abc"

func3()
print("Z: ", Z)
# Dzięki global funkcja modyfikuje zmienną globalną Z