import unittest

def trim(poly):
    # usuwa zera z końca, [] zamienia na [0]
    poly = poly[:]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly or [0]

def add_poly(poly1, poly2):        # poly1(x) + poly2(x)
    n = max(len(poly1), len(poly2))
    a = poly1 + [0] * (n - len(poly1))
    b = poly2 + [0] * (n - len(poly2))
    return trim([a[i] + b[i] for i in range(n)])

    return poly3

def sub_poly(poly1, poly2):        # poly1(x) - poly2(x)
    n = max(len(poly1), len(poly2))
    a = poly1 + [0] * (n - len(poly1))
    b = poly2 + [0] * (n - len(poly2))
    return trim([a[i] - b[i] for i in range(n)])

    return poly3

def mul_poly(poly1, poly2):        # poly1(x) * poly2(x)
    wynik = [0] * (len(poly1) + len(poly2) - 1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            wynik[i + j] += poly1[i] * poly2[j]
    return trim(wynik)

def is_zero(poly):                 # bool, [0], [0,0], itp.
    return all(c == 0 for c in poly)

def eq_poly(poly1, poly2):        # bool, porównywanie poly1(x) == poly2(x)
    return trim(poly1) == trim(poly2)

def eval_poly(poly, x0):           # poly(x0), algorytm Hornera
    wynik = 0
    for c in reversed(poly):
        wynik = wynik * x0 + c
    return wynik

def combine_poly(poly1, poly2):    # poly1(poly2(x)), trudne!
    wynik = [0]
    for c in reversed(poly1):
        wynik = add_poly(mul_poly(wynik, poly2), [c])
    return wynik

def pow_poly(poly, n):             # poly(x) ** n
    wynik = [1]
    for _ in range(n):
        wynik = mul_poly(wynik, poly)
    return wynik

def diff_poly(poly):               # pochodna wielomianu
    if len(poly) <= 1:
        return [0]
    return trim([i * poly[i] for i in range(1, len(poly))])

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x^2

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])
        # różne długości i element neutralny
        self.assertEqual(add_poly([1, 2], [3, 1, 1]), [4, 3, 1])
        self.assertEqual(add_poly(self.p1, [0]), self.p1)

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p2, self.p1), [0, -1, 1])
        # wielomian minus on sam = zero (po trim)
        self.assertEqual(sub_poly(self.p1, self.p1), [0])
        # zera na końcu są usuwane
        self.assertEqual(sub_poly([1, 2, 3], [0, 0, 3]), [1, 2])

    def test_mul_poly(self):
        # x * x^2 = x^3
        self.assertEqual(mul_poly(self.p1, self.p2), [0, 0, 0, 1])
        # (1 + x)(1 - x) = 1 - x^2
        self.assertEqual(mul_poly([1, 1], [1, -1]), [1, 0, -1])
        # mnożenie przez 1 i przez 0
        self.assertEqual(mul_poly(self.p1, [1]), self.p1)
        self.assertEqual(mul_poly(self.p1, [0]), [0])

    def test_is_zero(self):
        self.assertTrue(is_zero([0]))
        self.assertTrue(is_zero([0, 0, 0]))
        self.assertFalse(is_zero(self.p1))
        self.assertFalse(is_zero([0, 0, 5]))

    def test_eq_poly(self):
        self.assertTrue(eq_poly([1, 2], [1, 2]))
        self.assertTrue(eq_poly([1, 2], [1, 2, 0]))   # zera na końcu nie mają znaczenia
        self.assertFalse(eq_poly(self.p1, self.p2))

    def test_eval_poly(self):
        # 1 + 2x + 3x^2 dla x = 2: 1 + 4 + 12 = 17
        self.assertEqual(eval_poly([1, 2, 3], 2), 17)
        self.assertEqual(eval_poly(self.p1, 5), 5)     # x w punkcie 5
        self.assertEqual(eval_poly(self.p2, 3), 9)     # x^2 w punkcie 3
        self.assertEqual(eval_poly([7], 100), 7)       # stała
        self.assertEqual(eval_poly([1, 2, 3], 0), 1)   # wyraz wolny

    def test_combine_poly(self):
        # f(x) = x^2, g(x) = x + 1  ->  f(g(x)) = 1 + 2x + x^2
        self.assertEqual(combine_poly(self.p2, [1, 1]), [1, 2, 1])
        # f(x) = x, g(x) = x^2  ->  x^2
        self.assertEqual(combine_poly(self.p1, self.p2), self.p2)
        # złożenie z x nic nie zmienia
        self.assertEqual(combine_poly([1, 2, 3], self.p1), [1, 2, 3])

    def test_pow_poly(self):
        # (1 + x)^3 = 1 + 3x + 3x^2 + x^3
        self.assertEqual(pow_poly([1, 1], 3), [1, 3, 3, 1])
        self.assertEqual(pow_poly(self.p1, 2), self.p2)   # x^2
        self.assertEqual(pow_poly([5, 7], 0), [1])        # dowolny wielomian do potęgi 0
        self.assertEqual(pow_poly([5, 7], 1), [5, 7])

    def test_diff_poly(self):
        # (1 + 2x + 3x^2)' = 2 + 6x
        self.assertEqual(diff_poly([1, 2, 3]), [2, 6])
        self.assertEqual(diff_poly(self.p1), [1])         # x' = 1
        self.assertEqual(diff_poly(self.p2), [0, 2])      # (x^2)' = 2x
        self.assertEqual(diff_poly([5]), [0])             # pochodna stałej

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy