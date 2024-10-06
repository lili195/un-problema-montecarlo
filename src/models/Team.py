class Team:

    def __init__(self, id, archers):
        self.id = id
        self.archers = archers
        self.score = 0

    def update_score(self, points):
        self.score += points