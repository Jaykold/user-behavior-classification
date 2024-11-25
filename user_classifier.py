from flask import Flask, request, jsonify
from predict import predict
import waitress

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_user():
    # Get the data from the POST request
    user_data = request.get_json()
    
    # Make the prediction
    prediction = predict(user_data)

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(port=9696, host='0.0.0.0')