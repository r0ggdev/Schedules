import os
import sys
import subprocess
import time

def generate_log_name(test_name):
    log_name = f"{test_name}_{time.strftime("%Y-%m-%d_%H-%M-%S")}.log"
    return log_name

def run_tests(test_folder, test_name):
    # Generar el nombre del archivo de log
    log_name = generate_log_name(test_name)
    log_path = os.path.join('tests', 'logs', log_name)

    # Crear la carpeta de logs si no existe
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    python_path = sys.executable 
    
    # Ejecutar los tests
    command = [
        python_path, "-m", "unittest", f"{test_folder}.{test_name}"
    ]
    
    # Abrir el archivo de log para redirigir la salida
    with open(log_path, "w") as log_file:
        # Ejecutar el comando y redirigir la salida al archivo de log
        subprocess.run(command, stdout=log_file, stderr=subprocess.STDOUT)

    print(f"Tests ejecutados. Los resultados están en: {log_path}")

if __name__ == "__main__":
    # Recibir parámetros desde la línea de comandos
    test_folder = sys.argv[1]
    test_name = sys.argv[2]

    # Ejecutar la función principal
    run_tests(test_folder, test_name)
