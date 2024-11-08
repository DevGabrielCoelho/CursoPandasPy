"""usando bibli Faker e manipulando indices"""

import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

indices_nome = []

for i in range(32561):
    indices_nome.append(fake.name())

dataset = pd.read_csv("census.csv")

serie_idade_nome = pd.Series(np.array(dataset['age']), index=indices_nome)

print(serie_idade_nome.head(5))
# print(serie_idade_nome["Clinton Choi"])

serie_idade_nome_sem_duplicatas = serie_idade_nome.drop_duplicates()

print(serie_idade_nome_sem_duplicatas.index)

# print(serie_idade_nome_sem_duplicatas["Clinton Choi" : "Joseph Wright"])

serie_idade_nome3 = serie_idade_nome_sem_duplicatas.copy()

serie_idade_nome3 = serie_idade_nome3.reset_index(drop=True)

print(serie_idade_nome3.head())
print(serie_idade_nome3.index)
