import inspect
import unittest
from main import Stack


class MyTestCase(unittest.TestCase):

    def test1(self):
        s = Stack()
        s.push(1)
        self.assertEqual(s.pop(), 1)
        s.push(2)
        self.assertEqual(s.pop(), 2)

    def test2(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test3(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.peek(), 3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.peek(), 1)
        self.assertEqual(s.pop(), 1)

    def test4(self):
        self.assertTrue(inspect.isclass(Stack))


if __name__ == '__main__':
    unittest.main()
