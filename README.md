### Project description

This project is a Flask-based web application designed to predict the class a user falls into (1-5) based on their mobile device usage. The application exposes a single endpoint `/predict` which accepts POST requests containing user data in JSON format. The user data includes various features related to mobile device usage, such as app usage time, screen-on time, battery drain, number of apps installed, data usage, age, gender, and user behavior class.

The prediction is made using a pre-trained machine learning model, which is invoked by the `predict` function. The result of the prediction is returned as a JSON response.

The application is designed to be run using the `waitress` WSGI server for production deployment.

### Endpoint

- **POST /predict**
  - **Request Body**: JSON object containing user data with the following fields:
    - `device_model`: The model of the user's mobile device.
    - `operating_system`: The operating system of the user's mobile device.
    - `app_usage_time(hours/day)`: The average app usage time per day in hours.
    - `screen_on_time(hours/day)`: The average screen-on time per day in hours.
    - `battery_drain(mAh/day)`: The average battery drain per day in mAh.
    - `number_of_apps_installed`: The number of apps installed on the user's device.
    - `data_usage(mb/day)`: The average data usage per day in MB.
    - `age`: The age of the user.
    - `gender`: The gender of the user.
    - `user_behavior_class`: The user behavior class.
  - **Response**: JSON object containing the predicted class.

### Setting Up

#### Clone the repository

```
git clone https://github.com/Jaykold/user-behavior-classification.git
```

#### Navigate to the project directory

```
cd user-behavior-classification
```

### Create a virtual environment

```
python -m venv myenv
```

After creating the virtual environment, you need to activate it:

- On Windows:

```
myenv\Scripts\activate
```

- On macOS and Linux:

```
source myenv/bin/activate
```

You can install the project dependencies by running this command:

```

pip install -r requirements.txt

```

### Running the Application

To run the application, execute the following command:

```

waitress-serve --listen=0.0.0.0:9696 main:app

```

### Building & Running the Docker container

1. Build the docker image using this code

```

docker build -t user-classifer .

```

2. Run the container

```

docker run -it --rm -p 9696:9696 user-classifier

```

3. Test the flask app running this command:

```

python test_url.py

```

4. Push to DockerHub (Optional)

```
docker tag user-classifier <dockerhubName/user-classifier:latest>
```
