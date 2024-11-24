import pickle
from typing import Dict

model_path = "model/lr.bin"
preprocessor_path = "model/preprocessor.bin"

user_data = {
    'device_model': 'Samsung Galaxy S21',
    'operating_system': 'Android',
    'app_usage_time(hours/day)': 5.066666666666666,
    'screen_on_time(hours/day)': 6.5,
    'battery_drain(mAh/day)': 2375,
    'number_of_apps_installed': 79,
    'data_usage(mb/day)': 1493,
    'age': 51,
    'gender': 'Male'
}

with open(model_path, 'rb') as model_file, open(preprocessor_path, "rb") as preprocessor_file:
    model = pickle.load(model_file)
    dv, le = pickle.load(preprocessor_file)

def predict(user):
    if not isinstance(user, Dict):
        raise ValueError("Input must be a Dictionary.")
    
    data = dv.transform([user])
    y_pred = model.predict(data)

    return le.inverse_transform(y_pred)[0]

# if __name__ == "__main__":
#     ic(predict(user_data))