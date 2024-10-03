import Archer

class Team:

    def __init__(self, archers, id):
        self.players = archers
        self.score = 0
        self.id = id
        
        self.won_rounds = 0
        self.count_luck = 0

    def increase_score(self, points):
        self.score += points