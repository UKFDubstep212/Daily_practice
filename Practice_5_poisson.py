import numpy as np
import scipy.stats as sp

prom_A = 3.2
prom_B = 1.7
cantidad_de_simulaciones = 5

resultados = np.zeros((cantidad_de_simulaciones+1,cantidad_de_simulaciones+1))

def prob_A(prom_A, x):
    prob_x_goles = sp.poisson.pmf(x, prom_A)
    return prob_x_goles

def prob_B(prom_B, x):
    prob_x_goles = sp.poisson.pmf(x, prom_B)
    return prob_x_goles

for i in range(cantidad_de_simulaciones+1):
    for j in range(cantidad_de_simulaciones+1):
        resultados[i][j] = prob_A(prom_A, i) * prob_B(prom_B, j)

print(resultados)
max_prob = np.unravel_index(np.argmax(resultados), resultados.shape)
print(f"El resultado mas probable es que el equipo A meta {max_prob[0]} goles y el equipoo B {max_prob[1]} goles")
print(f"Con una probabilidad de {np.max(resultados)*100}%")


        
