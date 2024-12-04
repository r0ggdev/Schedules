import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from manager import DriverManager

WEB_URL = 'https://www.selenium.dev/selenium/web/inputs.html'

class TestInteraction(unittest.TestCase):
    """Pruebas para interactuar con elementos en una página web utilizando Selenium."""

    @classmethod
    def setUpClass(cls):
        """Se ejecuta una vez antes de todas las pruebas para inicializar el WebDriver."""
        DriverManager._reset()
        cls.driver = DriverManager(driver_type='chrome')
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        """Se ejecuta una vez después de todas las pruebas para cerrar el WebDriver."""
        if cls.driver:
            cls.driver.quit()

    def setUp(self):
        """Restaura el estado inicial antes de cada prueba."""
        self.driver.get(WEB_URL)

    def test_navigate_to_url(self):
        """Verifica que el WebDriver navegue a una URL y que la página cargue correctamente."""
        self.assertEqual(self.driver.title, "inputs", "El título de la página no coincide.")

    def test_text_input_field(self):
        """Prueba para interactuar con un campo de texto en la página."""
        text_input = self.driver.find_element(By.NAME, 'no_type')
        text_input.clear()
        text_input.send_keys("Selenium Test")
        self.assertEqual(
            text_input.get_attribute('value'),
            "Selenium Test",
            "El valor del campo de texto no se ingresó correctamente."
        )

if __name__ == "__main__":
    unittest.main()
