import unittest
from unittest.mock import patch
import requests
from yummy_app import YummyApp

class TestYummyApp(unittest.TestCase):
    def setUp(self):
        self.app = YummyApp()

    def test_calculate_total(self):
        cart = [{'price': 50000, 'quantity': 2}, {'price': 30000, 'quantity': 1}]
        self.assertEqual(self.app.calculate_total(cart), 130000)

    # 1. Đóng thế phần cứng GPS
    @patch('yummy_app.get_current_location')
    def test_suggest_restaurants_with_gps(self, mock_gps):
        mock_gps.return_value = "11.9404, 108.4583" # Giả lập có tọa độ GPS
        self.assertEqual(self.app.suggest_restaurants(), ["Nha hang A", "Nha hang B"])

    @patch('yummy_app.get_current_location')
    def test_suggest_restaurants_no_gps(self, mock_gps):
        mock_gps.return_value = None # Giả lập mất tín hiệu GPS
        self.assertEqual(self.app.suggest_restaurants(), [])

    # 2. Giả lập gọi API mạng di động
    @patch('yummy_app.requests.get')
    def test_apply_promo_valid(self, mock_get):
        mock_get.return_value.status_code = 200 # Mạng bình thường, mã đúng
        self.assertTrue(self.app.apply_promo("SALE100"))

    @patch('yummy_app.requests.get')
    def test_apply_promo_invalid(self, mock_get):
        mock_get.return_value.status_code = 404 # Mạng bình thường, mã sai
        self.assertFalse(self.app.apply_promo("SAI_MA"))

    @patch('yummy_app.requests.get')
    def test_apply_promo_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError # Sự cố kết nối mạng
        self.assertFalse(self.app.apply_promo("SALE100"))

if __name__ == '__main__':
    unittest.main()