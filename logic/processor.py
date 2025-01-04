from datetime import datetime
from manager import DriverManager
from scraping import Scraper
from calendars import HorarioICSGenerator
from cleaned import Clenaed

class Processor:
    def __init__(self, user, password, start_date_str, end_date_str, temp_path, export_path):
        # URL y clases
        self.url = 'https://intranet.upc.edu.pe/loginintranet/loginupc.aspx'
        self.manager = DriverManager()
        self.scraper = Scraper(self.manager, self.url)
        self.ics_generator = HorarioICSGenerator()
        self.cleaned = Clenaed(temp_path)
        
        # Variables
        self.user = user
        self.password = password
        self.start_date = self.parse_date(start_date_str)
        self.end_date = self.parse_date(end_date_str)
        self.export_path = export_path
        self.cleaned_schedule = self.cleaned.getCleanedScheduleName()

    def parse_date(self, date_str):
        """Convierte una cadena de fecha en formato 'ddmmyyyy' a un objeto datetime."""
        try:
            return datetime.strptime(date_str, "%d%m%Y")
        except ValueError:
            raise ValueError(f"Fecha no válida: {date_str}")

    def fetch_schedule_data(self):
        """Obtiene los datos de la tabla de horarios desde el scraper."""
        try:
            self.scraper.login(self.user, self.password)

            return self.scraper.getData() 
        
        except Exception as e:
            print(f"Error al obtener los datos del horario: {e}")
            return None, None

    def save_and_clean_data(self, table_schedule, table_info):
        """Guarda y limpia los datos obtenidos."""
        try:
            self.cleaned.saveTables(table_schedule, table_info)
            self.cleaned.cleanInfo()
        except Exception as e:
            print(f"Error al guardar o limpiar los datos: {e}")

    def generate_ics(self):
        """Genera el archivo .ics con el horario limpio."""
        try:
            self.ics_generator.generar_calendario(
                self.cleaned_schedule, self.export_path, self.start_date, self.end_date
            )
            print(f"Calendario generado correctamente en {self.export_path}")
        except Exception as e:
            print(f"Error al generar el calendario: {e}")

    def process(self):
        """Realiza todo el flujo de trabajo."""
        table_schedule, table_info = self.fetch_schedule_data()
        
        if table_schedule and table_info:
            self.save_and_clean_data(table_schedule, table_info)
            self.generate_ics()
        else:
            print("No se pudo obtener la información del horario. El proceso ha fallado.")


def main():
    user = 'u202319239'
    password = 'Upc_202404@'
    start_date = "10112024"  # Fecha de inicio en formato 'ddmmyyyy'
    end_date = "10112024"  # Fecha de fin en formato 'ddmmyyyy'
    temp_path = './exports/temp'
    export_path = './exports/cleaned_schedule.ics'

        # Crear el procesador de horarios
    processor = Processor(user, password, start_date, end_date, temp_path ,export_path)
    processor.process()

if __name__ == "__main__":
    main()