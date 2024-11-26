from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class DriverManager:
    '''
    Esta es una clase encargada de manejar el webDriver de Selenium usando el patron Singleton
    
    :param: **driver_type:** str: Tipo de driver *(navegador)* a utilizar (chrome, firefox, edge, safari, ie) por defecto es chrome
    :param: **driver_path:** str: Ruta donde se encuentra el driver (solo si es necesario)
    
    :return: WebDriver: Retorna el driver seleccionado
    '''

    __instance = None

    def __new__(cls, driver_type = 'chrome', driver_path = '') -> WebDriver:

        if cls.__instance is None:
            cls.__instance = cls.__browser(driver_type, driver_path)

        return cls.__instance
    
    @classmethod
    def __browser(cls, driver_type, driver_path):
        
        driver ={
            'chrome': webdriver.Chrome,
            'firefox': webdriver.Firefox,
            'edge': webdriver.Edge,
            'safari': webdriver.Safari,
            'ie': webdriver.Ie
            }
        
        if driver_type not in driver:
            raise ValueError(f"Unsupported browser type: {driver_type}")
        
        return driver[driver_type](driver_path)
