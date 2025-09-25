import numpy as np
# rng = np.random.default_rng(0)

# n = 400
# A = rng.standard_normal((n,n))
# B = rng.standard_normal((n,n))

rng = np.random.default_rng(42)
A = rng.integers(low=0, high=10, size=(3,3)) #Matriz 3x3 de numeros enteros
print(A)

B = rng.random((3,3))#Matiz aleatoria 3x3 de numeros entre 0 y 1
print(B)

C = rng.uniform(-3,3,(3,3)) #Matriz aleatoria 3x3 entre -3 y 3
print(C)

Z = rng.standard_normal((4,4)) #Distribucion Gaussiana
X = 100 + 15*Z
print(X)

M = rng.binomial(n=1, p=0.3, size=(3,3)) #Distribucion binomial o Bernoulli con probabilidad de 1 de 0.3
print(M)
print()

valores = np.array([10,20,30,40,50])
S = rng.choice(valores, size=(3,3), replace=True)
print(S)
print()
P = rng.permutation(9).reshape(3,3) #Permuta
print(P)

