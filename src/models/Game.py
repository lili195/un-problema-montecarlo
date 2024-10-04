import Archer
import Team
import Simulation

class Game: 

    def __init__(self, games_amount):
        teamA = self.generate_teams("Cara")
        teamB = self.generate_teams("Sello")
        self.simulation = Simulation(teamA,teamB)
        self.player_max__luchy = []
        self.player_max_experience = []
        self.champions_teams_with_scores = []
        self.champions_woman_amount = 0
        self.champions_man_amount = 0
        self.game_count = 0


    def generate_teams(self, id_team):
        players = []
        for i in range(0,5):
            id = f"player{i} {id_team}"
            players.append(Archer(id))

        return Team(players, id_team)    

    def start(self):
        for i in range(10):
            self.simulation.start_rount()
