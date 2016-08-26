from datetime import date

class Player:
    def __init__(self, json):
        self.number = json['jerseyNumber']
        self.name = json['name']
        self.position = json['position']
        self.birthDate = json['dateOfBirth']
        self.value = json['marketValue']

    def __str__(self):
        return (str)(self.number) + '. ' + self.name + '   ' + \
               self.position + '\n        Age : ' + (str)(self.getAge()) +\
               '   Market value : ' + (str)(self.value)

    def getAge(self):
        year = (int)(self.birthDate[:4])
        return date.today().year - year
