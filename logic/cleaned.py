import unicodedata
import os, json
class Cleaned:
    def __directoryExists(self, path):
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            
            print(f"Directorio '{path}' creado.")

    def __getRangeSchedule(self, horario):
        return horario[0][0]
    
    def __parseCourse(self, curso):
        """
        Parsear un string de curso en un diccionario estructurado.
        """
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

    def __normalizeText(self, text):
        """Normaliza el texto eliminando acentos y convirtiendo a minúsculas."""
        return ''.join(
            c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c)
        ).lower()
    
    def saveJson(self, data, path):
        self.__directoryExists(path)
        with open(path, 'w') as json_file:
            json.dump(data, json_file, ensure_ascii = False, indent = 4)

    def clean_schedule(self, horario):
        # Diccionario para almacenar los cursos organizados por código y día
        cursos_limpios = {}

        # Iterar sobre los días de la semana (1 a 7)
        for dia in range(1, 8):  # Los días están entre 1 y 7 en el JSON
            dia_str = horario[str(dia)][str(1)]  # Obtener el nombre del día (ej. "Lunes")
            dia_normalizado = self.__normalizeText(dia_str)  # Normalizar el nombre del día
            
            # Iterar sobre las horas (de la clave "2" a "18")
            for hora in range(2, 19):  # Las horas están en las claves "2" a "18"
                curso_info = horario[str(dia)].get(str(hora), "").strip()  # Obtener la información del curso

                if curso_info and curso_info != " ":  # Si hay un curso en esa hora
                    # Parsear el curso
                    curso = self.__parseCourse(curso_info)
                    
                    if curso:
                        # Extraer el código del curso
                        codigo = curso["codigo"]
                        
                        # Si el código no está en el diccionario, lo agregamos
                        if codigo not in cursos_limpios:
                            cursos_limpios[codigo] = {
                                "codigo": codigo,
                                "grupo": curso["grupo"],
                                "dias": {},
                                "seccion": curso["seccion"],
                                "local": curso["local"],
                                "modalidad": curso["modalidad"]
                            }

                        # Si el día normalizado no está en el diccionario, lo agregamos
                        if dia_normalizado not in cursos_limpios[codigo]["dias"]:
                            cursos_limpios[codigo]["dias"][dia_normalizado] = {
                                "salon": curso["salon"],
                                "hora_inicio": curso["hora_inicio"],
                                "hora_fin": curso["hora_fin"]
                            }
                        else:
                            # Si ya existe el día, solo actualizamos el horario
                            cursos_limpios[codigo]["dias"][dia_normalizado]["hora_inicio"] = curso["hora_inicio"]
                            cursos_limpios[codigo]["dias"][dia_normalizado]["hora_fin"] = curso["hora_fin"]

        return cursos_limpios
    
    def cleanedInfo(self, info):
        STUDENT = 2
        CAREER = 4
        SUBJECT = 7

        student_info = info["1"].get(str(STUDENT))

        if student_info:
            result = {
                'code': student_info.split(' - ')[0].replace(':', '').strip(),
                'lastName': student_info.split(' - ')[1].split(',')[0].strip(),
                'name': student_info.split(' - ')[1].split(',')[1].strip(),
                'career': info["1"].get(str(CAREER), '').replace(':', '').strip(),
                'site': info["1"].get(str(SUBJECT), '').split('CAMPUS')[1].strip()
            }
            
        else:
            result = {
                'code': None,
                'lastName': None,
                'name': None,
                'career': None,
                'site': None
            }

        return result
