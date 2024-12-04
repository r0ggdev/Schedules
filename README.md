# 📅⬇️ Descargar e importar horario en **Google Calendar**

Este proyecto se desarrolló como una solución para automatizar el proceso de importar el horario del ciclo a la aplicación de **Google Calendar**.

Para la creación de esta herramienta, se utilizó la técnica de **web scraping** con el lenguaje de programación **Python**, junto con la librería **Selenium**.

## **Guía de Ejecución desde VSCode**

Para facilitar el proceso de configuración del entorno de desarrollo y la instalación de las dependencias, cree **tareas automatizadas en VSCode**. Solo necesitas ejecutar una tarea para crear un entorno virtual y asegurarte de que todas las dependencias se instalen correctamente.

1. **Abre el proyecto en VSCode**:
   Si aún no lo has hecho, abre **VSCode** y carga el proyecto mediante `File > Open Folder...`.

2. **Verifica que las tareas estén configuradas**:
   Asegúrate de que el archivo `tasks.json` se encuentre en el directorio `.vscode`. Si no está presente, configura el entorno manualmente siguiendo las instrucciones en la sección de **[Instalación y Configuración entorno virtual [Manual]](#instalación-y-configuración-manual)**.

3. **Ejecutar la tarea para crear el entorno virtual y las dependencias**:
   
   En VSCode, puedes ejecutar una tarea a través del panel de comandos. Para ello, sigue estos pasos:
   
   - Abre la **Paleta de Comandos** en VSCode con `Ctrl + Shift + P`.
   - Escribe **Run Task** y selecciona **"🐍 createVirtualEnvironment"**.
   
   Este comando ejecutará una serie de acciones:
   - Verificará si el entorno virtual `.env` ya existe.
   - Si no existe, creará el entorno virtual y luego instalará las dependencias desde el archivo `requirements.txt`.
   - Si el entorno virtual ya está creado, solo instalará las dependencias.
   - 
4. **Ejecutar tarea para Ejecutar el proyecto**
   - Abre la **Paleta de Comandos** en VSCode con `Ctrl + Shift + P`.
   - Escribe **Run Task** y selecciona **Ejecutar el proyecto"**.


## Instalación y Configuración [Manual] 
> 💡 Comandos básicos: 
 > - cd : moverse entre directorios
 > - pwd : para mostrar del directorio actual
 > - ls : para mostrar los archivos de la carpeta


 ### Entorno virtual

 1. Dentro de una terminal (powershell) nos dirigiremos hacía la ruta del repositorio clonado

    ~~~PS
     # Creamos el entorno virutal
    python -m venv .env
    ~~~

 2. Activamos el entorno virtual con el comando
 
    ~~~PS
    # Use este comando para activar el entorno virtual
    .\.env\Scripts\activate
    ~~~
    
 3. Instalamos los requerimientos
    
    ~~~PS
    pip install -r requirements.txt
    ~~~

 ### Ejecutar proyecto
   ~~~PS
   python app.py
   ~~~
