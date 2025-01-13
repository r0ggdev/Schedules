from datetime import datetime
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

        self.chrome_options = ["--headless", "--disable-gpu", "--window-size=1920x1080"]
        self.__manager = DriverManager('chrome', self.chrome_options)
        self.scraper = Scraper(self.__manager, self.url)
        
        self.data_user = User()
        self.data_courses = None

    def __processCourses(data):
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

    def scrapeData(self):
        if self.scraper.login(self.user, self.password):
            print("Login exitoso")
            self.scraper.redirectSchedule()
            
            self.table_info, self.table_schedule = self.scraper.extractData()

            return True
        
    def processData(self):
        clean_schedule = Cleaned.clean_schedule(self.table_schedule)
        clean_user = Cleaned.cleanedInfo(self.table_info)

        self.data_user.loadUser(clean_user)
        self.data_courses = self.__processCourses(clean_schedule)
    
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