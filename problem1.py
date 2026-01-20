import pandas as pd
import numpy as np

datos= pd.read_csv("data.csv", encoding="latin-1")
print(datos.head())
print(datos.info())
nuevo= pd.DataFrame(datos)
nuevo= nuevo.replace(np.nan, "0")
print(nuevo.info())
print(nuevo.describe())
nuevo= nuevo.replace("N/A", "0")
nuevo= nuevo.replace("NR", "0")
nuevo["Wsets"]= nuevo["Wsets"].astype(int)
nuevo["Lsets"]= nuevo["Lsets"].astype(int)
nuevo["W1"]= nuevo["W1"].astype(int)
nuevo["WRank"]= nuevo["WRank"].astype(int)
print(nuevo.describe())


