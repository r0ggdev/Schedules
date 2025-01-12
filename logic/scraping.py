from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Scraper:
    def __init__(self, manager, url):
        self.manager = manager
        self.url = url
        self.wait = WebDriverWait(self.manager, 10)
        self.selector = {
            'login':{
                'user':(By.ID, 'ctl00_ContentPlaceHolder1_Login1_UserName'),
                'pwd': (By.ID, 'ctl00_ContentPlaceHolder1_Login1_Password'),
                'button': (By.XPATH, '//a[@href="javascript:InvocarForm();"]'),
                'after': 'Sócrates - Intranet'
            },
            'redirect':{
                'frame': 'principal',
                'submenu': (By.XPATH, '//font[@onclick="OpenSubmenu(sec4);"]'),
                'schedule': (By.XPATH, '//a[@href="Redirecciona.asp?iTipo=1&inum=27&nomasp=ic0014op.asp"]')
            },
            'extract':{
                'title': 'Sócrates - Intranet',
                'frame': 'F1',
                'info': (By.XPATH, '//b[text()="Horario de clases del ciclo"]'),
                'table_info': (By.XPATH, '//table[@align="left"]'),
                'table_schedule': (By.XPATH, '//table[@bgcolor="800000"]')
            }
        }

    def __tableScraper(self, _table, _rows=(By.TAG_NAME, 'tr'), _cells=(By.TAG_NAME, 'td')):
        """
        Extrae datos de una tabla HTML y los devuelve como un diccionario.
        
        :param _table: WebElement de la tabla HTML.
        :param _rows: Tupla con el método y el valor para localizar las filas (por defecto: (By.TAG_NAME, 'tr')).
        :param _cells: Tupla con el método y el valor para localizar las celdas (por defecto: (By.TAG_NAME, 'td')).
        :return: Diccionario con las filas de la tabla, donde las claves son los índices de las filas
                y los valores son diccionarios con los índices de las celdas y sus valores.
        """
        save_table = {}
        
        try:
            rows = _table.find_elements(*_rows)
            
            for row_index, row in enumerate(rows):
                cells = row.find_elements(*_cells)

                row_data = {}
                
                for cell_index, cell in enumerate(cells):
                    row_data[cell_index] = cell.text
                
                save_table[row_index] = row_data
                
        except Exception as e:
            print(f"Error al extraer datos de la tabla: {e}")
        
        return save_table
    
    def login(self, user, password):
        self.manager.get(self.url)
                
        self.wait.until( EC.presence_of_element_located(self.selector['login']['user']) ).send_keys(user)
        self.wait.until(EC.presence_of_element_located(self.selector['login']['pwd'])).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.selector['login']['button'])).click()
        
        try:
            self.wait.until(EC.title_is(self.selector['login']['after']))
            print("Login exitoso")
            return True
        
        except Exception as e:
            print("Credenciales incorrectas o el login no se completó correctamente.")
            return False
    
    def redirectSchedule(self):
        original_window = self.manager.current_window_handle
        #assert len(original_window) == 1, "Debe haber exactamente una ventana abierta"

        self.manager.switch_to.frame(self.selector['redirect']['frame'])
        self.wait.until( EC.element_to_be_clickable(self.selector['redirect']['submenu']) ).click()
        self.wait.until( EC.element_to_be_clickable(self.selector['redirect']['schedule']) ).click()
        
        self.wait.until( EC.number_of_windows_to_be(2) )

        for window_handle in self.manager.window_handles:
            if window_handle != original_window:
                self.manager.switch_to.window(window_handle)
                break

    def extractData(self):
        self.wait.until(EC.title_is(self.selector['extract']['title']))
        self.manager.switch_to.frame(self.selector['extract']['frame'])
        self.wait.until( EC.presence_of_element_located(self.selector['extract']['info']) )

        self.wait.until(EC.presence_of_element_located(self.selector['extract']['info']))
        table_info = self.__tableScraper(self.manager.find_element(*self.selector['extract']['table_info']))
        table_schedule = self.__tableScraper(self.manager.find_element(*self.selector['extract']['table_schedule']))

        self.manager.quit()

        return table_info, table_schedule 

    def controller(self, user, password):
        if not self.login(user, password):
            print("Fallo en el login.")
            return

        self.redirectSchedule()
        table_info, table_schedule = self.extractData()

        return table_schedule, table_info
    
def main():
    from .manager import DriverManager
    url = 'https://intranet.upc.edu.pe/loginintranet/loginupc.aspx'

    chrome_options = ["--headless", "--disable-gpu", "--window-size=1920x1080"]
    manager = DriverManager(driver_type= 'chrome', options= chrome_options)
    
    scraper = Scraper(manager, url)
    
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        user = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")

        if scraper.login(user, password):
            print("Login exitoso")
            break
        else:
            intentos += 1
            print(f"Login fallido. Intento {intentos}/{max_intentos}.")

        print("Se han alcanzado el número máximo de intentos. Cerrando el programa.")
        break 

if __name__ == '__main__':
    main()