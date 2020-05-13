from flask import Flask, json, jsonify
from flask_cors import CORS, cross_origin
import requests
import config

app = Flask(__name__, static_folder="")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/<string:region>/<string:summoner_name>', methods=['GET'])
def mastery_stats(region, summoner_name):
    API_KEY = config.RIOT_API_KEY
    if region == "br":
        api_region = "br1"
    elif region == "eune":
        api_region = "eun1"
    elif region == "euw":
        api_region = "euw1"
    elif region == "jp":
        api_region = "jp1"
    elif region == "kr":
        api_region = "kr"
    elif region == "lan":
        api_region = "la1"
    elif region == "las":
        api_region = "la2"
    elif region == "na":
        api_region = "na1"
    elif region == "oce":
        api_region = "oc1"
    elif region == "tr":
        api_region = "tr1"
    elif region == "ru":
        api_region = "ru"
    api_url = "https://" + api_region + ".api.riotgames.com/lol/"
    summoner_endpoint = api_url + "summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + API_KEY
    summoner_id = requests.get(summoner_endpoint).json()['id']
    mastery_endpoint = api_url + "champion-mastery/v4/champion-masteries/by-summoner/" + summoner_id + "?api_key=" + API_KEY
    result = requests.get(mastery_endpoint)
    return result.text
