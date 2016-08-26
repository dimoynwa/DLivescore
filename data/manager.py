import data.api_connection
import requests
from data.league import League
from data.match import Match
from data.matchdetails import MatchDetails
from data.teamdetails import TeamDetails
import time
import _thread

class Controller:
    def __init__(self):
        self.matches = {}
        self.loadMatches()
        self.favourites = []
        self.loadFavourites()
        self.leagues = {}
        self.loadLeagues()

    def loadLeagues(self):
        try:
            r = data.api_connection.getAllCompetitions()
        except requests.exceptions.RequestException as e:
            print(e)
            return
        for json in r:
            league = League(json)
            self.leagues[league.id] = league

    def loadMatches(self):
        try:
            r = data.api_connection.getAllMatchesForToday()
        except requests.exceptions.RequestException as e:
            print(e)
            return
        for json in r['fixtures']:
            match = Match(json)
            self.matches[match.matchId] = match

    def loadFavourites(self):
        try:
            lines = [line.rstrip('\n') for line in open('./favourites.txt')]
        except Exception as e:
            return
        for id in lines:
            id = (int)(id)
            self.favourites.append(id)
            if self.matches.get(id, False):
                self.matches.get(id).markAsFavourite()
            else:
                try:
                    r = data.api_connection.getMatchById(id)
                    match1 = Match(r['fixture'])
                    match1.markAsFavourite()
                    self.matches[id] = match1
                except requests.exceptions.RequestException as e:
                    print(e)
            
    def refreshAll(self):
        try:
            r = data.api_connection.getAllMatchesForToday()
        except requests.exceptions.RequestException as e:
            print(e)
            return
        for json in r['fixtures']:
            id = (int)(json['_links']['self']['href'][-6:])
            self.matches[id].refresh(json)

    def addToFavourites(self, id):
        if id in self.favourites:
            print('The match is already in favourites.')
        elif self.matches.get(id):
            self.favourites.append(id)
            self.matches[id].markAsFavourite()
            with open('./favourites.txt', 'a') as f:
                f.write((str)(id) + '\n')
            print('Match with id : ' + \
                  (str)(id) + ' successfully added to favourites.')
        else:
            print('No such match.')

    def removeFromFavourites(self, id):
        if id not in self.favourites:
            print('The match is NOT in favourites.')
            return
        with open('./favourites.txt', 'r') as f:
            lines = f.readlines()
        with open('./favourites.txt', 'w') as f:
            for line in lines:
                if line != (str)(id) + '\n':
                    f.write(line)
        self.favourites.remove(id)
        self.matches[id].markAsNotFavourite()
        print('Match with ID : ' + (str)(id) + ' succesfully removed from ' + \
              'favourites.')

    def printAllMatches(self):
        print('All matches : \n\n')
        self.refreshAll()
        for k in self.matches:
            league = '    '
            lId = self.matches[k].competitionId
            if self.leagues.get(lId):
                league = self.leagues[lId].league + '  '
                if len(league) == 4:
                    league += ' '
            print(league + (str)(self.matches[k]))

    def printAllFavouriteMatches(self):
        print('Favourite matches : \n\n')
        self.refreshAll()
        for id in self.favourites:
            league = '    '
            lId = self.matches[id].competitionId
            if self.leagues.get(lId):
                league = self.leagues[lId].league + '  '
                if len(league) == 4:
                    league += ' '
            print((str)(league) + (str)(self.matches[id]))

    def printAllLeagues(self):
        print('Leagues : \n\n')
        for lId in self.leagues:
            print((str)(self.leagues[lId]))

    def printLeagueTable(self, lId):
        if self.leagues.get(lId):
            self.leagues[lId].printLeagueTable()
        else:
            print('No such league.')

    def printMatchDetails(self, mId):
        if not self.matches.get(mId):
            print('No such match.')
            return
        try:
            r = data.api_connection.getMatchById(mId)
            matchDet = MatchDetails(r)
            matchDet.printMatchDetails()
        except requests.exceptions.RequestException as e:
            print(e)

    def printTeamDetails(self, tId):
        try:
            r = data.api_connection.getTeamInfo(tId)
            teamDet = TeamDetails(r)
            teamDet.printTeamDetails()
        except requests.exceptions.RequestException as e:
            print(e)
'''
    def refreshTask(self):
        time.sleep(60)
        print('Going to update matches')
        self.refreshAll()

    def runTask(self):
        print('Run the task.')
        _thread.start_new_thread ( self.refreshTask, ())
'''
