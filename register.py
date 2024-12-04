from dotenv import load_dotenv
import os

load_dotenv('credentials.env')

class Register:
    def __init__(self):
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('PASSWORD')

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password