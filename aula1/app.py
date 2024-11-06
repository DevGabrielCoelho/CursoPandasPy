"""importando o pandas em pd"""

import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

serie_dados = pd.Series([10, 20, 30, 40, 50])

print(serie_dados)

indices = ['A', 'B', 'C', 'D', 'E']

serie_dados = pd.Series([10, 20, 30, 40, 50], index=indices)

print(serie_dados)
print(serie_dados.shape)

serie_dados = pd.Series([10, 20, 30, 40, 50])

print(serie_dados)

serie_dados.index = ['A', 'B', 'C', 'D', 'E']

print(serie_dados)

valores = np.random.random(10)

indices = np.arange(0, 10)

serie_dados = pd.Series(valores, indices)

print(serie_dados)

dicionario = {
    'A': 10,
    'B': 20,
    'C': 30,
    'D': 40,
    'E': 50
}

type(dicionario)

serie_dados = pd.Series(dicionario)

print(serie_dados)
