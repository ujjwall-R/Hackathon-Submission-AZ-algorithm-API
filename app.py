from flask import Flask, request, jsonify
from storage import DBStorage
from requests.exceptions import RequestException
import pandas as pd
from datetime import datetime
from workers import GetRecommendations, ViewTracker, AddRecommendations

app = Flask(__name__)


@ app.route("/getRecommendations", methods=['GET'])
def recommend():
    return GetRecommendations()


@ app.route("/addRatings", methods=['POST'])
def addRatings():
    AddRecommendations()
    return


if __name__ == '__main__':
    # debug mode
    app.run(host='0.0.0.0', debug=True, port=6060)
