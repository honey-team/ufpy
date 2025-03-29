import unittest
from ufpy import ArithmeticProgression, GeometricProgression, Fibonacci
import numpy as np


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
                l = a[m:n]
                if not isinstance(l, list): l = [l]
                self.assertEqual(a.s(m, n), np.sum(l))

    def test_p(self):
        a = ArithmeticProgression(a1=1, d=10)
        for m in range(1, 11):
            for n in range(m, 11):
                l = a[m:n]
                if not isinstance(l, list): l = [l]
                self.assertEqual(a.p(m, n), np.prod(l))

    def test_zero_and_negative_indices(self):
        a = ArithmeticProgression(a1=1, d=10)
        self.assertEqual(a[0], 1 - 10)
        self.assertEqual(a[-1], 1 - 20)

    def test_missing_a1_only(self):
        with self.assertRaises(ValueError):
            ArithmeticProgression(a1=1)

    def test_missing_d_only(self):
        with self.assertRaises(ValueError):
            ArithmeticProgression(d=1)

    def test_conflict_init(self):
        with self.assertRaises(Exception):
            ArithmeticProgression(a1=1, a2=3, d=1)

class GeometricProgressionTestCase(unittest.TestCase):
    def test_init(self):
        a = GeometricProgression(b1=1, q=2)
        b = GeometricProgression(b2=2, q=2)
        self.assertEqual(a, b)

    def test_n(self):
        b = GeometricProgression(b1=1, q=2)
        for n in range(1, 11):
            self.assertEqual(b[n], 2**(n-1))

    def test_s(self):
        b = GeometricProgression(b1=1, q=2)
        for m in range(1, 11):
            for n in range(m, 11):
                l = b[m:n]
                if not isinstance(l, list): l = [l]
                self.assertEqual(b.s(m, n), np.sum(l))

    def test_p(self):
        b = GeometricProgression(b1=1, q=2)
        for m in range(1, 11):
            for n in range(m, 11):
                l = b[m:n]
                if not isinstance(l, list): l = [l]
                self.assertEqual(b.p(m, n), np.prod(l))


class FibonacciTestCase(unittest.TestCase):
    def test_n_and_iter(self):
        f = Fibonacci()
        ft = [1, 1, 2, 3, 5, 8, 13]

        for t, r in zip(ft, f):
            self.assertEqual(t, r)

    def test_s(self):
        f = Fibonacci()
        for m in range(1, 11):
            for n in range(m, 11):
                l = f[m:n]
                if not isinstance(l, list): l = [l]
                self.assertEqual(f.s(m, n), np.sum(l))

    def test_p(self):
        f = Fibonacci()
        for m in range(1, 11):
            for n in range(m, 11):
                l = f[m:n]
                if not isinstance(l, list): l = [l]
                self.assertEqual(f.p(m, n), np.prod(l))


if __name__ == '__main__':
    unittest.main()
