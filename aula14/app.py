"""funções"""

import pandas as pd
import numpy as np

dataset = pd.read_csv("census.csv")

serie_idade = pd.Series(np.array(dataset["age"]))

print(serie_idade)

print(serie_idade.loc[serie_idade < 18])


def corrige_idade(idade):
    """função para corrigir idades menores de 18"""
    if idade < 18:
        idade = 18
    return idade


serie_idade = serie_idade.apply(corrige_idade)
print(serie_idade.loc[serie_idade < 18])

serie_idade = serie_idade.apply(lambda x: 17 if x == 18 else x)
print(serie_idade.loc[serie_idade < 18])

serie_idade2 = serie_idade.iloc[0:6]

print(serie_idade2.where(serie_idade2 < 40, 0))
print(serie_idade2)
