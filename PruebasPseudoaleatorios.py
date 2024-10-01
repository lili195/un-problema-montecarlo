import numpy as np
from scipy import stats

# PUEBA DE MEDIA

# Cargar los números desde el archivo
numbers = np.loadtxt('pseudo_random_sequence.txt')

# PRUEBA DE MEDIA
media_observada = np.mean(numbers)
media_esperada = 0.5

print(f"Media observada: {media_observada}")

# PRUEBA DE VARIANZA

varianza_observada = np.var(numbers)
varianza_esperada = 1/12

print(f"Varianza observada: {varianza_observada}")

# PRUEBA KS

ks_stat, p_value_ks = stats.kstest(numbers, 'uniform')

print(f"Estadístico KS: {ks_stat}, Valor p: {p_value_ks}")

# PRUEBA chi²

# Crear intervalos (bins)
num_bins = 10
hist, bin_edges = np.histogram(numbers, bins=num_bins)

# Frecuencia esperada en cada intervalo
frecuencia_esperada = len(numbers) / num_bins

#Prueba

chi2_stat, p_value_chi2 = stats.chisquare(hist, [frecuencia_esperada] * num_bins)

print(f"Estadístico chi²: {chi2_stat}, Valor p: {p_value_chi2}")
