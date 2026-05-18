import pandas as pd
import matplotlib

# Configuración para servidores sin interfaz gráfica
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import os

# Carpeta donde se guardarán las gráficas
GRAPH_PATH = "static/graphs"

# Crear carpeta si no existe
os.makedirs(
    GRAPH_PATH,
    exist_ok=True
)

# Leer datos desde el archivo CSV
def load_data():

    df = pd.read_csv("datos.csv")

    # Eliminar valores nulos
    data = {
        "peso": df["peso"].dropna(),
        "altura": df["altura"].dropna(),
        "velocidad": df["velocidad"].dropna(),
        "color": df["color"].dropna()
    }

    return data

# Calcular frecuencia absoluta
def frecuencia_absoluta(data):

    return data.value_counts().sort_index()

# Calcular frecuencia relativa
def frecuencia_relativa(data):

    return round(
        data.value_counts(
            normalize=True
        ).sort_index(),
        2
    )

# Calcular frecuencia acumulada
def frecuencia_acumulada(data):

    return data.value_counts().sort_index().cumsum()

# Calcular media, mediana y moda
def estadisticas(data, tipo="num"):

    # Variables categóricas
    if tipo == "str":

        return {
            "media": "N/A",
            "mediana": "N/A",
            "moda": data.mode()[0]
        }

    # Variables numéricas
    return {
        "media": round(data.mean(), 2),
        "mediana": round(data.median(), 2),
        "moda": data.mode()[0]
    }

# Crear gráfica de barras
def grafica_barras(freq, variable):

    # Ruta de la imagen
    path = f"{GRAPH_PATH}/{variable}_barras.png"

    # Crear figura
    plt.figure(figsize=(8, 5))

    # Generar gráfica
    freq.plot(
        kind="bar",
        color="skyblue"
    )

    # Configurar títulos
    plt.title(
        f"Frecuencia Absoluta - {variable}"
    )

    plt.xlabel(variable)

    plt.ylabel("Frecuencia")

    # Ajustar márgenes
    plt.tight_layout()

    # Guardar imagen
    plt.savefig(path)

    # Liberar memoria
    plt.close()

    return path

# Crear gráfica de pastel
def grafica_pastel(freq, variable):

    path = f"{GRAPH_PATH}/{variable}_pastel.png"

    plt.figure(figsize=(7, 7))

    freq.plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.ylabel("")

    plt.title(
        f"Frecuencia Relativa - {variable}"
    )

    plt.tight_layout()

    plt.savefig(path)

    plt.close()

    return path

# Crear polígono de frecuencias
def poligono_frecuencia(freq, variable):

    path = f"{GRAPH_PATH}/{variable}_poligono.png"

    plt.figure(figsize=(8, 5))

    plt.plot(
        freq.index.astype(str),
        freq.values,
        marker="o",
        linestyle="-",
        color="red"
    )

    plt.title(
        f"Polígono de Frecuencias - {variable}"
    )

    plt.xlabel(variable)

    plt.ylabel("Frecuencia")

    plt.tight_layout()

    plt.savefig(path)

    plt.close()

    return path