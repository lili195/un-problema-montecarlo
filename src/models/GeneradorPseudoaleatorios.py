
# # Un problema Montecarlo

# ## Implementar Linear Congruential Generator (LCG)

# # Para generar una secuencia de 2000 números pseudoaleatorios se utiliza la fórmula:

# ##  x_{i+1} = (a_{i} + c) mod (m)

# # Siendo:

# # - Xi --> El numero generado en la iteración actual
# # - a, c, y m son parámetros específicos del LCG:

# #     a es el multiplicador.
# #     c es el incremento.
# #     m es el módulo (tamaño del rango).

# import csv

# # Parámetros del LCG 
# a = 1664525        # multiplicador
# c = 1013904223     # incremento
# m = 2**32          # módulo
# X0 = 42            # semilla inicial

# # Función LCG para generar números pseudoaleatorios
# def lcg(seed, a, c, m, n):
#     numbers = []
#     Xn = seed
#     for _ in range(n):
#         Xn = (a * Xn + c) % m
#         numbers.append(Xn / m)  # Normalizar los números entre 0 y 1
#     return numbers

# # Generar 2000 números pseudoaleatorios
# random_numbers = lcg(X0, a, c, m, 2000)

# # Guardar la secuencia en un archivo CSV con encabezado "numeros"
# with open("pseudo_random_sequence.csv", "w", newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["numeros"])  # Escribir el encabezado
#     for number in random_numbers:
#         writer.writerow([f"{number:.10f}"])  # Escribir los números con formato de 10 decimales








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

    
















