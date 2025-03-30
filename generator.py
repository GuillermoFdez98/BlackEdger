import subprocess

# Comando que deseas ejecutar
command_list = [
    r"env\Scripts\activate",
    r"python -m PyInstaller --onefile --noconsole --icon=resources\be.ico --name=BlackEdger interfaz.py & xcopy /e /i /Y resources dist\resources",
    r"env\Scripts\deactivate",
]

for command in command_list:
    # Ejecutar el comando en la terminal
    subprocess.run(command, shell=True)