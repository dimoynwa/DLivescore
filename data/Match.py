from datetime import datetime, timedelta
import time

class Match:
    def __init__(self, json):
        self.competitionLink = json['_links']['soccerseason']['href']
        self.matchLink = json['_links']['self']['href']
        self.homeTeamName = json['homeTeamName']
        self.awayTeamName = json['awayTeamName']
        self.homeTeamGoals = json['result']['goalsHomeTeam']
        self.awayTeamGoals = json['result']['goalsAwayTeam']
        self.date = json['date']
        self.status = json['status']

    def __str__(self):
        return (str)(self.calculateMinutes()) + '   ' + self.homeTeamName + '  ' + \
               (str)(self.homeTeamGoals) + ' : ' + \
            (str)(self.awayTeamGoals) + '  ' + self.awayTeamName

    def calculateMinutes(self):
        if self.status == 'TIMED':
            return self.date[11:16]
        elif self.status == 'FINISHED':
            return 'FT'
        elif self.status == 'IN_PLAY':
            fmt = '%Y-%m-%dT%H:%M:%S'
            dt1 = datetime.strptime(self.date[:19], tf)
            dt2 = strftime(tf, gmtime())
            dt2 = datetime.strptime(dt2, tf)
            mins = ((dt2 - dt1) // timedelta(minutes=1))
            return str(mins) + '\''
        else:
            return self.status

    def refresh(self, json):
        newHomeGoals = json['result']['goalsHomeTeam']
        newAwayGoals = json['result']['goalsAwayTeam']
        self.status = json['status']
        strToReturn = ''
        if self.homeTeamGoals != newHomeGoals:
            strToReturn += self.homeTeamName + ' scores in ' + \
                (str)(self.calculateMinutes())
            self.homeTeamGoals = newHomeGoals
        if self.awayTeamGoals != newAwayGoals:
            strToReturn += self.awayTeamName + ' scores in ' + \
                (str)(self.calculateMinutes())
            self.awayTeamGoals = newAwayGoals
        return strToReturn
            
