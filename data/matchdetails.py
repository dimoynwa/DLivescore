from data.match import Match
from data import api_connection
import requests


class MatchDetails:
    def __init__(self, json):
        self.match = Match(json['fixture'])
        self.oldMatches = json['head2head']['count']
        self.homeTeamWins = json['head2head']['homeTeamWins']
        self.awayTeamWins = json['head2head']['awayTeamWins']
        self.draws = json['head2head']['draws']
        self.previous = []
        for js in json['head2head']['fixtures']:
            m = Match(js)
            m.status = 'FINISHED'
            self.previous.append(m)

    def printMatchDetails(self):
        print('\nFixture with ID ' + (str)(self.match.matchId) + '\n')
        print((str)(self.match)+ '\n')
        print(self.match.printMatchOdds())
        print('Previous matches : ' + (str)(self.oldMatches))
        print(self.match.homeTeamName + ' wins : ' + (str)(self.homeTeamWins))
        print(self.match.awayTeamName + ' wins : ' + (str)(self.awayTeamWins))
        print('Draws : ' + (str)(self.draws))
        print('\nPrevious matches : \n')
        for match in self.previous:
            print((str)(match))
