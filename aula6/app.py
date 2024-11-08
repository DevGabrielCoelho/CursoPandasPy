"""usando sort"""

import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

indices_nome = []

for i in range(32561):
    indices_nome.append(fake.name())

dataset = pd.read_csv("census.csv")

serie_idade_nome = pd.Series(np.array(dataset['age']), index=indices_nome)

print(serie_idade_nome.sort_values())
print(serie_idade_nome.sort_values(ascending=False))

print(serie_idade_nome.sort_index())
print(serie_idade_nome.sort_index(ascending=False))

serie_recortada = serie_idade_nome.sort_index().iloc[0:11]

print(serie_recortada)
