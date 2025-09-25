import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

rng = np.random.default_rng(123)

# ids = np.arange(10)

# p = np.array([0.2, 0.15, 0.15, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05])

# V = rng.choice(ids, size=5, replace=True, p=p)
# print("Muestreo con pesos: ", V)

# M = rng.integers(1, 10, size=(6,4)) #Matriz de numeros aleatorios enteros
# print(M)

# print(M.sum(axis=1)) #Suma las filas de la matriz creada
# print(M.sum(axis=0)) #Suma las columans de la matriz
# print(M.max(axis=1)) #Valor maximo de cada fila
# print(M.min(axis=0)) #Valor minimo de cada columna
# print(M.argmax(axis=0)) #Indice del valor maximo por columna

ids = np.arange(10) #Crear valores para ids
pesos = np.array([0.18, 0.16, 0.14, 0.12, 0.10, 0.08, 0.07, 0.06, 0.05, 0.04]) #darle peso a cada id

#Declaramos nuestros parametros
dias, numVenDia, nProd = 30, 100, 10

#creamos una matriz de 0 donde guardar la ventas
V = np.zeros((dias, nProd), dtype=int)

#Simulamos la cantidad n de dias
for d in range(dias):
    #Le asignamos 100 productos vendidos a cada dia respecto a un peso especificado
    d_venta = rng.choice(ids, size=numVenDia, replace=True, p=pesos)
    #Contamos cuantos productos con ids iguales se vendieron en ese dia 
    #para guardarlo en la matriz de 0 que cremos anteriormente
    V[d] = np.bincount(d_venta, minlength=nProd)

print(V.shape)

#Vamos a analizar los datos
ventaProducto = V.sum(axis=0)
ventaDia = V.sum(axis=1)

print("La suma total por producto es la siguiente: ", ventaProducto)
print("La suma total por dia fue: ", ventaDia)
print("El producto mas vendido fue: ", (np.argmax(ventaProducto)+1))
print("El dia con mayor ventas fue: ", (np.argmax(ventaDia)+1))

#Mapa de calor para ver la comparativa de cantidad de productos vendidos
plt.imshow(V, cmap="hot", aspect="auto")
plt.title("Venta de 30 dias")
plt.xlabel("Producto")
plt.ylabel("Dia")
# plt.show()

#Grafico de barras para la cantidad de productos vendidos
plt.bar(np.arange(len(ventaProducto)), ventaProducto)
plt.title("Ventas por producto en 30 dias")
plt.xlabel("Producto")
plt.xticks(np.arange(nProd), np.arange(1, nProd+1))
plt.ylabel("Cantidad de productos vendidos")
# plt.show()

#Importar a un csv
df = pd.DataFrame(V, columns=[f"Producto {i}" for i in range(1, nProd+1)])
df.insert(0, "Dia", np.arange(1, dias+1))
df.insert((df.shape[1]), "Ventas totales por dia", ventaDia)

print(df.head())


