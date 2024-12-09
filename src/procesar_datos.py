import pandas as pd

def procesar_datos(ruta_archivo):
    # Leer archivo Excel
    datos = pd.read_excel(ruta_archivo)
    # Procesar datos (por ejemplo, calcular totales por producto)
    reporte = datos.groupby('Producto')['Total'].sum().reset_index()
    return reporte
