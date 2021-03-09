import unittest
import app

class TestArithmetic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.add(3, 4), 7)

    def test_sub(self):
        self.assertEqual(app.sub(3, 4), -1)

    def test_div(self):
        self.assertEqual(app.div(3, 4), 0.75)

    def test_mul(self):
        self.assertEqual(app.mul(3, 4), 12)

if __name__ == "__main__":
    unittest.main()
