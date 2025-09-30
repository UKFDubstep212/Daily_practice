import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(10)

M = rng.normal(50, 10, (6,4))

stand = M.std(axis=0)
media = M.mean(axis=0)

for i in range(6):
    for j in range(4):
        M[i][j] = 5*(M[i][j] - media[j])/stand[j]

print(M.std())

