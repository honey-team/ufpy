import unittest
from io import BytesIO

from ujson import loads, dumps

from ufpy import JsonFileUpdater


class JsonFileUpdaterTestCase(unittest.TestCase):
    def test_write_one_dict(self):
        b = BytesIO()
        d = {
            'test1': '1', 'test2': 2,
            'test3': True, 'test4': None
        }
        with JsonFileUpdater(b) as j:
            j['test1'] = '1'
            j['test2'] = 2
            j['test3'] = True
            j['test4'] = None

        self.assertEqual(d, loads(b.getvalue().decode('utf-8')))

    def test_write_several_dicts(self):
        b = BytesIO()
        d = {
            'test1': {'test2': 3},
            'test3': {'test4': {'test5': 1} }
        }
        with JsonFileUpdater(b) as j:
            j['test1 / test2'] = 3
            j['test3 / test4 / test5'] = 1

        self.assertEqual(d, loads(b.getvalue().decode('utf-8')))

    def test_load_one_dict(self):
        d = {
            'test1': '1', 'test2': 2,
            'test3': True, 'test4': None
        }
        b = BytesIO(dumps(d).encode('utf-8'))
        with JsonFileUpdater(b) as j:
            self.assertEqual(d['test1'], j['test1'])
            self.assertEqual(d['test2'], j['test2'])
            self.assertEqual(d['test3'], j['test3'])
            self.assertEqual(d['test4'], j['test4'])

    def test_load_several_dicts(self):
        d = {
            'test1': {'test2': 3},
            'test3': {'test4': {'test5': 1}}
        }
        b = BytesIO(dumps(d).encode('utf-8'))
        with JsonFileUpdater(b) as j:
            self.assertEqual(j['test1 / test2'], d['test1']['test2'])
            self.assertEqual(j['test3 / test4 / test5'], d['test3']['test4']['test5'])

if __name__ == '__main__':
    unittest.main()
