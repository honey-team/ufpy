import unittest

from ufpy import UDict


class UDictTestCase(unittest.TestCase):
    def test_init(self):
        d = UDict(hello=1, hi='world', default=10)
        d2 = UDict({'hello': 1, 'hi': 'world'})
        d3 = UDict()
        self.assertEqual(d.default, 10)
        self.assertEqual(d2.default, None)
        self.assertEqual(d3.default, None)

        self.assertDictEqual(d.dictionary, d2.dictionary)
        self.assertDictEqual(d3.dictionary, {})

        self.assertEqual(d, d2)
        self.assertNotEqual(d, d3)
        self.assertNotEqual(d2, d3)

    def test_keys_values_items(self):
        d = UDict(hello=1, hi=2)

        self.assertEqual(d.keys, list(d.dictionary.keys()))
        self.assertEqual(d.values, list(d.dictionary.values()))
        self.assertEqual(d.items, list(d.dictionary.items()))

    def test_call(self):
        d = {'hello': 1, 'hi': 2}
        ud = UDict(d)

        d2 = d

        for k, v in d2.items():
            d2[k] = v * 2

        ud2 = ud(lambda k, v: v * 2)

        self.assertDictEqual(d2, ud2.dictionary)

    def test_reverse(self):
        d = {'hello': 1, 'hi': 2}
        ud = UDict(d)

        keys, values = list(d.keys())[::-1], list(d.values())[::-1]
        d2 = dict(list(zip(keys, values)))

        self.assertDictEqual(d2, ud.reversed().dictionary)
        self.assertEqual(reversed(ud), ud.reversed())
        self.assertEqual(~ud, ud.reverse())

    def test_sort(self):
        d = {'hi': 2, 'hello': 1}
        ud = UDict(d)
        sd = {'hello': 1, 'hi': 2}
        sud = UDict(sd)

        self.assertDictEqual(ud.sorted().dictionary, sd)
        self.assertEqual(sorted(ud), sud.items)
        self.assertEqual(ud.sorted(), ud.sort())

    def test_get_item(self):
        d = UDict(hello=1, hi=2)

        self.assertEqual(d['hi'], 2)
        self.assertEqual(d[1], 1)
        self.assertEqual(d[1:2], d.values)

        self.assertEqual(d[-2:], d.values)

        self.assertEqual(d[1], d['hello'])

        # not existent key
        self.assertEqual(d['hey'], None)

    def test_set_item(self):
        d = UDict(hello=1, hi=2)
        d['hi'] = 3
        self.assertDictEqual(d.dictionary, {'hello': 1, 'hi': 3})

        d[1] = 4
        self.assertDictEqual(d.dictionary, {'hello': 4, 'hi': 3})

        d[:] = [1, 2]
        self.assertDictEqual(d.dictionary, {'hello': 1, 'hi': 2})

    def test_del_item(self):
        d = UDict(hello=1, hi=2)
        del d[1]
        self.assertDictEqual(d.dictionary, {'hi': 2})
        del d[:]
        self.assertDictEqual(d.dictionary, {})

    def test_get(self):
        d = UDict({2: 1, 4: 91, 1: 12}, default=None)
        self.assertEqual(d.get(index=1), d.get(key=2))
        self.assertEqual(d.get(index=2), d.get(key=4))
        self.assertEqual(d.get(index=3), d.get(key=1))

        self.assertEqual(d.get(value=1), 2)
        self.assertEqual(d.get(value=91), 4)
        self.assertEqual(d.get(value=12), 1)

        self.assertEqual(d.get(key=3, default='missing'), 'missing')
        self.assertEqual(d.get(key=3), None)
        self.assertEqual(d.get(value=3, default='missing'), 'missing')
        self.assertEqual(d.get(value=3), None)

        with self.assertRaises(ValueError):
            d.get()
        with self.assertRaises(ValueError):
            d.get(index=2, value=1)
        with self.assertRaises(ValueError):
            d.get(index=2, key=2)
        with self.assertRaises(ValueError):
            d.get(value=1, key=4)
        with self.assertRaises(ValueError):
            d.get(value=1, key=4, index=3)
        with self.assertRaises(IndexError):
            d.get(index=4)

    def test_len_and_iter(self):
        d = UDict(hello=1, hi=2)
        self.assertEqual(len(d), 2)

        l = []
        for k, v in d:
            l.append((k, v))

        self.assertEqual(l, [
            ('hello', 1), ('hi', 2)
        ])

    def test_nonzero(self):
        d = UDict(hello=1, hi=2)
        self.assertTrue(bool(d))

    def test_contains(self):
        d = UDict(hello=1, hi=2)
        self.assertTrue('hello' in d)
        self.assertTrue('hi' in d)

        self.assertTrue(('hello', 1) in d)
        self.assertFalse(('hello', 2) in d)

        self.assertTrue(('hi', 2) in d)
        self.assertFalse(('hi', 1) in d)

    def test_str_and_repr(self):
        d = {'hello': 1, 'hi': 2}
        ud = UDict(d)

        self.assertEqual(str(ud), str(d))
        self.assertEqual(repr(ud), f'u{repr(d)}')

    def test_cmp_and_eq(self):
        d = {'hello': 1, 'hi': 2}
        ud = UDict(d)

        ud2 = UDict(hello=1, hi=2, world=3)

        self.assertTrue(ud2 != ud)
        self.assertTrue(ud2 > ud)
        self.assertTrue(ud2 >= ud)
        self.assertTrue(ud < ud2)
        self.assertTrue(ud <= ud2)

        self.assertEqual(d, ud)

    def test_math_operations(self):
        d = UDict(hello=1, hi=2)

        self.assertEqual(d + {'world': 3}, UDict(hello=1, hi=2, world=3))
        self.assertEqual(d - {'hi': 2}, UDict(hello=1))

        self.assertEqual(d * 2, UDict(hello=2, hi=4))
        self.assertEqual(d / 2, UDict(hello=0.5, hi=1))

    def test_neg(self):
        d = UDict(hello=1, hi=2)
        self.assertEqual((-d).dictionary, {'hello': -1, 'hi': -2})


if __name__ == '__main__':
    unittest.main()
