import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Semilla para valores random
rng = np.random.default_rng(120)

#Generar los valores de temperatura para los 30 dias
mes_simulado = rng.normal(loc=25, scale=5, size=30)

#Acortar los valores
mes_simulado = np.clip(mes_simulado, min=10, max=40)

#Poner los datos en pandas
df_clima = pd.DataFrame({
    "Dia": (np.arange(30)+1),
    "Temperatura": mes_simulado
})

#Grafica la temperatura por dia
plt.plot((np.arange(30)+1), mes_simulado)
plt.title("Temperatur por dia")
plt.xlabel("Dias")
plt.ylabel("Temperatura")
plt.grid()
plt.show()

#Histograma
plt.hist(mes_simulado, bins=10)
plt.show()