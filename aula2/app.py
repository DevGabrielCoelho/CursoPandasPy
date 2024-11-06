"""fatiamento de dados"""

import pandas as pd
import numpy as np

serie__dados = pd.Series(np.random.random(10), np.arange(10))

print(serie__dados)

print(serie__dados[:])
print(serie__dados[0:3])
print(serie__dados[0:4])
print(serie__dados[-1:])
print(serie__dados[:-1])

x = serie__dados[:3]

print(x)
