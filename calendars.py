import json
from datetime import datetime, timedelta

class HorarioICSGenerator:
    def __init__(self, timezone="America/Lima", calendar_name="Horario Clases"):
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

    def iniciar_calendario(self):
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

    def get_next_weekday(self, start_date, weekday):
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
            return start_date + timedelta(days=days_to_add)
        except Exception as e:
            print(f"Error al calcular el próximo día: {e}")
            return None

    def agregar_evento(self, dia, evento, fecha_inicio_repeticion, fecha_fin_repeticion):
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
            primer_dia = self.get_next_weekday(fecha_inicio_repeticion, weekday)

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

    def cerrar_calendario(self):
        """Cierra el contenido del archivo ICS."""
        self.ics_content += "END:VCALENDAR\n"

    def guardar_archivo(self, filepath):
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


# Ejemplo de uso
if __name__ == "__main__":
    generator = HorarioICSGenerator()
    generator.iniciar_calendario()

    try:
        with open('./exports/cleaned/horario.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        fecha_inicio_repeticion = datetime.strptime("20241110", "%Y%m%d")
        fecha_fin_repeticion = datetime.strptime("20241218", "%Y%m%d")

        for dia, eventos in data.items():
            if eventos:
                for _, evento in eventos.items():
                    generator.agregar_evento(dia, evento, fecha_inicio_repeticion, fecha_fin_repeticion)
            else:
                print(f"No hay eventos para {dia}.")

        generator.cerrar_calendario()
        generator.guardar_archivo("./exports/horario.ics")

    except Exception as e:
        print(f"Error al procesar los datos: {e}")
