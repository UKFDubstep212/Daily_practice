import numpy as np
import matplotlib.pyplot as plt

#Semilla
rng = np.random.default_rng(0)

#Parametros
N, steps = 200, 50

#Se genera un conjunto de 200 particulas con coordendas (x,y) aleatorias
pos = rng.standard_normal((N,2))
#Se genera una matriz de ceros
hist = np.zeros((steps, N, 2))

#Se simula el moviemiento de las particulas con ruido gaussiano
for i in range(steps):
    pos += 0.1 * rng.standard_normal((N,2))
    hist[i] = pos

plt.plot(hist[:,0,0], hist[:,0,1])
plt.show()

