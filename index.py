import pandas as pd
import numpy as np
'''
datos= pd.read_csv("data.csv", encoding="latin-1")
print(datos.head())
'''
datos= {'Nombre': ['Juan', 'Maria', 'Pedro', 'Ana', 'Luis', 'Luisa', 'Luis', 'Luisa', 'Luis', 'Luisa'],
        'Apellido': ['Garcia', 'Rodriguez', 'Martinez', 'Gonzalez', 'Fernandez', 'Garcia', 'Rodriguez', 'Martinez', 'Gonzalez', 'Fernandez'],
        'Materias': ['Matematicas', 'Fisica', 'Quimica', 'Biologia', 'Historia', 'Matematicas', 'Fisica', 'Quimica', 'Biologia', 'Historia'],
        'Edad': ['25', '30', '35', '40', '45', '25', '30', '35', '40', '45'],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Valencia', 'Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Valencia']}

df= pd.DataFrame(datos)
print(df.head())

datos2= {
    'Nombre': ['Juan', 'Maria', 'Pedro', 'Ana', 'Luis', 'Luisa', 'N/A', 'Luisa', 'Luis', 'Luisa'],
    'Apellido': ['Garcia', 'Rodriguez', 'Martinez', 'N/A', 'Fernandez', 'Garcia', 'Rodriguez', 'Martinez', 'Gonzalez', 'Fernandez'],
    'Materias': ['Matematicas', 'Fisica', 'Quimica', 'Biologia', 'Historia', 'Matematicas', 'Fisica', 'Quimica', 'Biologia', 'Historia'],
    'Edad': ['25', '30', '35', '40', '45', '25', '30', '35', np.nan, '45'],
    'Tamaño': ['1.70', '1.60', '1.80', '1.75', '1.85', np.nan, '1.60', '1.80', '1.75', '1.85'],
    'Ciudad': ['Madrid', 'N/A', 'Valencia', 'Sevilla', 'Valencia', 'Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Valencia']
}
df2= pd.DataFrame(datos2)
print(df2.info())
print("\n"*5)
print(df2.head(10))
print("\n"*5)
print(df2.info())
print("\n"*5)
nuevo= df2.replace(np.nan,"0")
print(nuevo.info())                  
print("\n"*5)

nuevo["Edad"]= nuevo["Edad"].astype(int)
nuevo["Tamaño"]= nuevo["Tamaño"].astype(float)
print(nuevo.info())
print("\n"*5)


print(nuevo.describe(include="all"))
