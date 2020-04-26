from flask import Flask, json, jsonify
from flask_cors import CORS, cross_origin
import requests
import config

app = Flask(__name__, static_folder="")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# GET request where <str> is the summoner's name
@app.route('/api/<str>', methods=['GET'])
def mastery(str):
    API_KEY = config.RIOT_API_KEY
    summoner_endpoint = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str + "?api_key=" + API_KEY
    summoner_id = requests.get(summoner_endpoint).json()['id']
    mastery_endpoint = "https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summoner_id + "?api_key=" + API_KEY
    r = requests.get(mastery_endpoint)
    return r.text