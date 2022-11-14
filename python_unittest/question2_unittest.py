import bodmas
import unittest


class TestBodmas(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(bodmas.addition(3, 1), 4)
        self.assertEqual(bodmas.addition(10, 1), 11)
        self.assertEqual(bodmas.addition(3, 1), 4)

    def test_subtraction(self):
        self.assertEqual(bodmas.subtraction(3, 1), 2)
        self.assertEqual(bodmas.subtraction(20, 1), 19)
        self.assertEqual(bodmas.subtraction(3, 1), 2)


if __name__ == "__main__":
    unittest.main()
