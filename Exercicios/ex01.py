"""exercicio 1"""

import pandas as pd
import numpy as np

dataframe = pd.read_csv("Exercicios\\AirPassengers.csv")

print(type(dataframe))

print(dataframe)

series = pd.Series(
    np.array(dataframe["#Passengers"]), index=np.array(dataframe["Month"]))
series.index.name = "Month"

print(type(series))

print(series.index)
print(series.ndim)
print(series.count())
print(series.iloc[0:5])
print(series.head())
print(series.iloc[-5:])
print(series.tail())

print(series.iloc[0])

print(series.iloc[-1])
print(series["1960-08"])
print(series.sort_values(ascending=False))
print(series.sort_values())
print(series.sort_index(ascending=False))
print(series.sort_index())

print(series.value_counts())
print(series.loc[series > 300])
print(series.loc[series.index == "1954-07"])
print(series.loc["1950-08" > series.index])
print(series.loc[("1949-01" <= series.index) & (series.index < "1950-01")])
print(series.iloc[series.index.get_loc("1949-01"): series.index.get_loc("1950-01")])
print(series.sum())
print(series.mean())
print(series.min())
print(series.max())
print(series.loc[("1949-01" <= series.index)
      & (series.index < "1950-01")].sum())
print(series.iloc[series.index.get_loc("1949-01"): series.index.get_loc("1950-01")].sum())
print(series.index.unique())
print(series.isna().sum())
print(series)
print(pd.DatetimeIndex(series.index).month)
print(pd.DatetimeIndex(series.index).year)
print(series.loc[pd.DatetimeIndex(series.index).month == 7].sum())
print(series.loc[pd.DatetimeIndex(series.index).year == 1950].sum())
