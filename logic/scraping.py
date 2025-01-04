from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class Scraper:
    
    def __init__(self, manager, url):
        
        self.manager = manager
        self.url = url

    
    def tableScraper(self, _table, _rows = (By.TAG_NAME, 'tr'), _cells = (By.TAG_NAME, 'td')):
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

    def login(self, user, password):
        self.manager.get(self.url)
        email_field = self.manager.find_element(By.ID, 'ctl00_ContentPlaceHolder1_Login1_UserName')
        pwd_field =self.manager.find_element(By.ID, 'ctl00_ContentPlaceHolder1_Login1_Password')

        email_field.send_keys(user)
        pwd_field.send_keys(password)

        self.manager.find_element(By.XPATH, '//a[@href="javascript:InvocarForm();"]').click()
    # Esperar unos segundos para ver si aparece la alerta
        time.sleep(2)  # Usa WebDriverWait para un enfoque más robusto
        
        try:
            # Intentar manejar la alerta si aparece
            alert = WebDriverWait(self.manager, 10).until(EC.alert_is_present())
            #alert = self.manager.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_lblError"]')
            alert_text = alert.text
            
            if "La contraseña debe tener minimo 8 caracteres" in alert_text:
                print("Error: La contraseña es demasiado corta")
                alert.accept()  # Cerrar la alerta
                return False  # Indicar que la autenticación ha fallado

            elif "Usuario incorrecto o usuario y contraseña incorrectos." in alert_text:
                print("Error: Usuario o contraseña incorrectos")
                alert.accept()  # Cerrar la alerta
                return False  # Indicar que la autenticación ha fallado
            
            else:
                print(f"Alerta inesperada: {alert_text}")
                alert.accept()
                return False
        
        except Exception as e:
            # Si no aparece alerta, es posible que el login haya sido exitoso
            print("Login exitoso o sin alertas.")
            return True  # Login exitoso (sin alerta)


    def getData(self):
        wait = WebDriverWait(self.manager, 10)
        # Guardamos el ID de la ventana actual
        original_window = self.manager.current_window_handle

        # Verificamos que esta sea la unica ventana abierta
        assert len(self.manager.window_handles) == 1

        # Accedemos a la etiqueta horario (Padre)   
        self.manager.switch_to.frame('principal') # Cambiamos al frame principal
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
        for window_handle in self.manager.window_handles:
            if window_handle != original_window:
                self.manager.switch_to.window(window_handle)
                break
        
        # Esperamos a que la pagina cargue
        wait.until(EC.title_is('Sócrates - Intranet'))
        
        # Cambiamos al cuerpo del horario
        self.manager.switch_to.frame('F1')

        wait.until(
            EC.presence_of_element_located((By.XPATH, '//b[text()="Horario de clases del ciclo"]'))
        )

        table_info = self.tableScraper(_table = self.manager.find_element(By.XPATH, '//table[@align="left"]'))
        table_schedule = self.tableScraper(_table = self.manager.find_element(By.XPATH, '//table[@bgcolor="800000"]'))

        self.manager.quit()

        return table_schedule, table_info
    
