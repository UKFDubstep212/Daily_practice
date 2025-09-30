import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Semilla random
rng = np.random.default_rng(2025)

#Ejes de mi dataset
dias = pd.date_range("2025-01-01", periods=30, freq="D")
lineas = np.array(["C1","C2","C3"])
turnos = np.array(["Dia","Noche"])

#Combinaciones de los valores
D, L, T = np.meshgrid(dias, lineas, turnos, indexing="ij")

#Aplanar los datos para insertarlos en el dataframe
D_, L_, T_ = D.ravel(), L.ravel(), T.ravel()

#Hacer el dataframe
df = pd.DataFrame({
    "Dia": D_,
    "Linea": L_,   
    "Turno": T_
})

#Tasa base por dia
tasa_base_dia = {
    "C1": 380,
    "C2": 420,
    "C3": 460
}

factor_turno = {
    "Dia": 1,
    "Noche": 0.98
}

rng.normal

