from flask import Flask, json, jsonify
from flask_cors import CORS, cross_origin
import requests
import config

app = Flask(__name__, static_folder="")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# GET request where <str> is the summoner's name
@app.route('/api/br/<str>', methods=['GET'])
def br_mastery(str):
    API_KEY = config.RIOT_API_KEY
    summoner_endpoint = "https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str + "?api_key=" + API_KEY
    summoner_id = requests.get(summoner_endpoint).json()['id']
    mastery_endpoint = "https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summoner_id + "?api_key=" + API_KEY
    r = requests.get(mastery_endpoint)
    return r.text

@app.route('/api/eune/<str>', methods=['GET'])
def eune_mastery(str):
    API_KEY = config.RIOT_API_KEY
    summoner_endpoint = "https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str + "?api_key=" + API_KEY
    summoner_id = requests.get(summoner_endpoint).json()['id']
    mastery_endpoint = "https://eun1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summoner_id + "?api_key=" + API_KEY
    r = requests.get(mastery_endpoint)
    return r.text

@app.route('/api/euw/<str>', methods=['GET'])
def euw_mastery(str):
    API_KEY = config.RIOT_API_KEY
    summoner_endpoint = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str + "?api_key=" + API_KEY
    summoner_id = requests.get(summoner_endpoint).json()['id']
    mastery_endpoint = "https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summoner_id + "?api_key=" + API_KEY
    r = requests.get(mastery_endpoint)
    return r.text

@app.route('/api/jp/<str>', methods=['GET'])
def jp_mastery(str):
    API_KEY = config.RIOT_API_KEY
    summoner_endpoint = "https://jp1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str + "?api_key=" + API_KEY
    summoner_id = requests.get(summoner_endpoint).json()['id']
    mastery_endpoint = "https://jp1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summoner_id + "?api_key=" + API_KEY
    r = requests.get(mastery_endpoint)
    return r.text

@app.route('/api/kr/<str>', methods=['GET'])
def kr_mastery(str):
    API_KEY = config.RIOT_API_KEY
    summoner_endpoint = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str + "?api_key=" + API_KEY
    summoner_id = requests.get(summoner_endpoint).json()['id']
    mastery_endpoint = "https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summoner_id + "?api_key=" + API_KEY
    r = requests.get(mastery_endpoint)
    return r.text

@app.route('/api/lan/<str>', methods=['GET'])
def lan_mastery(str):
    API_KEY = config.RIOT_API_KEY
    summoner_endpoint = "https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str + "?api_key=" + API_KEY
    summoner_id = requests.get(summoner_endpoint).json()['id']
    mastery_endpoint = "https://la1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summoner_id + "?api_key=" + API_KEY
    r = requests.get(mastery_endpoint)
    return r.text

@app.route('/api/las/<str>', methods=['GET'])
def las_mastery(str):
    API_KEY = config.RIOT_API_KEY
    summoner_endpoint = "https://la2.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str + "?api_key=" + API_KEY
    summoner_id = requests.get(summoner_endpoint).json()['id']
    mastery_endpoint = "https://la2.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summoner_id + "?api_key=" + API_KEY
    r = requests.get(mastery_endpoint)
    return r.text

@app.route('/api/na/<str>', methods=['GET'])
def na_mastery(str):
    API_KEY = config.RIOT_API_KEY
    summoner_endpoint = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str + "?api_key=" + API_KEY
    summoner_id = requests.get(summoner_endpoint).json()['id']
    mastery_endpoint = "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summoner_id + "?api_key=" + API_KEY
    r = requests.get(mastery_endpoint)
    return r.text

@app.route('/api/oce/<str>', methods=['GET'])
def oce_mastery(str):
    API_KEY = config.RIOT_API_KEY
    summoner_endpoint = "https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str + "?api_key=" + API_KEY
    summoner_id = requests.get(summoner_endpoint).json()['id']
    mastery_endpoint = "https://oc1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summoner_id + "?api_key=" + API_KEY
    r = requests.get(mastery_endpoint)
    return r.text

@app.route('/api/tr/<str>', methods=['GET'])
def tr_mastery(str):
    API_KEY = config.RIOT_API_KEY
    summoner_endpoint = "https://tr1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str + "?api_key=" + API_KEY
    summoner_id = requests.get(summoner_endpoint).json()['id']
    mastery_endpoint = "https://tr1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summoner_id + "?api_key=" + API_KEY
    r = requests.get(mastery_endpoint)
    return r.text

@app.route('/api/ru/<str>', methods=['GET'])
def ru_mastery(str):
    API_KEY = config.RIOT_API_KEY
    summoner_endpoint = "https://ru.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str + "?api_key=" + API_KEY
    summoner_id = requests.get(summoner_endpoint).json()['id']
    mastery_endpoint = "https://ru.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summoner_id + "?api_key=" + API_KEY
    r = requests.get(mastery_endpoint)
    return r.text