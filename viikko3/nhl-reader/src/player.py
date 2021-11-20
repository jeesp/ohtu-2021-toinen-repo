class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.points = self.goals + self.assists
    
    def __str__(self):
        return self.name + self.team + str(self.goals) + "+" + str(self.assists) + "=" + str(self.goals + self.assists)
