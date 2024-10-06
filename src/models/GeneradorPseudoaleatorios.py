import csv
import random
import numpy as np

#Listas de numeros
lcg_randomNums = []
normal_dist_nums = []
uniform_dist_nums= []
    
# Leer el archivo CSV y extraer los números
def read_csv(csvFile):
    with open(csvFile, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Saltar la primera línea (encabezado "numeros")
        numbers = [float(num) for row in reader for num in row]  # Leer todos los números
    return numbers

# Leer los números desde el archivo CSV
lcg_randomNums = read_csv("pseudo_random_sequence.csv")

# Función para obtener numeros generados con el metodo de LCG
def get_nums_zero_one():
    if not lcg_randomNums:
        lcg_randomNums.extend(read_csv("pseudo_random_sequence.csv"))

    # Mezclar los números aleatoriamente
    random.shuffle(lcg_randomNums)
    return lcg_randomNums.pop(0)
 

normal_dist_nums = read_csv("distNorm.csv")


def get_normal_number():
    if not normal_dist_nums:
        normal_dist_nums.extend(read_csv("distNorm.csv"))

    random.shuffle(normal_dist_nums)
    return normal_dist_nums.pop(0)

def get_uniform_number(sup, inf):
    return np.random.uniform(inf, sup, 1)















