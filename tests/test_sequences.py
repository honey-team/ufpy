import unittest
from ufpy import ArithmeticProgression, mul


class ArithmeticProgressionTestCase(unittest.TestCase):
    def test_init(self):
        a = ArithmeticProgression(d=1, a1=1) # 1, 2, 3 ...
        b = ArithmeticProgression(a1=1, a2=2)
        self.assertEqual(a, b)

    def test_n(self):
        a = ArithmeticProgression(a1=1, d=10)
        for n in range(1, 11):
            self.assertEqual(a[n], 1 + 10*(n-1))

    def test_s(self):
        a = ArithmeticProgression(a1=1, d=10)
        for m in range(1, 11):
            for n in range(m, 11):
                self.assertEqual(a.s(m, n), (a[m] + a[n]) / 2 * (n-m+1))

    def test_p(self):
        a = ArithmeticProgression(a1=1, d=10)
        for m in range(1, 11):
            for n in range(m, 11):
                l = a[m:n]
                if not isinstance(l, list): l = [l]
                self.assertEqual(a.p(m, n), mul(l))

if __name__ == '__main__':
    unittest.main()
