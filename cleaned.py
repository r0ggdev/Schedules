import pandas as pd
import json
import os
from collections import Counter
import unicodedata

def directory_exists(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        
        print(f"Directorio '{path}' creado.")

def saveTable(table, path):

    directory_exists(path)
    df = pd.DataFrame(table)
    df.to_json(path)
    print("Tabla guardada en " + path)

def save_json(data, path):
    directory_exists(path)

    with open(path, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    

def normalize_text(text):
    """Normaliza el texto eliminando acentos y convirtiendo a minúsculas."""
    return ''.join(
        c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c)
    ).lower()

# Limpiamos informacion

ALUMNO = 2
CARRERA = 4
MATERIA = 7

def clean_info(input_path, output_path):
    valor = pd.read_json(input_path)
    
    result = {
        'codigo': valor[1][ALUMNO].split(' - ')[0].replace(':', '').strip(),
        'apellido': valor[1][ALUMNO].split(' - ')[1].split(',')[0].strip(),
        'nombre': valor[1][ALUMNO].split(' - ')[1].split(',')[1].strip(),
        'carrera': valor[1][CARRERA].replace(':', '').strip(),
        'sede': valor[1][MATERIA].split('CAMPUS')[1].strip()
    }

    save_json(result, output_path)

def get_range_schedule(path):
    range = pd.read_json(path)
    
    return range[0][0]


def parse_course(curso):
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
    
def procesar_horario(file_path, output_file):
    """Carga un archivo de horario, identifica cursos repetidos y los guarda en un archivo JSON."""
    
    horario = pd.read_json(file_path)
    
    repetidos = {}

    for i in range(1, 7):
        cursos = horario[i]
        contador = Counter(cursos)
        dia_normalizado = normalize_text(horario[i][1])
        repetidos[dia_normalizado] = {
            str(idx): {**parse_course(curso), "cantidad": cantidad}
            for idx, (curso, cantidad) in enumerate(contador.items())
            if cantidad > 1 and curso.strip() != ""
            if parse_course(curso)  # Solo si se pudo procesar correctamente
        }
    
    save_json(repetidos, output_file)

    print(f"Archivo guardado en {output_file}")