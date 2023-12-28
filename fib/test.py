import unittest
from main import fib


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(1, fib(1))
        self.assertEqual(1, fib(2))
        self.assertEqual(2, fib(3))
        self.assertEqual(3, fib(4))
        self.assertEqual(63245986, fib(39))


if __name__ == '__main__':
    unittest.main()
