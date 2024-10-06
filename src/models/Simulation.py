from Gender import *
from GeneradorPseudoaleatorios import *

class Simulation:

    def __init__(self, teamA, teamB):
        self.teamA = teamA
        self.teamB = teamB
        self.round_counter = 0
        self.champion = None

    def start_round(self):
        self.round_counter += 1
        print(f"RONDA {self.round_counter}")
        self.simulate_shots(self.teamB)
        self.simulate_shots(self.teamA)
        archers = self.teamB.archers + self.teamA.archers
        champion_archer = self.get_champion_archer(archers)
        print(f'La Ronda {self.round_counter} fue ganada por {champion_archer.id}')
        champion_archer.won_round(self.round_counter)
        self.get_champion_team()

    def get_champion_archer(self, archers):
        max_score_archer = max(archers, key=lambda x: x.round_score)
        max_score_archers = [archer for archer in archers if archer.round_score == max_score_archer.round_score]

        if len(max_score_archers) > 1: 
            print(f'Empate, tienen que lanzar')
            archers = self.solve_tie_archers(max_score_archers)
            max_score_archer= self.get_champion_archer(archers)

        return max_score_archer

    def get_champion_team(self):
        if self.round_counter == 10:
            if self.teamA.score > self.teamB.score:
                print("Gana equipo cara")
                self.champion = self.teamA
            elif self.teamA.score < self.teamB.score:
                print("Gana equipo Sello")
                self.champion = self.teamB
            else:
                print("EMPATE")
                self.champion = None 
            archers = self.teamA.archers + self.teamB.archers 
            
            most_won_archer = max(archers, key=lambda x: x.rounds_won)
            print(f'El arquero con mas rondas ganadas es {most_won_archer.id}')
        else:
            self.init_archers()    

    def init_archers(self):
        for archer in self.teamA.archers + self.teamB.archers:
            archer.luck = get_uniform_number(3,1)
            archer.round_score = 0
            archer.add_fatigue()
            archer.current_resistance = archer.resistance
    
    def init_game(self):
        print("Juego reiniciado")
        for archer in self.teamA.archers + self.teamB.archers:
            archer.gender = Gender.MALE if get_nums_zero_one() > 0.5 else Gender.FEMALE
            archer.resistance = get_normal_number()
            archer.actual_resistance = archer.resistance
            archer.experience = 10
            archer.luck = get_uniform_number(3,1)
            archer.score = 0
            archer.round_score = 0
            archer.extra_throws = 0
            archer.rounds_won = 0
            archer.won_bonus = 0
        self.teamA.score = 1
        self.teamB.score = 2
        self.round_counter = 0
        self.champion = None
        
    def additional_shoot(self,team):
        luckiest_archer = max(team.archers, key=lambda x: x.luck)
        if luckiest_archer.has_extra_shoot():
            score = luckiest_archer.simulate_shoot()
            team.update_score(score)
        score = luckiest_archer.simulate_shoot()
        team.update_score(score)              

    def simulate_shots(self, team):
        for archer in team.archers:
            while archer.can_continue_shooting():
                score = archer.simulate_shoot()
                archer.add_round_score(score)
                team.update_score(score)
        
        self.additional_shoot(team)

    def solve_tie_archers(self,archers):
        for archer in archers:
            archer.round_score = 0
            archer.round_score = archer.simulate_shoot()
            print(f'{archer.id} lanza, su puntaje es:  {archer.round_score}')
        return archers

              