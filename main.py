import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
from src.procesar_datos import procesar_datos

# Variables globales
datos = None

# Función para cargar archivo de ventas
def cargar_archivo():
    global datos
    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo Excel",
        filetypes=[("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*")]
    )
    if archivo:
        try:
            datos = procesar_datos(archivo)
            messagebox.showinfo("Éxito", "Archivo procesado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo procesar el archivo: {e}")

# Función para exportar datos a CSV
def exportar_datos():
    global datos
    if datos is None:
        messagebox.showwarning("Advertencia", "No hay datos procesados para exportar.")
        return

    archivo_salida = filedialog.asksaveasfilename(
        title="Guardar como",
        defaultextension=".csv",
        filetypes=[("Archivo CSV", "*.csv")]
    )
    if archivo_salida:
        try:
            datos.to_csv(archivo_salida, index=False)
            messagebox.showinfo("Éxito", "Datos exportados correctamente a CSV.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar el archivo: {e}")

# Función para visualizar datos en una tabla
def visualizar_datos():
    global datos
    if datos is None:
        messagebox.showwarning("Advertencia", "No hay datos procesados para visualizar.")
        return

    # Crear una nueva ventana para mostrar la tabla
    ventana_tabla = tk.Toplevel(ventana)
    ventana_tabla.title("Datos Procesados")
    ventana_tabla.geometry("800x400")

    # Crear tabla
    tabla = ttk.Treeview(ventana_tabla, columns=list(datos.columns), show='headings')
    
    # Configurar encabezados
    for col in datos.columns:
        tabla.heading(col, text=col)
        tabla.column(col, width=100)

    # Insertar datos
    for index, row in datos.iterrows():
        tabla.insert("", "end", values=list(row))

    # Empaquetar tabla
    tabla.pack(fill="both", expand=True)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Automatización de Procesos de Oficina")
ventana.geometry("400x300")

# Botón para cargar archivo
boton_cargar = tk.Button(ventana, text="Cargar Archivo de Ventas", command=cargar_archivo)
boton_cargar.pack(pady=10)

# Botón para exportar datos
boton_exportar = tk.Button(ventana, text="Exportar Datos a CSV", command=exportar_datos)
boton_exportar.pack(pady=10)

# Botón para visualizar datos
boton_visualizar = tk.Button(ventana, text="Visualizar Datos Procesados", command=visualizar_datos)
boton_visualizar.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
