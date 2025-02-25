from .manager import DriverManager
from .calendars import ICSGenerator
from .scraping import Scraper
from .cleaned import Cleaned
from .courses import Course
from .user import User

class Processor:
    def __init__(self):
        self.url = 'https://intranet.upc.edu.pe/loginintranet/loginupc.aspx'
        
        self.user = ''
        self.password = ''

        self.table_info = None
        self.table_schedule = None
        self.driver = None
        self.chrome_options = ["--headless", "--disable-gpu", "--window-size=1920x1080"]
        
        self.data_user = User()
        self.data_courses = None

    def __processCourses(self, data):
        courses = {}

        for course_code, course_info in data.items():
            # Crear un objeto de la clase Course
            course = Course(
                code = course_info.get('codigo', None),
                name = course_info.get('nombre', None),
                section = course_info.get('seccion', None),
                group = course_info.get('grupo', None),
                lesson = course_info.get('leccion', None),
                instructor = course_info.get('instructor', None),
                local = course_info.get('local', None),
                mode = course_info.get('modalidad', None)
            )

            for day, day_info in course_info['dias'].items():
                course.addDay(day, day_info['salon'], day_info['hora_inicio'], day_info['hora_fin'])
                courses[course_code] = course
            
        return courses

    def setCredentials(self, user, password):
        self.user = user
        self.password = password

    def createDriver(self):
        if self.driver is None:
            self.driver = DriverManager('chrome', self.chrome_options)

    def closeDriver(self):
        if self.driver:
            self.driver.quit()
        self.driver = None

    def scrapeData(self):
        self.createDriver()
        scraper = Scraper(self.driver, self.url)

        if scraper.login(self.user, self.password):
            scraper.redirectSchedule()

            self.table_info, self.table_schedule = scraper.extractData()
            if (self.table_info and self.table_schedule) or self.table_schedule:
                return True
            else:
                return False
            
        else:
            return False
        
    def processData(self):
        cleaned = Cleaned()
        try:
            clean_schedule = cleaned.clean_schedule(self.table_schedule)
            self.data_courses = self.__processCourses(clean_schedule)
        except:
            print("Error al limpiar el horario")
        
        try:
            clean_user = cleaned.cleanedInfo(self.table_info)
            self.data_user.loadUser(clean_user)
        except:
            print("Error al limpiar la información del usuario")

        # clean_user = cleaned.cleanedInfo(self.table_info)

    
    def generateICS(self, path, start_date, end_date):
        ics = ICSGenerator()
        ics.generate(self.data_courses, path, start_date, end_date)

    def getCodes(self):
        return self.data_courses.keys()
    
    def getCourse(self, code):
        if self.data_courses.get(code):
            return self.data_courses[code]
        else:
            return None
    
    def getDataUser(self):
        return self.data_user
    
    def setTableSchedule(self, table_schedule):
        self.table_schedule = table_schedule

    def setTableInfo(self, table_info):
        self.table_info = table_info
    

if __name__ == '__main__':
    horario = {
    "0": {
        "0": " HORARIO REGULAR SIN FECHA",
        "1": "Hora / D\u00eda",
        "2": "07:00 - 08:00",
        "3": "08:00 - 09:00",
        "4": "09:00 - 10:00",
        "5": "10:00 - 11:00",
        "6": "11:00 - 12:00",
        "7": "12:00 - 13:00",
        "8": "13:00 - 14:00",
        "9": "14:00 - 15:00",
        "10": "15:00 - 16:00",
        "11": "16:00 - 17:00",
        "12": "17:00 - 18:00",
        "13": "18:00 - 19:00",
        "14": "19:00 - 20:00",
        "15": "20:00 - 21:00",
        "16": "21:00 - 22:00",
        "17": "22:00 - 23:00",
        "18": "23:00 - 24:00"
    },
    "1": {
        "0": "null",
        "1": "Lunes",
        "2": "SI400 - 00\nUH-45 - SI35\nLocal: MO\n07:00 - 09:00\nPresencial",
        "3": "SI400 - 00\nUH-45 - SI35\nLocal: MO\n07:00 - 09:00\nPresencial",
        "4": " ",
        "5": " ",
        "6": "MA263 - 00\nUE-48 - SW51\nLocal: MO\n11:00 - 13:00\nPresencial",
        "7": "MA263 - 00\nUE-48 - SW51\nLocal: MO\n11:00 - 13:00\nPresencial",
        "8": " ",
        "9": " ",
        "10": " ",
        "11": " ",
        "12": " ",
        "13": " ",
        "14": " ",
        "15": " ",
        "16": " ",
        "17": " ",
        "18": " "
    },
    "2": {
        "0": "null",
        "1": "Martes",
        "2": " ",
        "3": " ",
        "4": " ",
        "5": " ",
        "6": " ",
        "7": " ",
        "8": " ",
        "9": " ",
        "10": " ",
        "11": " ",
        "12": " ",
        "13": " ",
        "14": " ",
        "15": " ",
        "16": " ",
        "17": " ",
        "18": " "
    },
    "3": {
        "0": "null",
        "1": "Mi\u00e9rcoles",
        "2": "SI725 - 00\nUD-57 - CC48\nLocal: MO\n07:00 - 09:00\nPresencial",
        "3": "SI725 - 00\nUD-57 - CC48\nLocal: MO\n07:00 - 09:00\nPresencial",
        "4": " ",
        "5": " ",
        "6": " ",
        "7": " ",
        "8": " ",
        "9": " ",
        "10": "MA475 - 00\nCC45\n15:00 - 17:00\nA distancia",
        "11": "MA475 - 00\nCC45\n15:00 - 17:00\nA distancia",
        "12": " ",
        "13": " ",
        "14": " ",
        "15": " ",
        "16": " ",
        "17": " ",
        "18": " "
    },
    "4": {
        "0": "null",
        "1": "Jueves",
        "2": "SI400 - 00\nUC-44 - SI35\nLocal: MO\n07:00 - 09:00\nPresencial",
        "3": "SI400 - 00\nUC-44 - SI35\nLocal: MO\n07:00 - 09:00\nPresencial",
        "4": "SI385 - 00\nUH-45 - SI49\nLocal: MO\n09:00 - 11:00\nPresencial",
        "5": "SI385 - 00\nUH-45 - SI49\nLocal: MO\n09:00 - 11:00\nPresencial",
        "6": "MA263 - 00\nUB-45 - SW51\nLocal: MO\n11:00 - 13:00\nPresencial",
        "7": "MA263 - 00\nUB-45 - SW51\nLocal: MO\n11:00 - 13:00\nPresencial",
        "8": "SI725 - 00\nUH-56 - CC48\nLocal: MO\n13:00 - 15:00\nPresencial",
        "9": "SI725 - 00\nUH-56 - CC48\nLocal: MO\n13:00 - 15:00\nPresencial",
        "10": " ",
        "11": " ",
        "12": " ",
        "13": " ",
        "14": " ",
        "15": " ",
        "16": " ",
        "17": " ",
        "18": " "
    },
    "5": {
        "0": "null",
        "1": "Viernes",
        "2": " ",
        "3": " ",
        "4": " ",
        "5": " ",
        "6": " ",
        "7": " ",
        "8": " ",
        "9": " ",
        "10": " ",
        "11": " ",
        "12": " ",
        "13": " ",
        "14": " ",
        "15": " ",
        "16": " ",
        "17": " ",
        "18": " "
    },
    "6": {
        "0": "null",
        "1": "S\u00e1bado",
        "2": "CC184 - 00\nUH-41 - CC42\nLocal: MO\n07:00 - 11:00\nPresencial",
        "3": "CC184 - 00\nUH-41 - CC42\nLocal: MO\n07:00 - 11:00\nPresencial",
        "4": "CC184 - 00\nUH-41 - CC42\nLocal: MO\n07:00 - 11:00\nPresencial",
        "5": "CC184 - 00\nUH-41 - CC42\nLocal: MO\n07:00 - 11:00\nPresencial",
        "6": " ",
        "7": " ",
        "8": " ",
        "9": " ",
        "10": " ",
        "11": " ",
        "12": " ",
        "13": " ",
        "14": " ",
        "15": " ",
        "16": " ",
        "17": " ",
        "18": " "
    },
    "7": {
        "0": "null",
        "1": "Domingo",
        "2": " ",
        "3": " ",
        "4": " ",
        "5": " ",
        "6": " ",
        "7": " ",
        "8": " ",
        "9": " ",
        "10": " ",
        "11": " ",
        "12": " ",
        "13": " ",
        "14": " ",
        "15": " ",
        "16": " ",
        "17": " ",
        "18": " "
    }
    }

    data = {
        "0":{
            "0":"Horario de clases del ciclo\nUtiliza esta opci\u00f3n para conocer tus horarios de clases del ciclo.","1":"Horario de clases del ciclo\nUtiliza esta opci\u00f3n para conocer tus horarios de clases del ciclo.","2":"Alumno","3":"REGULAR","4":"Estudio","5":" ","6":"  Sede Color\nMO - CAMPUS MONTERRICO","7":" ","8":"Sede","9":"MO - CAMPUS MONTERRICO","10":"","11":""
        },
        
        "1":{
            "0":"Horario de clases del ciclo\nUtiliza esta opci\u00f3n para conocer tus horarios de clases del ciclo.","1":"null","2":": 202319239 - Miranda Ayasta, Rogger Faryd","3":"null","4":": Ingenier\u00eda de Software","5":"null","6":" ","7":"Sede Color\nMO - CAMPUS MONTERRICO","8":"Color","9":"","10":"null","11":"null"
        },
        
        "2":{
            "0":"null","1":"null","2":"  M\u00f3dulo:","3":"null","4":"null","5":"null","6":"Sede Color\nMO - CAMPUS MONTERRICO","7":"Sede","8":"null","9":"","10":"null","11":"null"
        },
        "3":{
            "0":"null","1":"null","2":"REGULAR","3":"null","4":"null","5":"null","6":"Sede","7":"Color","8":"null","9":"null","10":"null","11":"null"
        },
        
        "4":{
            "0":"null","1":"null","2":"REGULAR","3":"null","4":"null","5":"null","6":"Color","7":"MO - CAMPUS MONTERRICO","8":"null","9":"null","10":"null","11":"null"
        },
        
        "5":{
            "0":"null","1":"null","2":"null","3":"null","4":"null","5":"null","6":"MO - CAMPUS MONTERRICO","7":"","8":"null","9":"null","10":"null","11":"null"
        },

        "6":{
            "0":"null","1":"null","2":"null","3":"null","4":"null","5":"null","6":"","7":"","8":"null","9":"null","10":"null","11":"null"
        },

        "7":{
            "0":"null","1":"null","2":"null","3":"null","4":"null","5":"null","6":"","7":"null","8":"null","9":"null","10":"null","11":"null"
        }
    }
    
    processor = Processor()
    processor.scrapeData()

    #processor.setTableSchedule(horario)
    #processor.setTableInfo(data)

    #processor.processData()

    #processor.generateICS('./export.ics',(12,1,2025),(12,3,2025))
