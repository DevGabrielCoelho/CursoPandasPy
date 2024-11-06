"""cópia, conversao e concatenação de dados"""

import pandas as pd
import numpy as np

serie__dados = pd.Series(np.random.random(10), np.arange(10))

print(serie__dados)

serie__dados2 = serie__dados.copy()

print(serie__dados2)

serie__dados2 = serie__dados2.astype(int)

print(serie__dados2)

dados_novos = {
  'A': 30,
  'B': 40
}

serie__dados3 = pd.Series(dados_novos)

serie__dados4 = pd.concat([serie__dados2, serie__dados3])

print(serie__dados4)
