import csv
import random
import math
import datetime

# Parámetros del LCG 
a = 1664525                                         # multiplicador
c = 3                                               # incremento
m = 2**32                                           # módulo
X0 = datetime.datetime.now().microsecond            # semilla inicial

def generate_numbers(n):
    multiplier = is_valid_module(a,m)
    return lcg(X0, multiplier, c, m, n)


def is_valid_module(a, m):
    # Verificar que a y m sean primos relativos (gcd debe ser 1)
    if math.gcd(a, m) != 1:
        return is_valid_module(a+1,m)
    # Verificar que a no sea múltiplo de 2
    if a % 2 == 0:
        return is_valid_module(a+1,m)
    #"Los parámetros son válidos."
    return a

# Función LCG para generar números pseudoaleatorios
def lcg(seed, a, c, m, n):
    numbers = []
    Xn = seed
    for _ in range(n):
        Xn = (a * Xn + c) % m
        numbers.append(Xn / m)  # Normalizar los números entre 0 y 1
    return numbers

    
# Leer el archivo CSV y extraer los números
def read_csv(csvFile):
    with open(csvFile, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Saltar la primera línea (encabezado "numeros")
        numbers = [float(num) for row in reader for num in row]  # Leer todos los números
    return numbers
lcg_randomNums = []
# Leer los números desde el archivo CSV
lcg_randomNums = read_csv("pseudo_random_sequence.csv")

# Mezclar los números aleatoriamente
random.shuffle(lcg_randomNums)

# Función para obtener el próximo número sin reemplazo
def get_nums_zero_one():
    return lcg_randomNums.pop(0)
 

normal_dist_nums =[]
normal_dist_nums = read_csv("distNorm.csv")
random.shuffle(normal_dist_nums)


def get_normal_numbers():
    return normal_dist_nums.pop(0)















