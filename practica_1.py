import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Fundamentos
# numeros = np.arange(-10,11)
# print(numeros)

# df = pd.DataFrame({
#     "Numeros": numeros,
#     "Cuadrados": numeros**2
# })
# print(df)

# plt.plot(df["Numeros"], df["Cuadrados"], marker='o')
# plt.title("Funcion Cuadratica")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.grid(True)
# plt.show()


# #Crea 100 valores entre 0 y 2pi
# x = np.linspace(0, 2*np.pi, 100)

# #Calcula el sin de cada valor
# y = np.sin(x)

# df = pd.DataFrame({
#     "x": x,
#     "y": y
# })

# #Grafica "normal"
# plt.plot(df["x"], df["y"], label="sinx")
# plt.title("Funcion sinx")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.grid(True)
# plt.show()

# #Grafico de dispersion
# plt.scatter(x,y, color="red")
# plt.title("Grafica sinx en puntos discretos")
# plt.show()

# #Dos funciones a la vez
# plt.plot(x,y,label="sinx")
# plt.plot(df["x"], np.cos(df["x"]), label="cosx")
# plt.grid(True)
# plt.show()

#Ejercicios
# x = np.linspace(-5,5)
# y = x**2
# plt.plot(x,y)
# plt.show()

# df = pd.DataFrame({
#     "x": x,
#     "y": y
# })
# plt.scatter(x,y, color="green")
# plt.show()

# df2 = pd.DataFrame({
#     "Datos": np.random.randn(100) 
# })
# desviacion_estandar = df2["Datos"].std()
# media = df2["Datos"].mean()
# print(f"Media: {media}, std: {desviacion_estandar}")

# arr = np.arange(1,11)

# print(arr[0:5]) #Los priimeros 5 numeros
# print(arr[::2]) #Los indices pares
# print(arr[-3:]) #Los ultimos tres datos

# arr = np.array(np.linspace(0, 10, 10)).astype(int)
# print(arr + 10)
# print(arr * 2)
# print(arr ** 2)

# x = np.linspace(0, 2*np.pi, 5)
# print(np.sin(x))
# print(np.cos(x))
# print(np.exp(x))

# arr = np.arange(-5,6)
# corregido = np.abs(arr[arr < 0]**3)
# print(corregido)

# matriz = np.arange(1, 10).reshape(3, 3)
# print(matriz)
# print()

# # print(np.sqrt(matriz[:,2]**2))

# print(np.sum(matriz)) #Suma los elementos de la matriz
# print(np.sum(matriz, axis=1)) #Suma por fila de la matriz
# print(np.mean(matriz, axis=0)) #promedio por columna d ela matriz
# print(np.min(matriz)) #Valor minimo de la matriz
# print(np.argmax(matriz)) #Indice del valor maximo
# print(np.argmin(matriz)) #Indice del valor minimo

# A = np.array([[2,1],
#               [1,3]])
# b = np.array([8,13])

# #Resolver el sistema Ax = b 
# x = np.linalg.solve(A, b)
# print(x)

# print(np.linalg.det(A)) #Determinante de A
# print(np.linalg.eigvals(A)) #Eigenvalores de A

# v = np.array([1, 2, 3])
# w = np.array([4, 5, 6])

# print(np.dot(v,w)) #Producto punto

# print(A.T) #Transpuesta
# print(np.linalg.norm(v)) #Norma de un vector

B = np.array([[1,0,1],[2,4,0],[3,5,6]])
b = np.array([1,2,3])
print("Determinantes: ", np.linalg.det(B))
print("Valores propios: ", np.linalg.eigvals(B))
print("Solucion al sistema Bx = b", np.linalg.solve(B,b))


