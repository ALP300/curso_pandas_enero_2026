import pandas as pd
import numpy as np

datos= pd.read_csv("data.csv", encoding="latin-1")
print(datos.head())
print(datos.iloc[0:15])
print(datos.iloc[[0,23,45,67,89,123,456,789,1011,1213],])
print(datos.iloc[:,[3,9]])
print(datos.iloc[100:120, 2:5])