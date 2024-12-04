import unittest
import os
from register import Register

class TestRegisterDirect(unittest.TestCase):
    def setUp(self):
        """Establece variables de entorno específicas para cada prueba."""
        os.environ['EMAIL'] = 'direct_test@example.com'
        os.environ['PASSWORD'] = 'directpassword123'

    def tearDown(self):
        """Limpia las variables de entorno después de cada prueba."""
        os.environ.pop('EMAIL', None)
        os.environ.pop('PASSWORD', None)

    def test_get_email(self):
        """Prueba que el método get_email devuelva el email correcto."""
        reg = Register()
        self.assertEqual(reg.get_email(), 'direct_test@example.com', "El email no coincide con el esperado.")

    def test_get_password(self):
        """Prueba que el método get_password devuelva la contraseña correcta."""
        reg = Register()
        self.assertEqual(reg.get_password(), 'directpassword123', "La contraseña no coincide con la esperada.")

    def test_missing_env_var(self):
        """Prueba que se maneje correctamente cuando falta una variable de entorno."""
        os.environ.pop('PASSWORD', None)
        reg = Register()
        self.assertIsNone(reg.get_password(), "La contraseña debería ser None si no está definida.")

if __name__ == "__main__":
    unittest.main()
