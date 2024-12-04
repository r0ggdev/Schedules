import unittest
from selenium import webdriver
from manager import DriverManager

class TestBrowserCreation(unittest.TestCase):
    """Pruebas para verificar la creación y el comportamiento de diferentes WebDrivers."""
    
    @classmethod
    def setUpClass(cls):
        """Inicializa el WebDriver solo una vez para todas las pruebas."""
        DriverManager._reset()
        cls.driver = None

    @classmethod
    def tearDownClass(cls):
        """Cierra el WebDriver después de ejecutar todas las pruebas."""
        if cls.driver:
            cls.driver.quit()

    def setUp(self):
        """Restaura el estado del WebDriver para cada prueba."""
        if self.driver:
            self.driver.quit()  # Asegura que no quede una instancia previa.
        self.driver = None

    def _create_driver(self, driver_type=None):
        """Crea y devuelve un WebDriver específico según el tipo."""
        self.driver = DriverManager(driver_type=driver_type)

    def test_create_default(self):
        """Verifica la creación del WebDriver predeterminado (Chrome)."""
        self._create_driver()
        self.assertIsInstance(self.driver, webdriver.Chrome, "El controlador debe ser una instancia de Chrome WebDriver.")

    def test_create_chrome(self):
        """Verifica la creación de un WebDriver de Chrome explícito."""
        self._create_driver(driver_type='chrome')
        self.assertIsInstance(self.driver, webdriver.Chrome, "El controlador debe ser una instancia de Chrome WebDriver.")

    def test_create_firefox(self):
        """Verifica la creación de un WebDriver de Firefox."""
        self._create_driver(driver_type='firefox')
        self.assertIsInstance(self.driver, webdriver.Firefox, "El controlador debe ser una instancia de Firefox WebDriver.")

    def test_create_edge(self):
        """Verifica la creación de un WebDriver de Edge."""
        self._create_driver(driver_type='edge')
        self.assertIsInstance(self.driver, webdriver.Edge, "El controlador debe ser una instancia de Edge WebDriver.")

    def test_invalid_browser_type(self):
        """Verifica el comportamiento cuando se pasa un tipo de navegador inválido."""
        with self.assertRaises(ValueError, msg="El tipo de navegador proporcionado no es válido."):
            self._create_driver(driver_type='invalid_browser')


if __name__ == "__main__":
    unittest.main()
