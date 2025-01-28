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
                'auto': self.btn_automatic, # TODO: conectar [listo]
                'manual': self.btn_manual, # TODO: conectar [listo]
                'close': self.btn_close, # TODO: conectar [listo]
                'fullscreen': self.btn_closeFullscreen, # TODO: conectar [listo]
                'save': self.btn_save, # TODO: conectar [listo]
                'help': self.btn_help, # TODO: conectar [listo]
                'colormode': self.btn_colorMode, # TODO: conectar [listo]
                'get': self.btn_get # TODO: conectar [listo] - #login
            },
            'pages':{
                'auto': self.page_automatic, # TODO: conectar [listo]
                'manual': self.page_manualy # TODO: conectar [listo]
            },
            'inputs':{
                'user': self.tbx_user, # TODO: conectar [listo]
                'pwd': self.tbx_pwd, # TODO: conectar [listo]
                'dateStart': self.date_start, # TODO: conectar [listo]
                'dateEnd': self.date_end # TODO: conectar [listo]
            },
            'outputs':{
                'console': self.lb_console, # TODO: conectar [listo]
                'progressbar': self.progressBar # TODO: conectar [listo]
            },
            'objects':{
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
        self.title_bar = self.frame_titleBar
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.moving = False
        self.offset = QPoint(0,0)

    def __setIcons(self):
        create = self.tools.create
        self.objs.get('objects/icon').setPixmap(create.pixmap("icons","icon"))
        
        btns = self.objs.get('btns')
        btns.get('fullscreen').setIcon(create.ico("icons", "titlebar/fullscreen"))
        btns.get('close').setIcon(create.ico("icons", "titlebar/close"))
        btns.get('auto').setIcon(create.ico("icons", "pages/auto/icon"))
        btns.get('manual').setIcon(create.ico('icons', 'pages/manual/icon'))
        btns.get('help').setIcon(create.ico('icons', 'menubar/help'))

    def __setStyles(self):        
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
                    'style': self.tools.loadCSS('dark')
                },

                'light':{
                    'state': 2,
                    'icon': self.tools.create.ico('icons', 'menubar/colormode/light'),
                    'style':  self.tools.loadCSS('light')
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
        btns['get'].clicked.connect(self.login)

        self.tools.toggle(self.objs.get('objects/stacked'))

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
    
    def view(self):
        pass

    def colorMode(self):
        theme = self.tools.themes
        theme.addState()

        if theme.state == theme.getState('windows'):
            theme.apply(self, 'windows')

        elif theme.state == theme.getState('dark'):
            theme.apply(self, 'dark')

        elif theme.state == theme.getState('light'):
            theme.apply(self, 'light')

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()