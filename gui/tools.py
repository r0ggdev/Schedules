import json
import winreg
from typing import Literal, overload
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QFile, QTextStream

class Objects:
    def __init__(self):
        self.objects = {}
    
    def setObjects(self, objects:dict):
        self.objects = objects
    
    def get(self, path: str, default=None):
        keys = path.split('/')
        result = self.objects
        
        for key in keys:
            result = result.get(key, default)
            if result is default:
                break
        
        return result


class Create:
    __category = Literal["icons", "styles", "fonts"]
    __QiconMode = Literal["Normal", "Disabled", "Active", "Selected"]
    __QiconState = Literal["Off", "On"]

    def __init__(self):
        self.path = './gui/paths.json'

        with open(self.path , 'r') as file:
            self.config = json.load(file)
        
        self.methods = {
            "ico": self.ico,
            "pixmap":self.pixmap,
            "get": self.get
        }
    
    def setPath(self, path:str):
        self.path = path
        
    def get(self, category: __category, key:str):
        category_data = self.config.get(category)

        if category_data is None:
            raise Exception(f"Category '{category}' not found in the configuration.")

        key_parts = key.split("/") 

        current_data = category_data
        for part in key_parts:
            if isinstance(current_data, dict) and part in current_data:
                current_data = current_data[part]
            else:
                raise Exception(f"Key '{key}' not found under category '{category}'.")

        return current_data
    
    @overload
    def ico(self, category: __category, key: str)->QIcon:
        ...

    @overload
    def ico(self, category: __category, 
            key: str, size: QSize | tuple[float, float])->QIcon:
        ...

    @overload
    def ico(self, category: __category, 
            key: str, size: QSize | tuple[float, float], 
            mode: QIcon.Mode | __QiconMode)->QIcon:
        ...

    @overload
    def ico(self, category: __category, 
            key: str, size: QSize | tuple[float, float], 
            mode: QIcon.Mode | __QiconMode, 
            state: QIcon.State | __QiconState)->QIcon:
        ...

    def ico(self, category: __category = ..., 
            key: str = ..., 
            size: QSize | tuple[float, float] = QSize(),
            mode: QIcon.Mode | __QiconMode = QIcon.Mode.Normal, 
            state: QIcon.State | __QiconState = QIcon.State.Off) -> QIcon:
        
        if isinstance(size, tuple):
            size = QSize(*size)
        
        if not isinstance(mode, QIcon.Mode):
            mode = QIcon.Mode[mode]  

        if not isinstance(state, QIcon.State):
            state = QIcon.State[state]
        
        icon = QIcon()
        icon.addFile(self.get(category, key), size, mode, state)
        
        return icon


    def pixmap(self, category: __category = ..., key: str = ...) -> QPixmap:
        return QPixmap(self.get(category, key))

    def __getatrr__(self, method: str):
        if method in self.methods:
            return self.methods[method]
        else:
            raise Exception("Method not found.")

class Themes:
    def __init__(self):
        self.state = 0
        self.quantity_themes = 0
        self.themes = {}  
        self.button = None 
        self.default = None

    def __setObject(self, windows):
        """Asocia los objetos con los parámetros proporcionados"""
        self.themes = self.objects.get('themes', {})
        self.button = self.objects.get('button')
        self.default = self.objects.get('default')
        
        self.themes.update({'windows': windows})

    def set(self, parameters: dict):
        """Establece los parámetros del objeto y los temas"""
        self.objects = parameters
        self.__setObject(parameters.get('windows'))

        self.quantity_themes = len(self.themes)

    def windows(self):
        """Obtiene el tema actual de Windows"""
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")

            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            
            if value == 1:
                return "light"
            
            elif value == 0:
                return "dark"
            else:
                return "unknown"
        
        except Exception as e:
            return f"Error al obtener el tema: {str(e)}"

        
    def apply(self, obj, themeName: str):
        """Aplica el tema seleccionado a la ventana"""
        theme = self.themes.get(themeName)
        default = self.themes.get(self.default).get('style', None)

        if theme:  
            try:
                # Aplicar el icono al botón
                icon = theme.get('icon')
                if icon:
                    self.button.setIcon(icon)

                # Si el tema es automático o el de Windows, usa los estilos predeterminados
                if themeName == 'windows' or themeName == 'auto':
                    current_windows_theme = self.windows()
                    
                    if current_windows_theme != 'light' and current_windows_theme != 'dark':
                        obj.setStyleSheet(default)
                        print("tema de windows no encontrado")

                    else:
                        windows_theme = self.themes.get(current_windows_theme).get('style', default)
                        obj.setStyleSheet(windows_theme)
                
                else:
                    # Aplicar el tema específico
                    obj.setStyleSheet(theme.get('style', default))

            except Exception as e:
                print(f"Error al aplicar el tema: {themeName}, {str(e)}")
        else:
            print(f"El tema {themeName} no está definido en los temas.")
    
    def addState(self):
        """Cambia al siguiente estado de tema (por ejemplo, del modo oscuro al claro y viceversa)"""
        self.state = (self.state + 1) % self.quantity_themes
    
    def getState(self, theme: str):
        """Obtiene el estado del tema específico"""
        return self.themes.get(theme, {}).get('state', None)

class CBX:
    def __init__(self):
        object = None

    def index(self, obj):
        values = []
        for key in range(obj.count()):
            values.append((key, obj.itemText(key)))

        return values



class Tools:
    def __init__(self):
        self.create = Create()
        self.objs = Objects()
        self.themes = Themes()
        self.type = 'ics'
        self.params = ("Guardar Calendario", "calendar", "Archivos de Calendario (*.ics)")

        self.dict = {}

    # metodos setters    
    def setDict(self, dict:dict):
        self.dict = dict

    def setTypeFile(self, type:str):
        self.type = type
    
    def setParameters(self, parameters:tuple[str, str, str]):
        self.params = parameters
    
    def setDates(self, objs: dict):
        self.objdates = objs

    def setConosole(self, console):
        self.objconsole = console

    def setProgressBar(self, obj):
        self.objprogress = obj

    # funciones
    def console(self, message:str):
        self.objconsole.setPlainText(message)
        
    def toggle(self, stackedWidget):
        
        def __changePage(page):
            button = self.dict[page]['button']
            pag = self.dict[page]['page']

            if (not button.isChecked()) or (button.isChecked()):
                stackedWidget.setCurrentWidget(pag)
                button.setChecked(True)
                self.dict[page]['selected'] = True

                for btn in self.dict:
                    if btn != page:
                        self.dict[btn]['button'].setChecked(False)
                        self.dict[btn]['selected'] = False

        for page in self.dict:
            self.dict[page]['button'].setCheckable(True)
            self.dict[page]['button'].clicked.connect(lambda checked, page=page: __changePage(page))
        
        for page in self.dict:
            if self.dict[page]['selected']:
                self.dict[page]['button'].setChecked(True)


    def loadCSS(self, name:str):
        sheet = self.create.get("styles", name)
        file = QFile(sheet)

        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            css = stream.readAll()
            file.close()
            
            return css
        
        else:
            return ""
    
    def specificStyle(self, styles=None):
        if styles is None:
            styles = []

        specifics = ""

        for style in styles:
            try:
                specifics += self.loadCSS(style)
            except FileNotFoundError:
                print(f"El archivo CSS '{style}' no se encontró.")
            except Exception as e:
                print(f"Error al cargar el archivo CSS '{style}': {e}")

        return specifics

    def dialogFile(self, type):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            type, *self.params, options=options
        )
            
        if file_name:
            if not file_name.endswith(f".{self.type}"):
                file_name += f".{self.type}"
            
            self.console(f"Archivo guardado como: {file_name}")

        return file_name
    
    def getDate(self, key:str = None):
        start = self.objdates.get('start').date()
        end = self.objdates.get('end').date()

        dict = {
            'start': (start.day(), start.month(), start.year()),
            'end': (end.day(), end.month(), end.year())
        }

        if key is None:
            return dict
        else:
            return dict.get(key)
        
    def setProgress(self, value):
        self.objprogress.setValue(value)