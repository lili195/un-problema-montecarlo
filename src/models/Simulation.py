class Simulation:

    def __init__(self, teamA, teamB):
        self.teamA = teamA
        self.teamB = teamB
        self.rount_number = 0
        self.winner = None


    def star_rount(self):
        self.rount_number += 1
        