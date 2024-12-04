import os
import sys

def run_tests(test_folder):

    folder_path = os.path.join('tests', test_folder)

    os.makedirs(folder_path, exist_ok=True)
    
    init_file_path = os.path.join(folder_path, '__init__.py')
    
    with open(init_file_path, 'w'):
        pass  # Solo para crear el archivo vacío

    print(f"Paquete {test_folder} creado con éxito en: {folder_path}")

if __name__ == "__main__":

    test_folder = sys.argv[1]
    run_tests(test_folder)
