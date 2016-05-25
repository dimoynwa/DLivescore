import json
import requests

__url = 'http://api.football-data.org/v1/'


def get_all_fixtures():
    url = __url + 'fixtures'
    r = requests.get(url)
    return r.json()


def get_fixture(fixture_id):
    url = __url + 'fixtures/' + str(fixture_id)
    r = requests.get(url)
    return r.json()


def get_all_socerseason():
    url = __url + 'soccerseasons'
    r = requests.get(url)
    return r.json()


def get_soccereason(season_id):
    url = __url + 'soccerseasons/' + str(season_id)
    r = requests.get(url)
    return r.json()


def get_team(team_id):
    url = __url + 'teams/' + str(team_id)
    r = requests.get(url)
    return r.json()
