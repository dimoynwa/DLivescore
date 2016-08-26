import requests
import json


def getRequest(url):
    headers = {'X-Auth-Token' : 'aaa7793a03be4c5fb76055d8909d2721'}
    r = requests.get(url, headers = headers)
    return r.json()


def getMatchById(id):
    return getRequest('http://api.football-data.org/v1/fixtures/' + (str)(id))


def getAllMatchesForToday():
    return getRequest('http://api.football-data.org/v1/fixtures?timeFrame=n1')


def getAllCompetitions():
    return getRequest('http://api.football-data.org/v1/soccerseasons/')


def getTeamInfo(id):
    return getRequest('http://api.football-data.org/v1/teams/' + (str)(id))
