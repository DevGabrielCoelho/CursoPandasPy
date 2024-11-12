"""agrupamento categorico"""

import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

dataset = pd.read_csv("census.csv")

paises = []

for i in range(32561):
    paises.append(fake.country())

series_paises_idade = pd.Series(np.array(dataset["age"]), index=paises)

series_paises_idade = series_paises_idade.index.to_series()
series_paises_idade.reset_index(drop=True, inplace=True)

print(series_paises_idade.value_counts(normalize=True))
print(series_paises_idade.value_counts())
print(series_paises_idade.index.unique())
print(series_paises_idade.nunique())

