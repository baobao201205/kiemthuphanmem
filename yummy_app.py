from gps_service import get_current_location
import requests

class YummyApp:
    def calculate_total(self, cart_items):
        return sum(item['price'] * item['quantity'] for item in cart_items)

    def apply_promo(self, code):
        response = requests.get(f"https://api.yummy.com/promo/{code}")
        if response.status_code == 200:
            return True
        return False

    def suggest_restaurants(self):
        location = get_current_location()
        if location:
            return ["Nha hang A", "Nha hang B"]
        return []