"""dataframe"""

import pandas as pd
import numpy as np

data = [
    ["Alice", 25, "Sao Paulo"],
    ["Lucas", 45, "Para"],
    ["Vinicius", 35, "Rio de Janeiro"],
    ["Pedro", 15, "Minas Gerais"]
]

colunas = ["Nome", "Idade", "Estado"]

data_frame = pd.DataFrame(data, columns=colunas)

print(data_frame)

data_frame = pd.DataFrame(
    # usando dicionario!
    {
        'Nome': ["Ricardo", "Daniel", "Paulo", "Eduardo"],
        'Idade': [18, 19, 21, 17],
        'Estado': ["Minas", "Minas", "Minas", "Minas"]
    }
)

print(data_frame)

data_frame = pd.DataFrame(
    # usando array
    np.array([
        ["Alice", 25, "Sao Paulo"],
        ["Lucas", 45, "Para"],
        ["Vinicius", 35, "Rio de Janeiro"],
        ["Pedro", 15, "Minas Gerais"]
    ]),
    columns=colunas
)

print(data_frame)

data_frame = pd.DataFrame(
    # usando lista/serie
    [
        ("Alice", 25, "Sao Paulo"),
        ("Lucas", 45, "Para"),
        ("Vinicius", 35, "Rio de Janeiro"),
        ("Pedro", 15, "Minas Gerais")
    ],
    columns=colunas
)

print(data_frame)

data_frame = pd.DataFrame(
    # usando dicionario com series
    {
        'Nome': pd.Series(["Ricardo", "Daniel", "Paulo", "Eduardo"]),
        'Idade': pd.Series([18, 19, 21, 17]),
        'Estado': pd.Series(["Minas", "Minas", "Minas", "Minas"])
    }
)

print(data_frame)

data_frame = pd.DataFrame(
    # usando dicionario com array
    {
        'Nome': np.array(["Ricardo", "Daniel", "Paulo", "Eduardo"]),
        'Idade': np.array([18, 19, 21, 17]),
        'Estado': np.array(["Minas", "Minas", "Minas", "Minas"])
    }
)

print(data_frame)
