from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class DriverManager:
    """
    Clase encargada de manejar el WebDriver de Selenium usando el patrón Singleton.
    
    :param driver_type: str: Tipo de navegador (chrome, firefox, edge, safari, ie), por defecto es 'chrome'.
    :param options: str: Ruta al ejecutable del driver (opcional, usa valores predeterminados si no se especifica).
    :return: WebDriver: Devuelve una instancia del controlador configurado.
    """
    __instance = None
    __driver_type = None

    def __new__(cls, driver_type='chrome', options=None) -> WebDriver:
        
        driver_type = driver_type or 'chrome'
        
        if cls.__instance is None or cls.__driver_type != driver_type:
            cls._reset()  # Asegura que cualquier instancia previa sea cerrada.
            cls.__driver_type = driver_type
            cls.__instance = cls.__create_driver(driver_type, options)
        return cls.__instance

    @classmethod
    def __create_driver(cls, driver_type, options):
        """
        Método interno para inicializar el WebDriver basado en el tipo de navegador.
        """
        drivers = {
            'chrome': webdriver.Chrome,
            'firefox': webdriver.Firefox,
            'edge': webdriver.Edge,
            'safari': webdriver.Safari,
            'ie': webdriver.Ie,
        }

        if driver_type not in drivers:
            raise ValueError(f"Unsupported browser type: {driver_type}")

        # Si no se proporciona `options`, Selenium usará su configuración predeterminada.
        return drivers[driver_type](options=options) if options else drivers[driver_type]()

    @classmethod
    def _reset(cls):
        """
        Restablece el WebDriver eliminando la instancia singleton.
        """
        if cls.__instance:
            try:
                cls.__instance.quit()  # Cierra el WebDriver si está en ejecución.
            except Exception as e:
                print(f"Error al cerrar el WebDriver: {e}")
            finally:
                cls.__instance = None
                cls.__driver_type = None
