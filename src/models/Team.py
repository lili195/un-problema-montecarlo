class Team:

    def __init__(self, players, id):
        self.id = id
        self.players = players
        self.score = 0

    def update_score(self, points):
        self.score += points