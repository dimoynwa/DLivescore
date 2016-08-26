class Team:
    def __init__(self, json):
        ind = json['_links']['team']['href'].rfind('/') + 1
        self.teamId = json['_links']['team']['href'][ind:]
        self.position = json['position']
        self.name = json['teamName']
        self.playedGames = json['playedGames']
        self.wins = json['wins']
        self.draws = json['draws']
        self.losses = json['losses']
        self.points = json['points']

    def __str__(self):
        return (str)(self.position) + '.  ' + \
                'ID : ' + self.teamId + '   ' + self.name + \
               '  GP: ' + (str)(self.playedGames) + '   W: ' + \
               (str)(self.wins) + '   D: ' + (str)(self.draws) + \
               '   L: ' + (str)(self.losses) + '   PTS: ' + \
               (str)(self.points)
