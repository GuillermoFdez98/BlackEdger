# BlackEdger

A Windows application on Python to add an edge to photographies.

## Set environment guide

1. Create virtual environment.

   ```
   python -m venv env
   ```
2. Install requirements for environment.

   ```
   pip install -r requirements.txt
   ```

## Exe generation guide

You can execute the autogenerator script o do it manually.

### Autogenerator script

1. Execute generator script using Python.
   ```
   python3 generator.py
   ```

### Manually commands

1. Activate venv.

   ```
   env\Scripts\activate
   ```
2. Generate .exe from script.

   ```
   python -m PyInstaller --onefile --noconsole --icon=resources\be.ico --name=BlackEdger interfaz.py & xcopy /e /i /Y resources dist\resources
   ```
3. Deactivate venv.

   ```
   env\Scripts\deactivate
   ```
