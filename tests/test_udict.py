import unittest

from ufpy import UDict


class UDictTestCase(unittest.TestCase):
    def test_init(self):
        d = UDict(hello=1, hi=2, default=10)
        d2 = UDict({'hello': 1, 'hi': 2})
        self.assertEqual(d.default, 10)
        self.assertDictEqual(d.dictionary, d2.dictionary)
        self.assertEqual(d, d2)

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
        self.assertEqual(-ud, ud.reverse())

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

    def test_set_item(self):
        d = UDict(hello=1, hi=2)
        d['hi'] = 3
        self.assertDictEqual(d.dictionary, {'hello': 1, 'hi': 3})

        d[1] = 4
        self.assertDictEqual(d.dictionary, {'hello': 4, 'hi': 3})

        d[:] = [1, 2]
        self.assertDictEqual(d.dictionary, {'hello': 1, 'hi': 2})

    def test_get(self):
        d = UDict({2: 1, 4: 91, 1: 12})
        self.assertEqual(d.get(index=1), d.get(key=2))
        self.assertEqual(d.get(index=2), d.get(key=4))
        self.assertEqual(d.get(index=3), d.get(key=1))

    # TODO: test_del_item
    # TODO: test_len_and_iter
    # TODO: test_bool
    # TODO: test_contains
    # TODO: test_str_and_repr
    # TODO: test_cmp_and_eq
    # TODO: test_math_operations


if __name__ == '__main__':
    unittest.main()
