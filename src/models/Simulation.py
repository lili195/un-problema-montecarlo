class Simulation:

    def __init__(self, teamA, teamB):
        self.teamA = teamA
        self.teamB = teamB
        self.rount_count = 0
        self.champion = None


    def star_rount(self):
        self.rount_number += 1

    def getChampionTeam(self):
        if self.rount_count == 10:
            if self.teamA.score < self.teamB.score:
                self.champion = self.teamB
            elif self.teamA.score > self.teamB.score:
                self.champion = self.teamA
            else:
                self.champion = None 
            players = self.teamA.players + self.teamB.players 
            max(players, key=lambda x: x.rounds_won)         
