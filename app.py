from logic import Processor
from gui import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.logic = Processor()
        self.tools = Tools()
        self.objs = self.tools.objs
        self.attempt = 0
        self.state = 0

        self.__setObject()
        self.__setIcons()
        self.__setStyles()
        self.__initilizationWindow()
        self.__connectButtons()
        self.__calendarPopup()

    # funcionamiento interno
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            if self.title_bar.geometry().contains(event.pos()):
                self.moving = True
                self.offset = event.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.moving:
            delta = event.pos() - self.offset
            self.move(self.pos() + delta)

    def mouseReleaseEvent(self, event):
        self.moving = False
    
    def closeEvent(self, event: QCloseEvent):
        self.logic.closeDriver()
        self.close()
        
    def __setObject(self):
        objects = {
            'btns':{
                'auto': self.btn_auto, # TODO: conectar [listo]
                'manual': self.btn_manual, # TODO: conectar [listo]
                'close': self.btn_close, # TODO: conectar [listo]
                'fullscreen': self.btn_fullscreen, # TODO: conectar [listo]
                'save': self.btn_save, # TODO: conectar [listo]
                'help': self.btn_help, # TODO: conectar [listo]
                'colormode': self.btn_themes, # TODO: conectar [listo]
                'get': self.btn_login, # TODO: conectar [listo] - #login
                'refresh': self.btn_refresh # TODO: conectar [listo] - #refresh
            },
            'pages':{
                'auto': self.page_auto, # TODO: conectar [listo]
                'manual': self.page_manual # TODO: conectar [listo]
            },
            'inputs':{
                'user': self.tbx_user, # TODO: conectar [listo]
                'pwd': self.tbx_pwd, # TODO: conectar [listo]
                'dateStart': self.date_start, # TODO: conectar [listo]
                'dateEnd': self.date_end, # TODO: conectar [listo]
                'cbxCode': self.cbx_code,
                
                'cbxDay': self.cbx_day,
                'timeEnd': self.time_end,
                'timeStart': self.time_start,

                'code': self.tbx_code,
                'name': self.tbx_name,
                'section': self.tbx_section,
                'group': self.tbx_group,
                'lection': self.tbx_lection,
                'instructor': self.tbx_instructor,
                'local': self.tbx_local,
                'mode': self.cbx_mode,
            },
            'outputs':{
                'console': self.obj_console, # TODO: conectar [listo]
                'progressbar': self.progressBar # TODO: conectar [listo]
            },
            'objects':{
                'titlebar': self.titlebar, # TODO: conectar [listo]
                'stacked': self.stackedWidget, 
                'icon': self.icon
            }
        }
        self.objs.setObjects(objects)

        dict = {
            'auto': {
                'button': self.objs.get('btns/auto'), 
                'page': self.objs.get('pages/auto'), 
                'selected': True
            },
            'manual': {
                'button': self.objs.get('btns/manual'), 
                'page': self.objs.get('pages/manual'), 
                'selected': False
            },
        }

        dates = {
            'start': self.objs.get('inputs/dateStart'),
            'end': self.objs.get('inputs/dateEnd')
        }

        console = self.objs.get('outputs/console')
        progressbar = self.objs.get('outputs/progressbar')

        # seteamos los objetos
        self.tools.setDict(dict)
        self.tools.setDates(dates)
        self.tools.setConosole(console)
        self.tools.setProgressBar(progressbar)

    def __initilizationWindow(self):
        # mover ventana
        self.title_bar = self.objs.get('objects/titlebar')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.moving = False
        self.offset = QPoint(0,0)

    def __setIcons(self):
        create = self.tools.create
        self.objs.get('objects/icon').setPixmap(create.pixmap("icons","titlebar/logo"))
        self.objs.get('objects/icon').setScaledContents(True)
        
        btns = self.objs.get('btns')
        btns.get('fullscreen').setIcon(create.ico("icons", "titlebar/fullscreen"))
        btns.get('close').setIcon(create.ico("icons", "titlebar/close"))
        btns.get('auto').setIcon(create.ico("icons", "pages/auto/icon"))
        btns.get('manual').setIcon(create.ico('icons', 'pages/manual/icon'))
        btns.get('help').setIcon(create.ico('icons', 'menubar/help'))
        btns.get('refresh').setIcon(create.ico('icons', 'pages/auto/filterSection/save'))

    def __setStyles(self):
        specific_styles = self.tools.specificStyle(['calendar', 'global'])
                
        objects = {  
            'button': self.objs.get('btns/colormode'),
            'default': 'dark',
            'windows': {
                'state': 0,
                'icon': self.tools.create.ico('icons', 'menubar/colormode/auto'),
            },    
            'themes': {
                'dark':{
                    'state': 1,
                    'icon': self.tools.create.ico('icons', 'menubar/colormode/dark'),
                    'style': self.tools.loadCSS('dark') + specific_styles
                },

                'light':{
                    'state': 2,
                    'icon': self.tools.create.ico('icons', 'menubar/colormode/light'),
                    'style':  self.tools.loadCSS('light') + specific_styles
                }
            }
        }

        self.tools.themes.set(objects)
        self.tools.themes.apply(self, 'windows')

    def __connectButtons(self):
        btns = self.objs.get('btns')

        btns['fullscreen'].clicked.connect(self.showMinimized)
        btns['close'].clicked.connect(self.closeEvent)
        btns['save'].clicked.connect(self.save)
        btns['help'].clicked.connect(self.help)
        btns['colormode'].clicked.connect(self.colorMode)
        btns['get'].clicked.connect(self.manualInfo)

        self.tools.toggle(self.objs.get('objects/stacked'))

    def __calendarPopup(self):
        today = QDate().currentDate()
        self.objs.get('inputs/dateEnd').setCalendarPopup(True)
        self.objs.get('inputs/dateStart').setCalendarPopup(True)
        self.objs.get('inputs/dateEnd').setDate(today)
        self.objs.get('inputs/dateStart').setDate(today)

    # funcionalidades
    def login(self):
        max_attempts = 3
        self.tools.setProgress(0)

        USER = self.objs.get('inputs/user').text()
        PASSWORD = self.objs.get('inputs/pwd').text()

        self.tools.setProgress(10)
        self.logic.setCredentials(USER, PASSWORD)    
        
        self.tools.setProgress(30)
        
        if self.attempt < max_attempts - 1:
            self.tools.setProgress(55)

            if self.logic.scrapeData():
                self.tools.setProgress(80)
                self.tools.console("Login exitoso.")

                if self.logic.processData():
                    self.tools.setProgress(100)
                    self.tools.console("Datos procesados exitosamente.")

                else:
                    self.tools.setProgress(0)
                    self.logic.closeDriver()
                    self.tools.console("Error al procesar los datos.")

            else:
                self.tools.setProgress(0)
                self.attempt += 1
                self.tools.console(f"Login fallido. Intento {self.attempt}/{max_attempts}.")
        
        else: 
            self.tools.console(f"Cerrando el programa.")
            self.logic.closeDriver()
            self.tools.setProgress(0)

    def save(self):
        self.tools.setProgress(0)

        try:
            self.tools.setProgress(30)
            path = self.tools.dialogFile(self)
            self.tools.setProgress(60)

            self.logic.generateICS(path, self.tools.getDate('start'), self.tools.getDate('end'))
            
            self.tools.setProgress(100)
            self.tools.console("Archivo guardado exitosamente.")
        
        except Exception as e:
            self.tools.setProgress(0)
            self.tools.console(f"Error al guardar el archivo ")

    def help(self):
        URL = 'https://github.com/r0ggdev/Schedules/tree/release/v0.1a'
        QDesktopServices.openUrl(QUrl(URL))

    def colorMode(self):
        theme = self.tools.themes
        theme.addState()

        if theme.state == theme.getState('windows'):
            theme.apply(self, 'windows')

        elif theme.state == theme.getState('dark'):
            theme.apply(self, 'dark')

        elif theme.state == theme.getState('light'):
            theme.apply(self, 'light')

# ! ADD

    def manualInfo(self): #! importante, funcion de prueba 
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
        self.logic.setTableSchedule(horario)
        self.logic.processData()
        # self.tools.console(str(self.logic.getCodes()))

        self.loadFilter()
        self.loadInformation()
    
    def indexMode(self, mode):
        if mode == 'Presencial':
            return 0
        else:
            return 1

    def loadInformation(self):
        codefilter = self.objs.get('inputs/cbxCode').currentText()
        info = lambda property: (self.logic.getCourse(codefilter).getCourse().get(property))

        self.objs.get('inputs/code').setText(info('code'))
        self.objs.get('inputs/name').setText(info('name'))
        self.objs.get('inputs/section').setText(info('section'))
        self.objs.get('inputs/group').setText(info('group'))
        self.objs.get('inputs/lection').setText(info('lection'))
        self.objs.get('inputs/instructor').setText(info('instructor'))
        self.objs.get('inputs/local').setText(info('local'))
        self.objs.get('inputs/mode').setCurrentIndex(self.indexMode(info('mode')))

    def loadDays(self, code = 'SI400'):
        days = list(self.logic.getCourse(code).getDays().keys())
        self.objs.get('inputs/cbxDay').addItems(days)


    def getCbx(self):
        return (self.cbx_code).currentText()
    
    def loadFilter(self):
        keys = list(self.logic.getCodes())
        self.objs.get('inputs/cbxCode').addItems(keys)
        


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()