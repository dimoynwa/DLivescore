import requests
import data.api_connection
from data.player import Player


class TeamDetails:
    def __init__(self, json):
        self.name = json['name']
        self.value = json['squadMarketValue']
        self.playersLink = json['_links']['players']['href']
        self.players = []
        self.loadPlayers()

    def loadPlayers(self):
        try:
            r = data.api_connection.getRequest(self.playersLink)
        except requests.exceptions.RequestException as e:
            print(e)
            return
        for pl in r['players']:
            self.players.append(Player(pl))

    def printTeamDetails(self):
        print('\n' + self.name + '\n')
        print('Squad market value : ' + (str)(self.value) + '\n')
        print('Squad : \n')
        for p in self.players:
            print((str)(p))
        
