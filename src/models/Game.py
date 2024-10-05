import Archer
import Team
import Simulation

class Game: 

    def __init__(self, games_amount):
        teamA = self.generate_teams("Cara")
        teamB = self.generate_teams("Sello")
        self.simulation = Simulation(teamA,teamB)
        self.max__luchy = []
        self.champions_teams_with_scores = []
        self.players_scores = []
        self.max_experience = []
        self.champions_woman_amount = 0
        self.champions_man_amount = 0
        self.game_count = 0
        self.count_men = 0
        self.count_women = 0


    def generate_teams(self, id_team):
        players = []
        for i in range(0,5):
            id = f"player{i} {id_team}"
            players.append(Archer(id))

        return Team(players, id_team)    

    def start(self):
        for i in range(10):
            self.simulation.start_rount()

    

    def check_gender_champion(self):
        if self.simulation.champion != None:
            for player in self.simulation.champion.players:
                if player.gender == "Male":
                    self.count_men+=1
                else: 
                    self.count_women+=1  
    
    def update_experience_list(self): 
         players = self.teamA.players + self.teamB.players
         max_experience_player  = max(players, key=lambda x: x.experience)
         self.max_experience.append(max_experience_player.name)

    def check_players_scores(self): 
         players = self.teamA.players + self.teamB.players
         count = 0
         for player in players:
            self.players_scores[count].append(player.score)
            count+=1

    def check_winner(self): 
        if self.simulation.champion != None:
            self.champions_teams_with_scores.append(self.simulation.champion)
        else:
             self.champions_teams_with_scores.append("Empate")
    
    def reset_game(self):
        self.game_count+=1
        teamA = self.generate_teams("Cara")
        teamB = self.generate_teams("Sello")
        self.simulation = Simulation(teamA,teamB) 

    def update_lucky_list(self): 
        players = self.teamA.players + self.teamB.players
        max_lucky_player  = max(players, key=lambda x: x.luck)
        self.max_lucky.append(max_lucky_player.name)


