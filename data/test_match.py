import unittest
from data import Match

class TestMatch(unittest.TestCase):
    def setUp(self):
        json = {  
                   "_links":{  
                      "self":{  
                         "href":"http://api.football-data.org/v1/fixtures/153572"
                      },
                      "competition":{  
                         "href":"http://api.football-data.org/v1/competitions/433"
                      },
                      "homeTeam":{  
                         "href":"http://api.football-data.org/v1/teams/679"
                      },
                      "awayTeam":{  
                         "href":"http://api.football-data.org/v1/teams/676"
                      }
                   },
                   "date":"2016-08-26T18:00:00Z",
                   "status":"TIMED",
                   "matchday":4,
                   "homeTeamName":"Vitesse Arnhem",
                   "awayTeamName":"FC Utrecht",
                   "result":{  
                      "goalsHomeTeam":0,
                      "goalsAwayTeam":0
                   },
                   "odds":{}
                }
        self.match = Match(json)

    def test_match_create(self):
        self.assertEqual(self.match.homeTeamName, 'Vitesse Arnhem')
        self.assertEqual(self.match.awayTeamName, 'FC Utrecht')

    def test_calculate_minutes(self):
        mins = self.match.calculateMinutes()
        assertEquals(mins, '18:00')


if __name__ == '__main__':
    unittest.main()
