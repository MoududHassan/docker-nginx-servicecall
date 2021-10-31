from flask import request, Flask
import json
import requests

app = Flask(__name__)
@app.route('/')


def hello_world():
    return 'Salam alikom, this is App1 :)'

@app.route("/get_app2_data")
def get_app2_data():
	response = requests.get(url="http://172.17.0.3:5000/")
	return response.content


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')