import requests
from predict import predict
from icecream import ic

url = "http://127.0.0.1:9696/predict"

user_id = "vbj-321"

user_data = {
    "device": "Xiaomi Mi 11",
    "operating_system":	"Android",
    "app_usage_time(hours/day)": 154,
    "screen_on_time(hours/day)": 4.00,
    "battery_drain(mAh/day)": 761,
    "number_of_apps_installed":	32,
    "data_usage(mb/day)": 322,
    "age": 42, 
    "gender": "Male"
}

#response = requests.post(url, json=user_data, timeout=5)

if __name__ == "__main__":
    result = predict(user_data)
    ic(result)