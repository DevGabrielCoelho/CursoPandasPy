"""operações com strings"""

import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

dataset = pd.read_csv("census.csv")

index_paises = []

for i in range(32561):
    index_paises.append(fake.country())

serie_pais_idade = pd.Series(np.array(dataset["age"]), index=index_paises)

serie_pais_index = serie_pais_idade.index.to_series()

serie_pais_index.reset_index(drop=True, inplace=True)

print(serie_pais_index)
print(serie_pais_index.str.contains("tse"))
print(serie_pais_index.str.upper())
print(serie_pais_index.str.lower())
print(serie_pais_index.str.strip("Libyan")) #remove a string desejada
print(serie_pais_index.str.split(" ", expand=True))
print(serie_pais_index.str[0:5]) #trunca as strings para o valor
