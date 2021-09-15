import unittest
from main import elem_sum

class MyTestCase(unittest.TestCase):
    def test_elem_sum(self):
        a, b = 2, 3
        output = elem_sum(a, b)
        self.assertEqual(output, 1)

if __name__ == '__main__':
    unittest.main()
