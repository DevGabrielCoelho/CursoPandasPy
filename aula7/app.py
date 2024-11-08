"""contagem de valores"""

import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

index_nomes = []

for i in range(32561):
    index_nomes.append(fake.name())

dataset = pd.read_csv("census.csv")

serie_idade_nome = pd.Series(np.array(dataset["age"]), index=index_nomes)

print(serie_idade_nome.size)

print(serie_idade_nome.value_counts())

print(serie_idade_nome.value_counts(normalize=True))
print(serie_idade_nome.value_counts(normalize=True, sort=True))

print(serie_idade_nome.value_counts(bins=10))
