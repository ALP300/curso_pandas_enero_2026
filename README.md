# Curso Pandas Enero 2026

Este proyecto contiene ejercicios y ejemplos de uso de la librería **pandas** en Python, analizando datos del ATP Tour (tenis).

## Requisitos

pip install pandas numpy

## Configuración del Dataset

Para ejecutar los scripts, necesitas descargar el archivo de datos `data.csv`.

1.  Ve a la siguiente página de Kaggle: [ATP Tour 2000-2016 Dataset](https://www.kaggle.com/datasets/jordangoblet/atp-tour-20002016?resource=download)
2.  Descarga el archivo CSV.
3.  Renombra el archivo descargado a `data.csv` (si tiene otro nombre).
4.  Coloca el archivo `data.csv` en la carpeta raíz de este proyecto (la misma carpeta donde están los archivos `.py`).

## Archivos del Proyecto

*   **index.py**: Script principal con ejemplos básicos de carga de datos, creación de DataFrames manuales, limpieza de valores nulos (NaN) y conversión de tipos de datos.
*   **problem1.py**: Script que carga el dataset del ATP Tour, realiza limpieza de datos (reemplazo de nulos y valores "NR", "N/A") y convierte columnas a tipos numéricos para su análisis.
*   **problem2.py**: Archivo reservado para futuros ejercicios.

## Ejecución

Para correr el script principal:

```bash
python index.py
```

Para correr la solución del problema 1:

```bash
python problem1.py
```
