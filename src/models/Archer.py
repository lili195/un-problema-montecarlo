from Gender import Gender
from GeneradorPseudoaleatorios import generate_numbers
from scipy.stats import norm

class Archer:
    def __init__(self, id):
        self.id = id
        #self.gender:Gender = self.generate_gender()
        self.resistance = self.generate_resistence()


    def generate_resistence(self):
        mean_resistance = 35
        standard_deviation_resistance = 10

        # Usar scipy.stats.norm.ppf para calcular el valor inverso de la distribución normal
        resistance = norm.ppf(generate_numbers(1)[0], mean_resistance, standard_deviation_resistance)

        # Redondear al entero más cercano
        int_resistance = round(resistance)
        return int_resistance

    def generate_gender(self):
        return Gender.FEMALE if self.generate_numbers(1)[0] >= 0.5 else Gender.MALE
    
print(Archer(1).generate_resistence(), "resistencia")