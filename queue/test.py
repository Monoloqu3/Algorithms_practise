import unittest
import inspect
from main import Queue

class MyTestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(inspect.isclass(Queue))

    def test2(self):
        q = Queue()
        self.assertRaises(Exception, q.add(1))

    def test3(self):
        q = Queue()
        self.assertRaises(Exception, q.add(1))
        self.assertRaises(Exception, q.remove())

    def test4(self):
        q = Queue()
        q.add(1)
        q.add(2)
        q.add(3)
        self.assertEqual(1, q.remove())
        self.assertEqual(2, q.remove())
        self.assertEqual(3, q.remove())
        self.assertEqual(None, q.remove())

if __name__ == '__main__':
    unittest.main()
