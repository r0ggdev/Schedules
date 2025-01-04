from logic import Processor
from gui import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_start.clicked.connect(self.get(self.tbx_user))
        self.progressBar.setValue(20)

#        self.listView.

    def get(self, object):
        print(object.text())

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()