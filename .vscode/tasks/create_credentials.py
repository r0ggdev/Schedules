import os
import sys

def create_credentials(email, password):
    # Ruta del archivo de credenciales en la raíz del sistema de archivos
    init_file_path = os.path.join(os.getcwd(), 'credentials.env')
    
    # Abrir el archivo en modo escritura y escribir los valores de EMAIL y PASSWORD
    with open(init_file_path, 'w') as file:
        file.write("EMAIL = " f"{email}" "\n")
        file.write("PASSWORD = " f"{password}")

    print(f"Archivo {init_file_path} creado con éxito.")

if __name__ == "__main__":
    email = sys.argv[1]
    password = sys.argv[2]

    create_credentials(email, password)
