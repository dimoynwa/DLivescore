import unittest
from team import Team

class TestTeam(unittest.TestCase):
    def setUp(self):
        json = {"_links":{"team":
                {"href":"http://api.football-data.org/v1/teams/60"}},
                "position":1,"teamName":"Bolton Wanderers FC",
                "playedGames":4,"points":12,"goals":7,"goalsAgainst":3,
                "goalDifference":4,"wins":4,"draws":0,"losses":0,
                "home":{"goals":3,"goalsAgainst":1,"wins":2,"draws":0,
                "losses":0},"away":{"goals":4,"goalsAgainst":2,"wins":2,
                "draws":0,"losses":0}}
        self.team = Team(json)

    def test_team_create(self):
        self.assertEqual(self.team.position, 1)
        self.assertEqual(self.team.name, 'Bolton Wanderers FC')
        self.assertEqual(self.team.points, 12)


if __name__ == '__main__':
    unittest.main()
