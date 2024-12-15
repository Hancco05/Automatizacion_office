import pandas as pd

def procesar_datos(ruta_archivo):
    # Leer el archivo Excel
    datos = pd.read_excel(ruta_archivo)

    # Procesamiento de datos (ejemplo simple: añadir columna calculada)
    datos['Total'] = datos['Cantidad'] * datos['Precio']

    return datos
