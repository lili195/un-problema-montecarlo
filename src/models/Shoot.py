import csv
import random

# Leer el archivo CSV y extraer los números
def leer_numeros_csv(archivo_csv):
    with open(archivo_csv, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Saltar la primera línea (encabezado "numeros")
        numeros = [float(num) for row in reader for num in row]  # Leer todos los números
    return numeros

# Leer los números desde el archivo CSV
random_numbers = leer_numeros_csv("pseudo_random_sequence.csv")

# Mezclar los números aleatoriamente
random.shuffle(random_numbers)

# Función para obtener el próximo número sin reemplazo
def obtener_numero_lanzamiento(random_number):
    if random_number:
        return random_number.pop(0)
    else:
        print("Se acabaron los números en la lista.")
        return None

# Definir los intervalos para hombres y mujeres
def check_shoot_male(self, random_number):
    if random_number < 0.20:
        return 10               
    elif random_number < 0.53:  
        return 9                
    elif random_number < 0.93:  
        return 8                
    else:
        return 0                

def check_shoot_female(self, random_number):
    if random_number < 0.30:
        return 10          
    elif random_number < 0.68:  
        return 9           
    elif random_number < 0.95:  
        return 8          
    else:
        return 0         
   

# Simulación de un lanzamiento para un jugador
def simular_lanzamiento(genero):
    numero_lanzamiento = obtener_numero_lanzamiento(random_numbers)
    if numero_lanzamiento is not None:
        resultado = check_shoot_female(numero_lanzamiento, genero)
        print(f"El número {numero_lanzamiento} dio como resultado: {resultado}")
    else:
        print("No se pudo realizar el lanzamiento.")

# Ejemplo: Simular un lanzamiento para un hombre y una mujer
simular_lanzamiento("hombre")
simular_lanzamiento("mujer")
