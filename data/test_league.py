import unittest
from league import League

class TestLeague(unittest.TestCase):
    def setUp(self):
        json = {"_links":
            {"self":
            {"href":"http://api.football-data.org/v1/soccerseasons/427"},
            "teams":
            {"href":"http://api.football-data.org/v1/soccerseasons/427/teams"},
            "fixtures":
            {"href":"http://api.football-data.org/v1/soccerseasons/427/fixtures"},
            "leagueTable":
            {"href":"http://api.football-data.org/v1/soccerseasons/427/leagueTable"}},
            "id":427,"caption":"Championship 2016/17","league":"ELC",
            "year":"2016","currentMatchday":5,"numberOfMatchdays":46,
            "numberOfTeams":24,"numberOfGames":552,
            "lastUpdated":"2016-08-25T00:00:45Z"}
        self.league = League(json)

    def test_league_create(self):
        self.assertEqual(self.league.id, 427)
        self.assertEqual(self.league.caption, 'Championship 2016/17')
        self.assertEqual(self.league.league, 'ELC')
        self.assertEqual(self.league.numberOfTeams, 24)

       
if __name__ == '__main__':
    unittest.main()
