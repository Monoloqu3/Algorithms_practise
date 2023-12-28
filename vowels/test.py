import unittest
from main import vowels


class MyTestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(callable(vowels))

    def test2(self):
        self.assertEqual(5, vowels('aeiou'))

    def test3(self):
        self.assertEqual(5, vowels('AEIOU'))

    def test4(self):
        self.assertEqual(0, vowels('bcdfghjkl'))

    def test5(self):
        self.assertEqual(3, vowels('Hi There!'))

    def test6(self):
        self.assertEqual(4, vowels('Why do you ask?'))

    def test7(self):
        self.assertEqual(0, vowels('Why?'))

if __name__ == '__main__':
    unittest.main()
