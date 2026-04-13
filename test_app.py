import unittest
from app import greet, farewell

class TestApp(unittest.TestCase):
    def test_greet(self):
        result = greet("Mohit")
        self.assertIn("Mohit", result)
        self.assertIn("AIDI 2004", result)

    def test_farewell(self):
        result = farewell("Mohit")
        self.assertIn("Mohit", result)

if __name__ == "__main__":
    unittest.main()
