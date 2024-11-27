import requests
from icecream import ic

url = "http://localhost:9696/predict"

user_data = {
    "device": "Google Pixel 5",
    "operating_system":	"Android",
    "app_usage_time(hours/day)": 393,
    "screen_on_time(hours/day)": 6.40,
    "battery_drain(mAh/day)": 1331,
    "number_of_apps_installed":	62,
    "data_usage(mb/day)": 944,
    "age": 25,
    "gender": "Male",
}

try:
    response = requests.post(url, json=user_data, timeout=5).json()
    ic(response)
except requests.exceptions.RequestException as e:
    ic(f"Request Error: {e}")
except Exception as e:
    ic(f"Unexpected Error: {e}")