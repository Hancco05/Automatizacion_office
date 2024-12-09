from src.procesar_datos import procesar_datos
from src.generar_pdf import crear_pdf
from src.enviar_correo import enviar_correo

# Ruta de archivos
archivo_ventas = "data/ventas.xlsx"
reporte_pdf = "data/reportes/reporte_ventas.pdf"

# Procesar datos
datos_procesados = procesar_datos(archivo_ventas)

# Generar PDF
crear_pdf(datos_procesados, reporte_pdf)

# Enviar correo
enviar_correo(
    destinatario="destinatario@gmail.com",
    asunto="Reporte de Ventas",
    cuerpo="Adjunto encontrarás el reporte de ventas.",
    archivo_adj=reporte_pdf
)
print("Automatización completada.")
