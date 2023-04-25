import unittest
from fibonacci import fibonacci


class FibonacciTest(unittest.TestCase):

    def test_fibonacci_sequence(self):
        self.assertEqual(fibonacci(0), [0])
        self.assertEqual(fibonacci(1), [0, 1])
        self.assertEqual(fibonacci(2), [0, 1, 1])
        self.assertEqual(fibonacci(3), [0, 1, 1, 2])
        self.assertEqual(fibonacci(4), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3, 5])
        self.assertEqual(fibonacci(6), [0, 1, 1, 2, 3, 5])
        self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5])
        self.assertEqual(fibonacci(8), [0, 1, 1, 2, 3, 5, 8])


if __name__ == "__main__":
    unittest.main()