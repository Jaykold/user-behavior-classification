import pickle

model_path = "model/lr.bin"
preprocessor_path = "model/preprocessor.bin"


with open(model_path, 'rb') as model_file, open(preprocessor_path, "rb") as preprocessor_file:
    model = pickle.load(model_file)
    dv, le = pickle.load(preprocessor_file)

def predict(user):
    if not isinstance(user, dict):
        raise ValueError("Input must be a Dictionary.")
    
    data = dv.transform([user])
    y_pred = model.predict(data)

    return le.inverse_transform(y_pred)[0]