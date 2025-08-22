import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from main import main
import os
import threading
import json

VERSION = "v0.6.0"
output_folder_path = "output"

valores = {
    "val1": 0,
    "val2": 0,
    "val3": 0,
    "val4": 0,
    "val5": 0,
    "val6": "",
}

def leer_valores_json():
    try:
        with open(r"resources\valores.json", "r") as archivo_json:
            valores = json.load(archivo_json)
            return valores
    except FileNotFoundError:
        print("El archivo 'valores.json' no se encuentra.")
        return None
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON. Puede estar vacío o dañado.")
        return None

def agregar_log(mensaje):
    log_text.insert(tk.END, mensaje + "\n")
    log_text.yview(tk.END)

def iniciar_proceso():
    ruta = entry_ruta.get()
    if not os.path.exists(ruta):
        agregar_log("Error: La ruta especificada no existe.")
        return
    agregar_log(f"Iniciando el proceso con la ruta: {ruta}")
    
    valores = leer_valores_json()
    
    # Ejecutar la función principal en un hilo separado
    thread = threading.Thread(target=main, args=(ruta, valores["val6"], valores, log_text, formato_variable_opcion, orientacion_variable_opcion,var_logo,))
    thread.start()

# Función de previsualización
def previsualizar(ruta):
    agregar_log(f"Previsualización activada. Mostrando vista previa para la ruta: {ruta}")
    # Aquí puedes agregar la lógica de previsualización (por ejemplo, mostrar un mensaje o realizar una operación leve)
    # Este es un ejemplo genérico, puedes personalizarlo con lo que necesites
    # Puedes agregar imágenes, mostrar un resumen, etc.
    messagebox.showinfo("Previsualización", f"Mostrando vista previa de la ruta: {ruta}")

def abrir_ventana_acerca():
    ventana_secundaria = tk.Toplevel(ventana)
    ventana_secundaria.title("Acerca de")

    ventana_secundaria.iconbitmap(r'resources\be.ico')

    ventana_secundaria.geometry("200x100+560+240")

    valor1_label = tk.Label(ventana_secundaria, text=f"Versión actual\n{VERSION}")
    valor1_label.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')

    ventana_secundaria.grid_rowconfigure(0, weight=1)
    ventana_secundaria.grid_columnconfigure(0, weight=1)

# Función para abrir la ventana secundaria con campos numéricos
def abrir_ventana_secundaria():
    ventana_secundaria = tk.Toplevel(ventana)
    ventana_secundaria.title("Configuración")

    ventana_secundaria.iconbitmap(r'resources\be.ico')
    
    valores = leer_valores_json() or {
        "val1": 0,
        "val2": 0,
        "val3": 0,
        "val4": 0,
        "val5": 0,
        "val6": "",
    }

    # Variables para los valores numéricos
    valor1_label = tk.Label(ventana_secundaria, text="Tamaño logo:")
    valor1_label.grid(row=0, column=0, padx=10, pady=5)
    valor1_entry = tk.Entry(ventana_secundaria)
    valor1_entry.insert(0, valores["val1"])
    valor1_entry.grid(row=0, column=1, padx=10, pady=5)

    valor2_label = tk.Label(ventana_secundaria, text="Separación logo:")
    valor2_label.grid(row=1, column=0, padx=10, pady=5)
    valor2_entry = tk.Entry(ventana_secundaria)
    valor2_entry.insert(0, valores["val2"])
    valor2_entry.grid(row=1, column=1, padx=10, pady=5)

    valor3_label = tk.Label(ventana_secundaria, text="Tamaño marco:")
    valor3_label.grid(row=2, column=0, padx=10, pady=5)
    valor3_entry = tk.Entry(ventana_secundaria)
    valor3_entry.insert(0, valores["val3"])
    valor3_entry.grid(row=2, column=1, padx=10, pady=5)
    
    valor4_label = tk.Label(ventana_secundaria, text="Tamaño imagen final:")
    valor4_label.grid(row=3, column=0, padx=10, pady=5)
    valor4_entry = tk.Entry(ventana_secundaria)
    valor4_entry.insert(0, valores["val4"])
    valor4_entry.grid(row=3, column=1, padx=10, pady=5)
    
    valor5_label = tk.Label(ventana_secundaria, text="PPP:")
    valor5_label.grid(row=4, column=0, padx=10, pady=5)
    valor5_entry = tk.Entry(ventana_secundaria)
    valor5_entry.insert(0, valores["val5"])
    valor5_entry.grid(row=4, column=1, padx=10, pady=5)
    
    valor6_label = tk.Label(ventana_secundaria, text="Carpeta salida:")
    valor6_label.grid(row=5, column=0, padx=10, pady=5)
    valor6_entry = tk.Entry(ventana_secundaria)
    valor6_entry.insert(0, valores["val6"])
    valor6_entry.grid(row=5, column=1, padx=10, pady=5)
    
    # Función para restaurar valores predeterminados en la ventana secundaria
    def restaurar_valores_predeterminados():
        # Valores predeterminados
        valores_por_defecto = {
            "val1": 60,
            "val2": 30,
            "val3": 120,
            "val4": 2048,
            "val5": 72,
            "val6": "output",
        }

        # Restaurar los valores por defecto en los campos de texto
        valor1_entry.delete(0, tk.END)
        valor1_entry.insert(0, valores_por_defecto["val1"])
        valor2_entry.delete(0, tk.END)
        valor2_entry.insert(0, valores_por_defecto["val2"])
        valor3_entry.delete(0, tk.END)
        valor3_entry.insert(0, valores_por_defecto["val3"])
        valor4_entry.delete(0, tk.END)
        valor4_entry.insert(0, valores_por_defecto["val4"])
        valor5_entry.delete(0, tk.END)
        valor5_entry.insert(0, valores_por_defecto["val5"])
        valor6_entry.delete(0, tk.END)
        valor6_entry.insert(0, valores_por_defecto["val6"])

        # Actualizar el diccionario valores y guardarlos en el archivo JSON
        with open(r"resources\valores.json", "w") as archivo_json:
            json.dump(valores_por_defecto, archivo_json, indent=4)

        # Agregar mensaje de log o notificación al usuario
        agregar_log("Valores restaurados a los valores predeterminados.")

    # Botón para procesar los valores
    def procesar_valores():
        try:
            # Obtener los valores de los campos de entrada
            val1 = int(valor1_entry.get())
            val2 = int(valor2_entry.get())
            val3 = int(valor3_entry.get())
            val4 = int(valor4_entry.get())
            val5 = int(valor5_entry.get())
            val6 = valor6_entry.get()
            
            # Guardar los valores en un diccionario
            valores["val1"] = val1
            valores["val2"] = val2
            valores["val3"] = val3
            valores["val4"] = val4
            valores["val5"] = val5
            valores["val6"] = val6
            
            # Guardar los valores en un archivo JSON
            with open(r"resources\valores.json", "w") as archivo_json:
                json.dump(valores, archivo_json, indent=4)

            # Agregar mensaje de log o imprimir en consola (puedes cambiar esta función)
            agregar_log(f"Valores guardados: \r\nTamaño logo: {val1} \r\nSeparación logo: {val2} \r\nTamaño fotografía: {val3} \r\nTamaño imagen final: {val4} \r\nPPP: {val5}\r\nCarpeta salida: {val6}")
            
            # Cierra la ventana secundaria después de procesar
            ventana_secundaria.destroy()

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")
    
    # Botón para procesar los valores
    boton_procesar = tk.Button(ventana_secundaria, text="Aplicar", command=procesar_valores)
    boton_procesar.grid(row=6, columnspan=2, padx=10, pady=10)

    # Botón para restaurar los valores predeterminados
    boton_restaurar = tk.Button(ventana_secundaria, text="Valores predeterminados", command=restaurar_valores_predeterminados)
    boton_restaurar.grid(row=7, columnspan=2, padx=10, pady=10)
    
# Botón para abrir el explorador de archivos y seleccionar una ruta
def seleccionar_ruta():
    ruta = filedialog.askdirectory(title="Seleccionar ruta")
    if ruta:
        entry_ruta.delete(0, tk.END)
        entry_ruta.insert(0, ruta)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("BlackEdger")
# ventana.geometry("800x600+100+50")

ventana.iconbitmap(r'resources\be.ico')

# Variable para el checkbox "Previsualizar"
var_previsualizar = tk.IntVar()
var_logo = tk.IntVar(value=1)

# Variable que almacena la opción seleccionada
formato_variable_opcion = tk.StringVar(ventana)
orientacion_variable_opcion = tk.StringVar(ventana)

# Lista de formato_op para el menú desplegable
formato_op = ["5:4", "1:1", "4:3", "Original"]
orientacion_op = ["Vertical", "Horizontal"]

# Establecer la opción por defecto (la primera opción)
formato_variable_opcion.set(formato_op[0])
orientacion_variable_opcion.set(orientacion_op[0])

# Checkbox de previsualización
checkbox_previsualizar = tk.Checkbutton(ventana, text="Previsualizar", variable=var_previsualizar)
# checkbox_previsualizar.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Botón para abrir la ventana secundaria de valores numéricos
boton_valores = tk.Button(ventana, text="Configuración", command=abrir_ventana_secundaria)
boton_valores.grid(row=0, column=0, padx=10, pady=5)

# Botón para abrir la ventana secundaria de valores numéricos
boton_acerca = tk.Button(ventana, text="Acerca de", command=abrir_ventana_acerca)
boton_acerca.grid(row=0, column=1, padx=10, pady=5)

# Etiqueta para la ruta
label_ruta = tk.Label(ventana, text="Ruta:")
label_ruta.grid(row=1, column=0, padx=10, pady=5, sticky="w")

# Campo de texto para la ruta
entry_ruta = tk.Entry(ventana, width=40)
entry_ruta.grid(row=1, column=1, padx=10, pady=5, sticky="w")

boton_explorar = tk.Button(ventana, text="Seleccionar carpeta", command=seleccionar_ruta)
boton_explorar.grid(row=1, column=2, padx=10, pady=5, sticky="w")

# Crear el menú de formato
menu_formato = tk.OptionMenu(ventana, formato_variable_opcion, *formato_op)
menu_formato.grid(row=2, column=0, padx=10, pady=5)

# Crear el menú orientacion
menu_orientacion = tk.OptionMenu(ventana, orientacion_variable_opcion, *orientacion_op)
menu_orientacion.grid(row=2, column=1, padx=10, pady=5)

# Checkbox de añadir logo o no
checkbox_proporcional = tk.Checkbutton(ventana, text="Logo", variable=var_logo)
checkbox_proporcional.grid(row=2, column=2, padx=10, pady=5, sticky="w")

# Botón para iniciar el proceso
boton_iniciar = tk.Button(ventana, text="Iniciar Proceso", command=iniciar_proceso)
boton_iniciar.grid(row=3, columnspan=3, padx=10, pady=10)

# Área de log
label_log = tk.Label(ventana, text="Log:")
label_log.grid(row=4, column=0, padx=10, pady=5, sticky="w")

log_text = tk.Text(ventana, width=50, height=10, wrap=tk.WORD)
log_text.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

# Hacer que la ventana sea responsiva
ventana.mainloop()
