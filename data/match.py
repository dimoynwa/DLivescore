from datetime import datetime, timedelta
import time

class Match:
    def __init__(self, json):
        i = (int)(json['_links']['competition']['href'].rfind('/') + 1)
        self.competitionId = (int)(json['_links']['competition']['href'][i:])
        ind = (int)(json['_links']['self']['href'].rfind('/') + 1)
        self.matchId = (int)(json['_links']['self']['href'][ind:])
        self.homeTeamName = json['homeTeamName']
        self.awayTeamName = json['awayTeamName']
        self.homeTeamGoals = json['result']['goalsHomeTeam']
        self.awayTeamGoals = json['result']['goalsAwayTeam']
        self.date = json['date']
        self.status = json['status']
        self.favourite = False
        self.odds = {}
        if(json.get('odds', False)):
            self.odds = json['odds']
        self.updatedStatus = ''

    def __str__(self):
        fav = ''
        if self.favourite:
            fav = 'Fav.'
        homeGoals = self.homeTeamGoals
        awayGoals = self.awayTeamGoals
        if self.homeTeamGoals is None:
            homeGoals = '-'
        if self.awayTeamGoals is None:
            awayGoals = '-'
        return self.updatedStatus + 'Id : ' + (str)(self.matchId) + '   ' + \
               (str)(self.calculateMinutes()) + '   ' + self.homeTeamName + \
                '  ' + \
               (str)(homeGoals) + ' : ' + \
            (str)(awayGoals) + '  ' + self.awayTeamName + '   ' + fav

    def calculateMinutes(self):
        if self.status == 'TIMED' or self.status == 'SCHEDULED':
            return self.date[11:16]
        elif self.status == 'FINISHED':
            return 'FT'
        elif self.status == 'IN_PLAY':
            '''
            tf = '%Y-%m-%dT%H:%M:%S'
            dt1 = datetime.strptime(self.date[:19], tf)
            dt2 = datetime.strftime(tf, time.gmtime())
            dt2 = datetime.strptime(dt2, tf)
            mins = ((dt2 - dt1) // timedelta(minutes=1))
            '''
            now = time.strftime("%H:%M:%S")
            nowH = (int)(now[0:2]) - 3
            nowM = (int)(now[3:5])
            matchH = (int)(self.date[11:13])
            metchM = (int)(self.date[14:16])
            mins = 0
            if nowH == matchH:
                mins = nowM - matchM
            elif nowH == matchM + 1:
                mins = 60 - matchM + nowM
            elif nowH == matchM + 2:
                mins = 60 - matchM + nowM + 60
            if mins > 45 and mins <= 60:
                mins = 'HT'
            elif mins > 60:
                mins = mins - 15
            return (str)(mins) + '\''
        else:
            return self.status

    def refresh(self, json):
        if self.status == 'FINISHED':
            return
        newHomeGoals = json['result']['goalsHomeTeam']
        newAwayGoals = json['result']['goalsAwayTeam']
        self.status = json['status']
        self.updatedStatus = ''
        if self.homeTeamGoals != newHomeGoals:
            self.updatedStatus += self.homeTeamName + ' scores in ' + \
                (str)(self.calculateMinutes()) + '\n'
            self.homeTeamGoals = newHomeGoals
        if self.awayTeamGoals != newAwayGoals:
            self.updatedStatus += self.awayTeamName + ' scores in ' + \
                (str)(self.calculateMinutes()) + '\n'
            self.awayTeamGoals = newAwayGoals

    def printMatchOdds(self):
        if self.odds:
            print('Odds : ' + self.homeTeamName + ' : ' +\
                  (str)(self.odds['homeWin']) +\
                  '   Draw : ' + (str)(self.odds['draw']) +\
                  '   ' + self.awayTeamName + ' : ' +\
                  (str)(self.odds['awayWin']))

    def markAsFavourite(self):
        self.favourite = True

    def markAsNotFavourite(self):
        self.favourite = False
