"""operações matemáticas"""

import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

dataset = pd.read_csv("census.csv")

indices_paises = []

for i in range(32561):
    indices_paises.append(fake.country())

serie_pais_idade = pd.Series(np.array(dataset["age"]), index=indices_paises)

print(serie_pais_idade)
print(serie_pais_idade + 2)
print(serie_pais_idade.add(2))
print(serie_pais_idade.sub(2))
print(serie_pais_idade.mul(2))
print(serie_pais_idade.div(2))

s1 = pd.Series([20, 30, 40])
s2 = pd.Series([1, 2, 3])

print(s1.add(s2))
print(s1.sub(s2))
print(s1.mul(s2))
print(s1.div(s2))
