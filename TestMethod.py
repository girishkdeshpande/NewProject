import unittest


class MyTestCase(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('girish'.upper(), 'GIRISH')

    def test_isupper(self):
        self.assertTrue('GIRISH'.isupper())
        self.assertFalse('girish'.isupper())


if __name__ == '__main__':
    unittest.main()
