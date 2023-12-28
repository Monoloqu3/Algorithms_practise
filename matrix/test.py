import unittest
from main import matrix

class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertTrue(callable(matrix))

    def test2x2(self):
        m = matrix(2)
        self.assertEqual(2, len(m))
        self.assertEqual([1, 2], m[0])
        self.assertEqual([4, 3], m[1])

    def test3x3(self):
        m = matrix(3)
        self.assertEqual(3, len(m))
        self.assertEqual([1, 2, 3], m[0])
        self.assertEqual([8, 9, 4], m[1])
        self.assertEqual([7, 6, 5], m[2])

    def test4x4(self):
        m = matrix(4)
        self.assertEqual(4, len(m))
        self.assertEqual([1, 2, 3, 4], m[0])
        self.assertEqual([12, 13, 14, 5], m[1])
        self.assertEqual([11, 16, 15, 6], m[2])
        self.assertEqual([10, 9, 8, 7], m[3])

if __name__ == '__main__':
    unittest.main()
