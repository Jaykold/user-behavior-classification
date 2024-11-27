import requests
from icecream import ic

url = "https://userclassifier.azurewebsites.net/predict"

user_data = {
    "device": "Google Pixel 5",
    "operating_system": "Android",
    "app_usage_time(hours/day)": 239,
    "screen_on_time(hours/day)": 4.80,
    "battery_drain(mAh/day)": 1676,
    "number_of_apps_installed": 56,
    "data_usage(mb/day)": 871,
    "age": 20,
    "gender": "Female",
}

try:
    response = requests.post(url, json=user_data, timeout=5).json()
    ic(response)
except requests.exceptions.RequestException as e:
    ic(f"Request Error: {e}")
except Exception as e:
    ic(f"Unexpected Error: {e}")