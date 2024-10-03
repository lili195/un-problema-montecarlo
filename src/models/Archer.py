from Gender import Gender
from GeneradorPseudoaleatorios import generate_numbers

class Archer:
    def __init__(self, id):
        self.id = id
        self.gender:Gender = self.generate_gender()
        self.resistance = self.generate_resistence()


    def generate_resistence(self):
        #genera un valor entre 25 y 45
        #21 representa la diferencia entre 45 y 25, más uno para incluir ambos límites (25 y 45).
        return (self.generate_numbers(1)[0] * 21) +25

    def generate_gender(self):
        return Gender.FEMALE if self.generate_numbers(1)[0] >= 0.5 else Gender.MALE