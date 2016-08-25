import requests
import json


def getRequest(url):
    r = requests.get(url)
    return r.json()


def getAllMatchesForToday():
    return getRequest('http://api.football-data.org/v1/fixtures?timeFrame=n1')


def getAllCompetitions():
    return getRequest('http://api.football-data.org/v1/competitions/')
