import unittest
from selenium import webdriver
from manager import DriverManager  

_web = 'https://google.com'

class TestDriverManager(unittest.TestCase):

    def test_create_chrome(self):
        manager = DriverManager()
        self.assertIsInstance(manager, webdriver.Chrome, "El controlador debe ser una instancia de Chrome WebDriver.")
        manager.get(_web)

    def test_create_chrome_instance(self):
        manager = DriverManager(driver_type='chrome')
        self.assertIsInstance(manager, webdriver.Chrome, "El controlador debe ser una instancia de Chrome WebDriver.")
        manager.get(_web)


if __name__ == "__main__":
    unittest.main()