from gps_service import get_current_location
import requests

class YummyApp:
    def calculate_total(self, cart_items):
        return sum(item['price'] * item['quantity'] for item in cart_items)

    def apply_promo(self, code):
        try:
            response = requests.get(f"https://api.yummy.com/promo/{code}")
            if response.status_code == 200:
                return True
            return False
        except requests.exceptions.ConnectionError:
            # Xử lý khi mất kết nối mạng di động
            return False

    def suggest_restaurants(self):
        location = get_current_location()
        if location:
            return ["Nha hang A", "Nha hang B"]
        return []
    def ham_loi_cu_phap()
    print("Loi roi")