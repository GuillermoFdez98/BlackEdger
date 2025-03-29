import os
from PIL import Image
import tkinter as tk

# Steps:
#   1. Create white background with 1365 x 2048 px
#   2. Resize input photograph with large border to 1275 px
#   3. Paste input resized photo in center of background
#   4. Open logo
#   5. Resize logo to X px
#   6. Paste logo on previous photo
#   7. Save final output photo



BG_COLOR = (255, 255, 255)

INPUT_FOLDER_PATH = r"C:\Users\pipo1\Desktop\belgica\brujas"
OUTPUT_FOLDER_PATH = "output"
LOGO_FOLDER_PATH = r"resources/logo_azul.png"


# Función para agregar logs en el cuadro de texto
def agregar_log(logger, mensaje):
    logger.insert(tk.END, mensaje + "\n")
    logger.yview(tk.END)  # Para hacer scroll al final del log


def main(input_folder, output_folder, valores, logger, prev):
    
    try:
        # Crear la carpeta 'output' si no existe
        output_dir = os.path.join(input_folder, output_folder)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        logo = resize(Image.open(LOGO_FOLDER_PATH), valores["val1"])
        
        if logo.mode != 'RGBA':
            logo = logo.convert('RGBA')
            
        lista_archivos = [archivo for archivo in os.listdir(input_folder) if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        numero_errores = 0
        numero_correctas = 0
        
        agregar_log(logger, f"Imágenes encontradas: {len(lista_archivos)}\r\n")

        index = 1
        # Iterar por todos los archivos en la carpeta
        for archivo in lista_archivos:
            ruta_archivo = os.path.join(input_folder, archivo)
            
            # Comprobar si el archivo es una imagen
            if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                try:
                    # Abrir la imagen
                    imagen = Image.open(ruta_archivo).convert('RGBA')
                    
                    final_image = process_photo(imagen, logo, valores, prev).convert('RGB')
                    
                    # Guardar la nueva imagen en la carpeta 'output'
                    final_image.save(os.path.join(output_dir, f"{archivo}"), dpi=(valores["val5"],valores["val5"]))
                    agregar_log(logger, f"Imagen procesada ({index}/{len(lista_archivos)}): {archivo}")
                    numero_correctas += 1
                
                except Exception as e:
                    agregar_log(logger, f"ERROR: No se pudo procesar la imagen {archivo}: {e}")
                    numero_errores += 1
                    
                index += 1
        
        agregar_log(logger, "\r\nProceso terminado correctamente!")
        agregar_log(logger, f"Correctas: {numero_correctas}, Errores: {numero_errores}")
    
    except Exception as e:
        agregar_log(logger, f"{e}")

def process_photo(photo, logo, valores, prev):
    
    bg_width = int(valores["val4"] * 4 / 5)
    
    # Create white background with 1365 x 2048 px
    background = Image.new('RGBA', (bg_width, valores["val4"]), BG_COLOR)
    if prev:
        cuadrado = Image.new('RGBA', (bg_width, bg_width), (0, 255, 255))
    
    # Resize input photograph with large border to 1275 px
    image = resize(photo, valores["val3"])
    
    # Paste input resized photo in center of background
    pos_x = (background.width - image.width) // 2
    pos_y = (background.height - image.height) // 2
    
    if prev:
        background.paste(cuadrado, (((background.width - cuadrado.width) // 2), ((background.height - cuadrado.height) // 2)))
    
    background.paste(image, (pos_x, pos_y))
    
    # Paste logo on previous photo
    background.paste(logo, ((background.width - logo.width) // 2, background.height - valores["val1"] - valores["val2"]), logo.split()[3])
    
    # Return final output photo
    return background
   
   
def resize(photo, long_border):
    
    # Obtener el tamaño original
    ancho, alto = photo.size
    # Determinar la nueva altura o anchura manteniendo la relación de aspecto
    if ancho > alto:
        factor = long_border / ancho
        nuevo_ancho = long_border
        nuevo_alto = int(alto * factor)
    else:
        factor = long_border / alto
        nuevo_alto = long_border
        nuevo_ancho = int(ancho * factor)
    # Redimensionar la imagen usando el nuevo método de resampling
    imagen_redimensionada = photo.resize((nuevo_ancho, nuevo_alto), Image.Resampling.LANCZOS)
    
    return imagen_redimensionada