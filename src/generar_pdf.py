from reportlab.pdfgen import canvas

def crear_pdf(datos, nombre_archivo):
    c = canvas.Canvas(nombre_archivo)
    c.drawString(100, 800, "Reporte de Ventas")
    y = 750
    for index, row in datos.iterrows():
        c.drawString(100, y, f"{row['Producto']}: ${row['Total']}")
        y -= 20
    c.save()
