"""acesso aos dados com iloc"""

import pandas as pd
import numpy as np

dataset = pd.read_csv("census.csv")
print(dataset)

serie_idade = dataset['age']

print(serie_idade)

serie_idade = dataset['age'].values

print(serie_idade)

serie_idade = dataset['age']

print(serie_idade.head())
print(serie_idade.head(10))
print(serie_idade.tail())
print(serie_idade.tail(10))

print(serie_idade.iloc[10])
print(serie_idade.iloc[32559])
print(serie_idade.iloc[-1])
print(serie_idade.iloc[0:3])
print(serie_idade.iloc[[0, 2, 4]])

lista_idade = []

for i in serie_idade.items():
    # print(i)
    print(i[0], i[1])
    if i[1] > 50:
        lista_idade.append(i[1])

print(len(lista_idade))

print(serie_idade.iloc[lista_idade])
