import unittest
from yummy_app import YummyApp

class TestYummyApp(unittest.TestCase):
    def setUp(self):
        self.app = YummyApp()

    def test_calculate_total(self):
        cart = [{'price': 50000, 'quantity': 2}, {'price': 30000, 'quantity': 1}]
        self.assertEqual(self.app.calculate_total(cart), 130000)

if __name__ == '__main__':
    unittest.main()