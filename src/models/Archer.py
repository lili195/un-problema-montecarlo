from Gender import Gender
from Shoot import *
from Bonus_record_shot import BonusRecordShot

class Archer:
    def __init__(self, id):

        self.id = id
        self.gender:Gender = self.generate_gender()
        self.experience = 10
        self.resistance = self.generate_resistence()
        self.current_resistance = self.resistance
        self.luck = self.generate_luck() 
        self.score = 0 
        self.round_score = 0
        self.extra_shoots = 0
        self.rounds_won = 0
        self.won_bonus = 0
        self.bonus_record_shot = BonusRecordShot()
    

    def generate_gender(self):
        return Gender.FEMALE if get_nums_zero_one() > 0.5 else Gender.MALE

    def generate_resistence(self):
        resistance = get_normal_number()

        # Redondear al entero más cercano
        int_resistance = round(resistance)

        return int_resistance

    def generate_luck(self):
        return get_uniform_number(3,1)[0]
    
    def simulate_shoot(self):
        self.current_resistance -= 5
        return simulate_shoot(self.gender)

    def has_extra_shoot(self):
        if self.extra_shoots == 2:
            self.extra_shoots = 0
            return True
        else:
            self.extra_shoots +=1
            return False
    
    def add_fatigue(self):
        Ri = get_uniform_number(2,1)[0]
        self.resistance = int(self.resistance - Ri)
    
    def can_continue_shooting(self):
        return True if self.current_resistance >= 5 else False
    
    def add_round_score(self, points):
        self.round_score += points
        self.score += points

    def reset_round_score(self):
        self.round_score = 0

    def won_round(self,round_number):
        self.record_victories.increase(round_number)
        self.rounds_won += 1
        self.experience += 3
        if self.rounds_won % 3 == 0: 
            self.won_bonus = 2
            print(f"El {self.id} obtuvo bonificación! (solo -1 resitencia por dos rondas) ")
            self.won_bonus = 2; 
    
    def record_bonus(self,rount):
        self.bonus_record_shot(rount)
    
    def print_info(self):
        print('---------------------------------------------------')
        print('INFORMACION DEL ARQUERO')
        print('---------------------------------------------------')
        print(f"\nID: {self.id}, \nGENERO: {self.gender}, \nRESISTENCIA: {self.resistance}, \nRESIS ACTUAL: {self.current_resistance}, \nEXPERIENCIA: {self.experience}, \nSUERTE: {self.luck}, \nPUNTAJE: {self.score}, \nRONDA PUNTAJE: {self.round_score}, \nEXTRA LANZAM: {self.extra_shoots}, \nRONDAS GANADAS: {self.rounds_won} ")
        print('---------------------------------------------------')

Archer(1).print_info()
print(Archer(1).simulate_shoot())
