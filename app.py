from flask import Flask, render_template, abort
import consults as cs

# Crear aplicación Flask
app = Flask(__name__)

# Lista de variables permitidas
VARIABLES = [
    "peso",
    "altura",
    "velocidad",
    "color"
]

# Ruta principal
@app.route("/")
def index():

    # Renderizar página principal
    return render_template(
        "index.html",
        variables=VARIABLES
    )

# Ruta dinámica para cada variable
@app.route("/variable/<nombre>")
def variable(nombre):

    # Validar que la variable exista
    if nombre not in VARIABLES:
        abort(404)

    # Cargar datos desde el CSV
    data = cs.load_data()

    # Obtener columna seleccionada
    columna = data[nombre]

    # Detectar si la variable es categórica
    tipo = "str" if nombre == "color" else "num"

    # Calcular frecuencia absoluta
    freq_abs = cs.frecuencia_absoluta(columna)

    # Calcular frecuencia relativa
    freq_rel = cs.frecuencia_relativa(columna)

    # Calcular frecuencia acumulada
    freq_acum = cs.frecuencia_acumulada(columna)

    # Obtener media, mediana y moda
    stats = cs.estadisticas(
        columna,
        tipo
    )

    # Generar gráfica de barras
    barras = cs.grafica_barras(
        freq_abs,
        nombre
    )

    # Generar gráfica de pastel
    pastel = cs.grafica_pastel(
        freq_rel,
        nombre
    )

    # Generar polígono de frecuencias
    poligono = cs.poligono_frecuencia(
        freq_abs,
        nombre
    )

    # Enviar información a la plantilla HTML
    return render_template(
        "variable.html",
        variable=nombre,
        freq_abs=freq_abs.to_dict(),
        freq_rel=freq_rel.to_dict(),
        freq_acum=freq_acum.to_dict(),
        stats=stats,
        barras=barras,
        pastel=pastel,
        poligono=poligono
    )

# Ejecutar servidor Flask
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )