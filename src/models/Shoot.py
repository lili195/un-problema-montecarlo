from Gender import Gender
from GeneradorPseudoaleatorios import *

# Definir los intervalos para hombres y mujeres
def check_shoot_male(random_number):
    if random_number < 0.20:
        return 10               
    elif random_number < 0.53:  
        return 9                
    elif random_number < 0.93:  
        return 8                
    else:
        return 0                

def check_shoot_female(random_number):
    if random_number < 0.30:
        return 10          
    elif random_number < 0.68:  
        return 9           
    elif random_number < 0.95:  
        return 8          
    else:
        return 0         
   

# Simulación de un lanzamiento para un jugador
def simulate_shoot(gender):
    number_shoot = get_nums_zero_one()
    if gender == Gender.MALE:
        result = check_shoot_male(number_shoot)
    else:
        result = check_shoot_female(number_shoot)
    return result
