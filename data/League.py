from Team import Team
import api_connection

class League:
    def __init__(self, json):
        self.id = json['id']
        self.tableUrl = json['_links']['leagueTable']['href']
        self.caption = json['caption']
        self.league = json['league']
        self.numberOfTeams = json['numberOfTeams']

    def printLeagueTable(self):
        try:
            r = api_connection.getRequest(self.tableUrl)
        except requests.exceptions.RequestException as e:
            print(e)
            return
        print(self.caption + '\n\n')
        for team in r['standing']:
            t = Team(team)
            print(t)

            
        
