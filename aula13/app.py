"""valores faltantes"""

import pandas as pd
import numpy as np

series_faltante = pd.Series([1, 2, 3, np.nan, 5, np.nan])

print(series_faltante)
print(series_faltante.isna())
print(series_faltante.isna().sum())
print(series_faltante.value_counts(dropna=False))
print(series_faltante.value_counts())
print(series_faltante.fillna(0))
print(series_faltante.dropna())
print(series_faltante.fillna(series_faltante.mean()))

series_faltante = pd.Series(["Maçã", "Banana", "Arroz", "Arroz", np.nan, "Batata"])
print(series_faltante)
print(series_faltante.isna().sum())
print(series_faltante.fillna("Não Informado!"))
print(series_faltante.mode())
print(series_faltante.fillna(series_faltante.mode().iloc[0]))
