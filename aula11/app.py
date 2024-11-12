"""agrupamento numerico"""

import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

dataset = pd.read_csv("census.csv")

paises = []

for i in range(32561):
    paises.append(fake.country())

series_paises_idade = pd.Series(np.array(dataset["age"]), index=paises)

# series_paises_idade = series_paises_idade.index.to_series()
# series_paises_idade.reset_index(drop=True, inplace=True)

# print(series_paises_idade)

print(series_paises_idade.sum())
print(series_paises_idade.mean())
print(series_paises_idade.median())
print(series_paises_idade.count())
print(series_paises_idade.std()) #desvio padrão
print(series_paises_idade.var()) #variancia
print(series_paises_idade.loc["Brazil"].mean())
print(series_paises_idade.loc["India"].mean())
print(series_paises_idade.quantile([0.25, 0.5, 0.75])) #presentes em uma porcentagem da base de dados
