import subprocess

# Comando que deseas ejecutar
comando = r"python -m PyInstaller --onefile --windowed --icon=resources\be.ico --name=BlackEdger interfaz.py"  # Por ejemplo, para listar los archivos en el directorio actual

# Ejecutar el comando en la terminal
subprocess.run(comando, shell=True)