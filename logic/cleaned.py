import pandas as pd
import json
import os
from collections import Counter
import unicodedata
class Clenaed:
    
    def __init__(self, directory = None , extension_file = '.json'):
        self.ALUMNO = 2
        self.CARRERA = 4
        self.MATERIA = 7

        self.original_timetable_name = 'timetable_original'
        self.original_info_name = 'info_original'
        
        self.cleaned_timetable_name = 'schedule_cleaned'
        self.cleaned_info_name = 'info_cleaned'
        
        self.directory = directory
        self.extension_file = extension_file
  
    def __getRangeSchedule(path):
        range = pd.read_json(path)
        return range[0][0]
      
    def __directoryExists(self, path):
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            
            print(f"Directorio '{path}' creado.")

    def __saveJson(self, data, path):
        self.__directoryExists(path)
        with open(path, 'w') as json_file:
            json.dump(data, json_file, ensure_ascii = False, indent = 4)
        
    def __normalizeText(self, text):
        """Normaliza el texto eliminando acentos y convirtiendo a minúsculas."""
        return ''.join(
            c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c)
        ).lower()
    
    def __parseCourse(self, curso):
        """Parsea un string de curso en un diccionario estructurado."""
        try:
            lines = curso.strip().split("\n")
            codigo, grupo = (lines[0].split(" - ") + [None])[:2]
            salon, seccion = (lines[1].split(" - ") + [None])[:2] if len(lines) > 1 else (None, None)
            local = next((line.split(":")[1].strip() for line in lines if line.startswith("Local:")), None)
            hora_inicio, hora_fin = (lines[-2].split(" - ") + [None])[:2] if len(lines) > 2 else (None, None)
            modalidad = lines[-1] if len(lines) > 3 else None

            return {
                "codigo": codigo,
                "grupo": grupo,
                "salon": salon,
                "seccion": seccion,
                "local": local,
                "hora_inicio": hora_inicio,
                "hora_fin": hora_fin,
                "modalidad": modalidad
            }
        except Exception as e:
            print(f"Error al procesar el curso: {curso}. Error: {e}")
            return None
        
    def setOrinalTimetableName(self, name):
        self.original_timetable_name = name

    def setOrinalInfoName(self, name):
        self.original_info_name = name

    def getCleanedScheduleName(self):
        return  self.directory + self.cleaned_timetable_name + self.extension_file
    
    def saveTables(self, tableschedule, tableinfo):
        path_schedule = self.directory + self.original_timetable_name + self.extension_file
        path_info = self.directory + self.original_info_name + self.extension_file

        self.__directoryExists(path_schedule)
        self.__directoryExists(path_info)

        df = pd.DataFrame(tableschedule)
        df.to_json(path_schedule)

        df2 = pd.DataFrame(tableinfo)
        df2.to_json(path_info)

        print("Tablas guardadas en " + self.directory)

    def cleanedInfoJson(self):
        input_path = self.directory + self.original_info_name + self.extension_file
        output_path = self.directory + self.cleaned_info_name + self.extension_file

        valor = pd.read_json(input_path)
        result = {
            'codigo': valor[1][self.ALUMNO].split(' - ')[0].replace(':', '').strip(),
            'apellido': valor[1][self.ALUMNO].split(' - ')[1].split(',')[0].strip(),
            'nombre': valor[1][self.ALUMNO].split(' - ')[1].split(',')[1].strip(),
            'carrera': valor[1][self.CARRERA].replace(':', '').strip(),
            'sede': valor[1][self.MATERIA].split('CAMPUS')[1].strip()
        }

        self.__saveJson(result, output_path)
    
    def cleanedScheduleJson(self):
        """Carga un archivo de horario, identifica cursos repetidos y los guarda en un archivo JSON."""
        input_path = self.directory + self.original_timetable_name + self.extension_file
        output_path = self.directory + self.cleaned_timetable_name + self.extension_file

        horario = pd.read_json(input_path)
        
        repetidos = {}

        for i in range(1, 7):
            cursos = horario[i]
            contador = Counter(cursos)
            dia_normalizado = self.__normalizeText(horario[i][1])
            repetidos[dia_normalizado] = {
                str(idx): {**self.__parseCourse(curso), "cantidad": cantidad}
                for idx, (curso, cantidad) in enumerate(contador.items())
                if cantidad > 1 and curso.strip() != ""
                if self.__parseCourse(curso)  # Solo si se pudo procesar correctamente
            }
        
        self.__saveJson(repetidos, output_path)

        print(f"Archivo guardado en {output_path}")

    def cleanInfo(self):
        self.cleanedScheduleJson()
        self.cleanedInfoJson()

