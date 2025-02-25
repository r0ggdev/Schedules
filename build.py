import subprocess
import sys
import os

# # Ruta al archivo principal de tu proyecto
# main_script = "app.py"

# # Ruta al ícono (si lo tienes)
# icon_path = "gui/source/icon.ico"

# # Asegurarse de que las rutas de las carpetas son absolutas
# base_dir = os.path.dirname(os.path.abspath(__file__))
# gui_folder = os.path.join(base_dir, "gui")  # Carpeta gui
# logic_folder = os.path.join(base_dir, "logic")  # Carpeta logic

# # Obtener la lista de todos los archivos en las carpetas gui y logic
# gui_files = []
# logic_files = []

# # Buscar todos los archivos en gui y logic (recursivo si hay subcarpetas)
# for root, dirs, files in os.walk(gui_folder):
#     for file in files:
#         gui_files.append(os.path.join(root, file))

# for root, dirs, files in os.walk(logic_folder):
#     for file in files:
#         logic_files.append(os.path.join(root, file))

# # Carpeta de salida donde quieres que se guarden todos los archivos generados
# output_folder = "releases/v0.1a"  # Cambia esta ruta según lo necesites

# # Asegurarse de que la carpeta de salida exista
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# # Carpeta donde se guardarán los archivos temporales y la carpeta build
# work_folder = os.path.join(output_folder, "build")

# # Carpeta donde se guardará el archivo .spec de PyInstaller
# spec_folder = os.path.join(output_folder, "spec")

# # Crear las opciones de --add-data para incluir todos los archivos de gui y logic
# gui_add_data = f"--add-data={os.pathsep.join(gui_files)};gui"
# logic_add_data = f"--add-data={os.pathsep.join(logic_files)};logic"

# # Construir el comando de PyInstaller
# command = [
#     "pyinstaller",
#     "--onefile",  # Empaquetar todo en un solo archivo ejecutable
#     f"--icon={icon_path}",  # Establecer el ícono
#     gui_add_data,  # Incluir todos los archivos en 'gui'
#     logic_add_data,  # Incluir todos los archivos en 'logic'
#     f"--distpath={output_folder}",  # Ruta donde se guardará el ejecutable
#     f"--workpath={work_folder}",  # Ruta donde se guardarán los archivos temporales y la carpeta build
#     f"--specpath={spec_folder}",  # Ruta donde se guardará el archivo .spec
    
#     main_script  # El script principal de tu aplicación
# ]

# # Ejecutar el comando
# def run_pyinstaller(command):
#     try:
#         # Ejecutar el comando
#         subprocess.run(command, check=True)
#         print(f"¡Compilación exitosa! Los archivos generados se guardaron en {output_folder}")
        
#     except subprocess.CalledProcessError as e:
#         print(f"Hubo un error durante la compilación: {e}")
#         sys.exit(1)

# # Llamar a la función para ejecutar PyInstaller
# if __name__ == "__main__":
#     run_pyinstaller(command)

# def sub(dict, name, files):
#     dict.update({name: files})
#     return dict


# def getFiles(path):
#     files = os.listdir(path)
#     dict = {}
    
#     for file in files:
#         if file == "__pycache__":
#             files.remove(file)

#         elif os.path.isdir(os.path.join(path, file)):
#             files.remove(file)
#             dict = sub(dict, file, getFiles(os.path.join(path, file)))

#     files.append(dict)

#     return files




# files = {
#     "logo": "gui/source/logo.ico",
#     "main_script": "app.py",
#     "folders": {
#         "gui": {

#         },
#         "logic": [
#         ]
#     }
# }


# getfiles =  getFiles("gui")
# print(*getfiles)


# {
#     'source': {
#         'fonts': ['Poppins-Bold.ttf', 'Poppins-Medium.ttf', 'Poppins-Regular.ttf'], 
#         'icons': ['chevron_left.svg', 'chevron_right.svg', 'close.svg', 'close_fullscreen.svg', 'dark_mode.svg', 'home.svg', 'light_mode.svg', 'Logo@3x.png', 'night_light_auto.svg', 'question.svg', 'save.svg', 'table.svg']
#     }, 
#     'styles': ['dark.css', 'light.css']
# }

# [
#     'interface.py', 'paths.json', 'styles', 'tools.py', '__init__.py', 
    
#     {'source': ['icon.ico', 
#         { 
#             'fonts': ['Poppins-Bold.ttf', 'Poppins-Medium.ttf', 'Poppins-Regular.ttf', {}], 
#             'icons': ['chevron_left.svg', 'chevron_right.svg', 'close.svg', 'close_fullscreen.svg', 'dark_mode.svg', 'home.svg', 'light_mode.svg', 'Logo@3x.png', 'night_light_auto.svg', 'question.svg', 'save.svg', 'table.svg', {}]
#          }
#     ]
#     }
# ]


