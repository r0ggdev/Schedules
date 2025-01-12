import json
from datetime import datetime, timedelta

class ICSGenerator:
    def __init__(self, timezone = "America/Lima", calendar_name = "Horario Clases"):
        self.timezone = timezone
        self.calendar_name = calendar_name
        self.dias_semana = {
            'lunes': 'MO',
            'martes': 'TU',
            'miercoles': 'WE',
            'jueves': 'TH',
            'viernes': 'FR',
            'sabado': 'SA',
            'domingo': 'SU'
        }
        self.ics_content = ""

    def startCalendar(self):
        """Inicializa el contenido del archivo ICS."""
        self.ics_content = (
            "BEGIN:VCALENDAR\n"
            "VERSION:2.0\n"
            "CALSCALE:GREGORIAN\n"
            f"METHOD:PUBLISH\nX-WR-CALNAME:{self.calendar_name}\n"
            f"X-WR-TIMEZONE:{self.timezone}\n"
            "BEGIN:VTIMEZONE\n"
            f"TZID:{self.timezone}\n"
            f"X-LIC-LOCATION:{self.timezone}\n"
            "BEGIN:STANDARD\n"
            "TZOFFSETFROM:-0500\n"
            "TZOFFSETTO:-0500\n"
            "TZNAME:GMT-5\n"
            "DTSTART:19700101T000000\n"
            "END:STANDARD\n"
            "END:VTIMEZONE\n"
        )

    def findNextWeekday(self, start_date, weekday):
        """
        Calcula el próximo día de la semana después de una fecha dada.

        Args:
            start_date (datetime): Fecha de inicio.
            weekday (int): Día de la semana (0=Monday, ..., 6=Sunday).

        Returns:
            datetime: Próxima fecha que corresponde al día de la semana.
        """
        try:
            days_to_add = (weekday - start_date.weekday()) % 7
            if days_to_add == 0:  # Si ya es el día actual, avanza a la próxima semana
                days_to_add = 7
            return start_date + timedelta(days=days_to_add)
        except Exception as e:
            print(f"Error al calcular el próximo día: {e}")
            return None

    def addEvent(self, dia, evento, fecha_inicio_repeticion, fecha_fin_repeticion):
        """
        Agrega un evento al calendario en formato ICS.

        Args:
            dia (str): Día de la semana del evento.
            evento (dict): Información del evento.
            fecha_inicio_repeticion (datetime): Fecha de inicio de la repetición.
            fecha_fin_repeticion (datetime): Fecha de fin de la repetición.
        """
        try:
            abreviatura_dia = self.dias_semana.get(dia.lower())
            if not abreviatura_dia:
                raise ValueError(f"Día no válido: {dia}")

            weekday = list(self.dias_semana.values()).index(abreviatura_dia)
            primer_dia = self.findNextWeekday(fecha_inicio_repeticion, weekday)

            if 'hora_inicio' not in evento or 'hora_fin' not in evento:
                raise ValueError("El evento debe contener 'hora_inicio' y 'hora_fin'.")

            start_time = primer_dia.strftime("%Y%m%d") + f"T{evento['hora_inicio'].replace(':', '')}00"
            end_time = primer_dia.strftime("%Y%m%d") + f"T{evento['hora_fin'].replace(':', '')}00"
            until_date = f"{fecha_fin_repeticion.strftime('%Y%m%d')}T045959Z"

            summary = evento.get('codigo', 'Sin Código')
            if "nombre" in evento:
                summary += f" - {evento['nombre']}"

            description = (
                f"<strong>Grupo:</strong> {evento.get('grupo', 'N/A')}<br>"
                f"<strong>Sección:</strong> {evento.get('seccion', 'N/A')}<br>"
                f"<strong>Local:</strong> {evento.get('local', 'N/A')}<br>"
                f"<strong>Modalidad:</strong> {evento.get('modalidad', 'N/A')}<br>"
                f"<strong>Salón:</strong> {evento.get('salon', 'N/A')}<br>"
                f"<strong>Horario:</strong> {evento.get('hora_inicio', 'N/A')} - {evento.get('hora_fin', 'N/A')}"
            )

            self.ics_content += (
                "BEGIN:VEVENT\n"
                f"DTSTART;TZID={self.timezone}:{start_time}\n"
                f"DTEND;TZID={self.timezone}:{end_time}\n"
                f"RRULE:FREQ=WEEKLY;WKST=MO;UNTIL={until_date};BYDAY={abreviatura_dia}\n"
                f"DTSTAMP:{datetime.now().strftime('%Y%m%dT%H%M%SZ')}\n"
                f"UID:{evento.get('codigo', '') + evento.get('salon', '')}@generated.calendar\n"
                "CREATED:19000101T120000Z\n"
                f"DESCRIPTION:{description}\n"
                f"LOCATION:{evento.get('salon', 'N/A')}\n"
                "SEQUENCE:0\n"
                "STATUS:CONFIRMED\n"
                f"SUMMARY:{summary}\n"
                "TRANSP:OPAQUE\n"
                "END:VEVENT\n"
            )
        except Exception as e:
            print(f"Error al agregar el evento: {e}")

    def closeCalendar(self):
        """Cierra el contenido del archivo ICS."""
        self.ics_content += "END:VCALENDAR\n"

    def saveICS(self, filepath):
        """
        Guarda el contenido del calendario en un archivo.

        Args:
            filepath (str): Ruta del archivo.
        """
        try:
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(self.ics_content)
            print(f"Archivo ICS guardado en {filepath}")
        except Exception as e:
            print(f"Error al guardar el archivo ICS: {e}")

    def generate(self, courses, export_path, start_date = ('dd','mm','YYYY'), end_date = ('dd','mm','YYYY')):
        
        date ={
            'start': datetime(start_date[2], start_date[1], start_date[0]),
            'end': datetime(end_date[2], end_date[1], end_date[0])
        }

        self.startCalendar()

        for course_code, course in courses.items():
            course_days = course.getDays()

            for day, details in course_days.items():
                evento = {
                    'codigo': course.getCode(),
                    'nombre': course.getName(),
                    'grupo': course.getGroup(),
                    'seccion': course.getSection(),
                    'local': course.getLocal(),
                    'modalidad': course.getMode(),
                    'salon': details['salon'],
                    'hora_inicio': details['hora_inicio'],
                    'hora_fin': details['hora_fin']
                }

                self.addEvent(day, evento, date['start'], date['end'])

        self.closeCalendar()
        self.saveICS(export_path)


# Ejemplo de uso:
if __name__ == "__main__":
    generator = ICSGenerator()
    ruta_salida = "./exports/horario.ics"
    
    courses ={ 
        'SI400': {
            'codigo': 'SI400', 
            'grupo': '00', 
            'dias': {
                'lunes': {'salon': 'UH-45', 'hora_inicio': '07:00', 'hora_fin': '09:00'}, 
                'jueves': {'salon': 'UC-44', 'hora_inicio': '07:00', 'hora_fin': '09:00'}
            }, 
            'seccion': 'SI35', 
            'local': 'MO', 
            'modalidad': 'Presencial'
        }, 
        
        'MA263': {
            'codigo': 'MA263', 
            'grupo': '00', 
            'dias': {
                'lunes': {'salon': 'UE-48', 'hora_inicio': '11:00', 'hora_fin': '13:00'}, 
                'jueves': {'salon': 'UB-45', 'hora_inicio': '11:00', 'hora_fin': '13:00'}
            }, 
            'seccion': 'SW51', 
            'local': 'MO', 
            'modalidad': 'Presencial'
        }, 
        
        'SI725': {
            'codigo': 'SI725', 
            'grupo': '00', 
            'dias': {
                'miercoles': {'salon': 'UD-57', 'hora_inicio': '07:00', 'hora_fin': '09:00'}, 
                'jueves': {'salon': 'UH-56', 'hora_inicio': '13:00', 'hora_fin': '15:00'}
            }, 
            'seccion': 'CC48', 
            'local': 'MO', 
            'modalidad': 'Presencial'
        }, 
        
        'MA475': {
            'codigo': 'MA475', 
            'grupo': '00', 
            'dias': {
                'miercoles': {'salon': 'CC45', 'hora_inicio': '15:00', 'hora_fin': '17:00'}
            }, 
            'seccion': None, 
            'local': None, 
            'modalidad': 'A distancia'
        }, 
        
        'SI385': {
            'codigo': 'SI385', 
            'grupo': '00', 
            'dias': {
                'jueves': {'salon': 'UH-45', 'hora_inicio': '09:00', 'hora_fin': '11:00'}
            },
            'seccion': 'SI49', 
            'local': 'MO', 
            'modalidad': 'Presencial'
        }, 
        
        'CC184': {
            'codigo': 'CC184', 
            'grupo': '00', 
            'dias': {
                'sabado': {'salon': 'UH-41', 'hora_inicio': '07:00', 'hora_fin': '11:00'}
            }, 
            'seccion': 'CC42', 
            'local': 'MO', 
            'modalidad': 'Presencial'
        }
    }

    generator.generate(courses, ruta_salida, (10,11,2024), (10,14,2024))