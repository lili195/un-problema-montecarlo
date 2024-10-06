from Archer import *
from Team import *
from Simulation import *
from Gender import *

class Game: 

    def __init__(self, num_games):
        self.teamB = self.generate_teams("Sello")
        self.teamA = self.generate_teams("Cara")
        self.simulation = Simulation(self.teamA,self.teamB)
        self.luckiest_archers = []
        self.most_experienced_archers = []
        self.champions_teams_with_scores = []
        self.winner_gender_per_game = []
        self.archers_scores = []
        self.champions_woman_amount = 0
        self.champions_man_amount = 0
        self.game_count = 0
        self.count_men = 0
        self.count_women = 0

        for _ in range(10):
            self.archers_scores.append([])

        for i in range(0, num_games):
            self.start()
            self.check_winner()
            self.check_gender_winner()
            self.update_lucky_list()
            self.update_experience_list()
            self.check_gender_champions()
            self.check_archers_scores()
            self.reset_game()

    def generate_teams(self, id_team):
        archers = []
        for i in range(0,5):
            id = f"Arquero #{i} {id_team}"
            archers.append(Archer(id))

        return Team(id_team, archers)    

    def start(self):
        for _ in range(10):
            self.simulation.start_round()


    def check_gender_champions(self):
        if self.simulation.champion != None:
            for archer in self.simulation.champion.archers:
                if archer.gender == Gender.MALE:
                    self.count_men+=1
                else: 
                    self.count_women+=1  
    
    def update_experience_list(self): 
         archers = self.teamA.archers + self.teamB.archers
         most_experienced_archer  = max(archers, key=lambda x: x.experience)
         self.most_experienced_archers.append(most_experienced_archer.id)

    def check_archers_scores(self): 
         archers = self.teamA.archers + self.teamB.archers
         counter = 0
         for archer in archers:
            self.archers_scores[counter].append(archer.score)
            counter+=1

    def check_winner(self): 
        if self.simulation.champion != None:
            self.champions_teams_with_scores.append(f"Ganador: {self.simulation.champion.id}; Puntos: {self.simulation.champion.score}")
        else:
            self.champions_teams_with_scores.append(f"Empate con {self.simulation.teamA.score} puntos")

    def check_gender_winner(self): 
        if self.simulation.genderWon != None:
            self.winner_gender_per_game.append(f"El genero con mas victorias en el juego #{self.game_count} fue {self.simulation.genderWon.get_gender()}")
        else:
            self.winner_gender_per_game.append(f"Empate de los dos generos con {self.simulation.womenWins} victorias cada uno")
    
    def reset_game(self):
        self.game_count+=1
        print(f'Juego #{self.game_count} terminado')
        self.simulation.init_game()

    def update_lucky_list(self): 
        archers = self.teamA.archers + self.teamB.archers
        luckiest_archer = max(archers, key=lambda x: x.luck)
        self.luckiest_archers.append(luckiest_archer.id)


        