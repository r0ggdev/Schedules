import unicodedata
from typing import Dict

class Day:

    def __init__(self, day, classroom, start, end):
        self.day = day
        self.classroom = classroom
        self.start = start
        self.end = end

    def getDay(self):
        return self.day
    
    def getClassroom(self):
        return self.classroom
    
    def getStart(self):
        return self.start
    
    def getEnd(self):
        return self.end


class Course :

    def __init__(self, code, name, section, group, lesson, instructor, local, mode):
        self.code = code
        self.name = name
        self.section = section
        self.group = group
        self.lesson = lesson
        self.instructor = instructor
        self.local = local
        self.mode = mode
        self.days: Dict[str, Day] = {}

    def __normalized_day(self, text):
        return ''.join(
            c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c)
        ).lower()
    
    def __valid_day(self, day):
        normalized_day = self.__normalized_day(day)
        valid_days = {"lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"}

        return normalized_day in valid_days


    def addDay(self, day, classroom, start, end):
        normalized_day = self.__normalized_day(day)
        if self.__valid_day(day):
            self.days[normalized_day] = Day(normalized_day, classroom, start, end)
        
        else:
            print(f"El día '{day}' no es válido")
    

    # Método getter para obtener los datos de un curso

    def getCode(self):
        return self.code
    
    def getName(self):
        return self.name
    
    def getSection(self):
        return self.section
    
    def getGroup(self):
        return self.group

    def getLesson(self):
        return self.lesson
    
    def getInstructor(self):
        return self.instructor
    
    def getLocal(self):
        return self.local
    
    def getMode(self):
        return self.mode
    
    def getDays(self):
        return {
            day: (day_obj.getClassroom(), day_obj.getStart(), day_obj.getEnd())
            for day, day_obj in self.days.items()
        }

    def getAvailableDays(self):
        return [day for day, day_obj in self.days.items() if day_obj is not None]


def main():
    # Creamos una instancia de la clase Course
    course = Course("INF103", "Programación I", "A", "1", "Teoría", "Gonzalo", "Sede", "Presencial")

    # Agregamos un días de clase
    course.addDay("Lúnes", "Aula 101", "08:00", "10:00")
    course.addDay("Miércoles", "Aula 103", "11:00", "13:00")
    course.addDay("Viernes", "Aula 106", "15:00", "17:00")

    
    # Mostramos los datos del curso
    print(f"Curso: {course.getName()}")
    print(f"Modalidad: {course.getMode()}")
    
    # Mostramos los datos de los dias de clase
    print(course.getDays())

    # Mostramos los días de clase disponibles
    print(course.getAvailableDays())
    
    # Filtramos los datos de un día de clase
    course_lunes = course.days["lunes"]

    print(f"Día:  {course_lunes.getDay()}" )
    print(f"Clase:  {course_lunes.getClassroom()}" )
    print(f"Incio:  {course_lunes.getStart()} - Fin: {course_lunes.getEnd()}" )


if __name__ == "__main__":
    main()
