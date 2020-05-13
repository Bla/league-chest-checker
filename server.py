from flask import Flask, json
from flask_cors import CORS
import requests
import config

app = Flask(__name__, static_folder="")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/<string:region>/<string:summoner_name>', methods=['GET'])
def mastery_stats(region, summoner_name):
    API_KEY = config.RIOT_API_KEY
    if region == "br":
        api_url = "https://br1.api.riotgames.com/lol/"
    elif region == "eune":
        api_url = "https://eun1.api.riotgames.com/lol/"
    elif region == "euw":
        api_url = "https://euw1.api.riotgames.com/lol/"
    elif region == "jp":
        api_url = "https://jp1.api.riotgames.com/lol/"
    elif region == "kr":
        api_url = "https://kr.api.riotgames.com/lol/"
    elif region == "lan":
        api_url = "https://la1.api.riotgames.com/lol/"
    elif region == "las":
        api_url = "https://la2.api.riotgames.com/lol/"
    elif region == "na":
        api_url = "https://na1.api.riotgames.com/lol/"
    elif region == "oce":
        api_url = "https://oc1.api.riotgames.com/lol/"
    elif region == "tr":
        api_url = "https://tr1.api.riotgames.com/lol/"
    elif region == "ru":
        api_url = "https://ru.api.riotgames.com/lol/"
    summoner_endpoint = api_url + "summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + API_KEY
    summoner_id = requests.get(summoner_endpoint).json()['id']
    mastery_endpoint = api_url + "champion-mastery/v4/champion-masteries/by-summoner/" + summoner_id + "?api_key=" + API_KEY
    result = requests.get(mastery_endpoint)
    return result.text