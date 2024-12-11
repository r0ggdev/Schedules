from manager import *
from register import Register 
from cleaned import *
import time

WEB_URL = 'https://intranet.upc.edu.pe/loginintranet/loginupc.aspx' # URL del la pagina

EXPORTS = './exports/' # Directorio de exportacion
INFO = './exports/original/data.json' # Nombre del archivo JSON con la informacion del alumno
HORARIO = './exports/original/horario.json' # Nombre del archivo JSON con el horario del alumno

def logOut(manager, wait):
    # logout del sistema
    manager.switch_to.frame('encabezado') # Cambiamos al frame del encabezado
    logout = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="Redirecciona.asp?iTipo=2&nomasp=https://matricula.upc.edu.pe/"]'))
    )
    logout.click()

def tableScraper(_table, _rows = (By.TAG_NAME, 'tr'), _cells = (By.TAG_NAME, 'td')):
    """
    Extrae datos de una tabla HTML.
    
    :param _table: WebElement de la tabla HTML.
    :param _rows: Tupla con el método y el valor para localizar las filas (por defecto: (By.TAG_NAME, 'tr')).
    :param _cells: Tupla con el método y el valor para localizar las celdas (por defecto: (By.TAG_NAME, 'td')).
    :return: Lista de listas con los datos de las celdas de la tabla.
    """
    save_table = []
    try:
        rows = _table.find_elements(_rows[0], _rows[1])
        
        for row in rows:
            cells = row.find_elements(_cells[0], _cells[1])
            cell_data = [cell.text for cell in cells]
            save_table.append(cell_data)

    except Exception as e:
        print(f"Error al extraer datos de la tabla: {e}")
    
    return save_table


def main():    
    CREDENTIALS = Register() # Creamos una instancia de la clase Register
    manager = DriverManager() # Creamos una instancia de la clase DriverManager
    wait = WebDriverWait(manager, 10) # Creamos una instancia de WebDriverWait

    manager.get(WEB_URL) # Abrimos el navegador en la URL
    
    # Login al sistema
    email_field = manager.find_element(By.ID, 'ctl00_ContentPlaceHolder1_Login1_UserName')
    pwd_field =manager.find_element(By.ID, 'ctl00_ContentPlaceHolder1_Login1_Password')

    email_field.send_keys(CREDENTIALS.get_email())
    pwd_field.send_keys(CREDENTIALS.get_password())

    manager.find_element(By.XPATH, '//a[@href="javascript:InvocarForm();"]').click() # Click en el boton de login

    # Guardamos el ID de la ventana actual
    original_window = manager.current_window_handle

    # Verificamos que esta sea la unica ventana abierta
    assert len(manager.window_handles) == 1

    # Accedemos a la etiqueta horario (Padre)   
    manager.switch_to.frame('principal') # Cambiamos al frame principal
    tag = wait.until(

        # Despliega el submenu de horario
        EC.element_to_be_clickable((By.XPATH, '//font[@onclick="OpenSubmenu(sec4);"]'))
    )

    tag.click()

    # Accedemos al horario (Hijo)
    tag_child = wait.until(

        # Redirecciona a la pagina del horario
        EC.element_to_be_clickable((By.XPATH, '//a[@href="Redirecciona.asp?iTipo=1&inum=27&nomasp=ic0014op.asp"]')) 
    )

    tag_child.click()

    # Esperamos a que se abra una nueva ventana
    wait.until(EC.number_of_windows_to_be(2)) 

    # Itera en las ventanas existentes y cambia a la nueva ventana
    for window_handle in manager.window_handles:
        if window_handle != original_window:
            manager.switch_to.window(window_handle)
            break
    
    # Esperamos a que la pagina cargue
    wait.until(EC.title_is('Sócrates - Intranet')) 

    #?? Recuperamos el nuevo link de la pagina
    print("Link de la nueva pagima: " + manager.current_url)

    # Cambiamos al cuerpo del horario
    manager.switch_to.frame('F1')

    wait.until(
        EC.presence_of_element_located((By.XPATH, '//b[text()="Horario de clases del ciclo"]'))
    )

    # Recuperamos y guardamos el info en un archivo CSV
    table_info = tableScraper(_table = manager.find_element(By.XPATH, '//table[@align="left"]'))
    saveTable(table_info, INFO)

    # Recuperamos y guardamos el horario en un archivo CSV
    table_schedule = tableScraper(_table = manager.find_element(By.XPATH, '//table[@bgcolor="800000"]'))
    saveTable(table_schedule, HORARIO)

    clean_info(INFO, EXPORTS + 'cleaned/alumno.json')
    procesar_horario(HORARIO, EXPORTS + 'cleaned/horario.json')

    # Esperamos 5 segundos
    time.sleep(5)

# Run the main function
if __name__ == '__main__':
    main()