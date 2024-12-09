import os
from src.generar_pdf import crear_pdf

def test_crear_pdf():
    datos_ficticios = [
        {"Producto": "Producto A", "Total": 100},
        {"Producto": "Producto B", "Total": 200}
    ]
    # Convertir los datos en un DataFrame
    import pandas as pd
    df = pd.DataFrame(datos_ficticios)

    # Crear el PDF
    archivo_pdf = "data/reportes/test_reporte.pdf"
    crear_pdf(df, archivo_pdf)

    # Verificar si el archivo PDF fue creado
    assert os.path.exists(archivo_pdf)
    print("Prueba de generación de PDF exitosa.")

# Ejecutar prueba
test_crear_pdf()
