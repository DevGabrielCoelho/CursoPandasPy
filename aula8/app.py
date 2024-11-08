"""filtros"""
import pandas
import numpy
from faker import Faker

fake = Faker()

dataset = pandas.read_csv("census.csv")

index_paises = []

for i in range(32561):
    index_paises.append(fake.country())

series = pandas.Series(numpy.array(dataset["age"]), index=index_paises)

print(series.loc[series > 50])
print(series.loc[(series > 50) & (series.index == "India")])
print(series.index.isin(["India", "Brazil"]))
print(~series.index.isin(["India", "Brazil"]))
