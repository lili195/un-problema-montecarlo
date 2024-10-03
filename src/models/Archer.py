from Gender import Gender
from GeneradorPseudoaleatorios import generate_numbers
from scipy.stats import norm

class Archer:
    def __init__(self, id):
        self.id = id
        self.gender:Gender = self.generate_gender()
        self.experience = 10
        self.resistance = self.generate_resistence()
        self.luck = self.generate_luck()
        # self.precision = precision    # Precisión del arquero
        # self.error = error            # Error en los lanzamientos
        self.score = 0                # Puntaje acumulado en el juego
        self.rounds_won = 0           # Rondas ganadas

    def generate_gender(self):
        return Gender.FEMALE if generate_numbers(1)[0] >= 0.5 else Gender.MALE

    def generate_resistence(self):
        mean_resistance = 35
        standard_deviation_resistance = 10

        # Usar scipy.stats.norm.ppf para calcular el valor inverso de la distribución normal
        resistance = norm.ppf(generate_numbers(1)[0], mean_resistance, standard_deviation_resistance)

        # Redondear al entero más cercano
        int_resistance = round(resistance)
        return int_resistance

    def generate_luck(self):
        Ri = generate_numbers(1)
        a= 1
        b=3
        Ni= a + ((b-a)*Ri[0])
        return Ni


















