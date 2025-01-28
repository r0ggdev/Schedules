from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter, QDesktopServices,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget, QFileDialog, QMessageBox)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 500)
        MainWindow.setMinimumSize(QSize(650, 500))
        MainWindow.setMaximumSize(QSize(850, 650))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(650, 500))
        self.centralwidget.setMaximumSize(QSize(850, 650))
        self.centralwidget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_titleBar = QFrame(self.mainFrame)
        self.frame_titleBar.setObjectName(u"frame_titleBar")
        self.frame_titleBar.setMinimumSize(QSize(0, 35))
        self.frame_titleBar.setMaximumSize(QSize(16777215, 40))
        self.frame_titleBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_titleBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_titleBar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 5, 10, 5)
        self.icon = QLabel(self.frame_titleBar)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(25, 25))
        self.icon.setMaximumSize(QSize(25, 25))

        self.icon.setScaledContents(True)

        self.horizontalLayout.addWidget(self.icon)

        self.spacer_left = QSpacerItem(185, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.spacer_left)

        self.title = QLabel(self.frame_titleBar)
        self.title.setObjectName(u"title")
        self.title.setScaledContents(False)

        self.horizontalLayout.addWidget(self.title)

        self.spacer_right = QSpacerItem(184, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.spacer_right)

        self.btn_closeFullscreen = QPushButton(self.frame_titleBar)
        self.btn_closeFullscreen.setObjectName(u"btn_closeFullscreen")
        self.btn_closeFullscreen.setIconSize(QSize(10, 10))

        self.horizontalLayout.addWidget(self.btn_closeFullscreen)

        self.btn_close = QPushButton(self.frame_titleBar)
        self.btn_close.setObjectName(u"btn_close")


        self.btn_close.setIconSize(QSize(10, 10))

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout_2.addWidget(self.frame_titleBar)

        self.frame_content = QFrame(self.mainFrame)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_content)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_automatic = QWidget()
        self.page_automatic.setObjectName(u"page_automatic")
        self.horizontalLayout_6 = QHBoxLayout(self.page_automatic)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_form = QFrame(self.page_automatic)
        self.frame_form.setObjectName(u"frame_form")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_form.sizePolicy().hasHeightForWidth())
        self.frame_form.setSizePolicy(sizePolicy)
        self.frame_form.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_form.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.box_dates = QGroupBox(self.frame_form)
        self.box_dates.setObjectName(u"box_dates")
        self.box_dates.setMinimumSize(QSize(0, 80))
        self.box_dates.setMaximumSize(QSize(400, 100))
        self.box_dates.setFont(font)
        self.formLayout = QFormLayout(self.box_dates)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_start = QLabel(self.box_dates)
        self.lbl_start.setObjectName(u"lbl_start")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_start)

        self.lbl_end = QLabel(self.box_dates)
        self.lbl_end.setObjectName(u"lbl_end")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_end)

        self.date_start = QDateEdit(self.box_dates)
        self.date_start.setObjectName(u"date_start")
        self.date_start.setMinimumSize(QSize(0, 25))
        self.date_start.setMaximumSize(QSize(130, 16777215))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.date_start)

        self.date_end = QDateEdit(self.box_dates)
        self.date_end.setObjectName(u"date_end")
        self.date_end.setMinimumSize(QSize(0, 25))
        self.date_end.setMaximumSize(QSize(130, 16777215))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.date_end)


        self.gridLayout_2.addWidget(self.box_dates, 3, 0, 1, 2)

        self.tbx_pwd = QLineEdit(self.frame_form)
        self.tbx_pwd.setObjectName(u"tbx_pwd")
        self.tbx_pwd.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.tbx_pwd, 1, 1, 1, 1)

        self.btn_save = QPushButton(self.frame_form)
        self.btn_save.setObjectName(u"btn_save")

        self.gridLayout_2.addWidget(self.btn_save, 4, 0, 1, 1)

        self.tbx_user = QLineEdit(self.frame_form)
        self.tbx_user.setObjectName(u"tbx_user")
        self.tbx_user.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.tbx_user, 0, 1, 1, 1)

        self.progressBar = QProgressBar(self.frame_form)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setMaximumSize(QSize(150, 16777215))
        self.progressBar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.gridLayout_2.addWidget(self.progressBar, 4, 1, 1, 1)

        self.lbl_user = QLabel(self.frame_form)
        self.lbl_user.setObjectName(u"lbl_user")

        self.gridLayout_2.addWidget(self.lbl_user, 0, 0, 1, 1)

        self.lbl_pwd = QLabel(self.frame_form)
        self.lbl_pwd.setObjectName(u"lbl_pwd")

        self.gridLayout_2.addWidget(self.lbl_pwd, 1, 0, 1, 1)

        self.btn_get = QPushButton(self.frame_form)
        self.btn_get.setObjectName(u"btn_get")

        self.gridLayout_2.addWidget(self.btn_get, 2, 0, 1, 1)

        self.box_console = QGroupBox(self.frame_form)
        self.box_console.setObjectName(u"box_console")
        self.box_console.setMinimumSize(QSize(0, 60))
        self.box_console.setMaximumSize(QSize(400, 100))
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(8)
        self.box_console.setFont(font1)
        self.verticalLayout_4 = QVBoxLayout(self.box_console)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lb_console = QLabel(self.box_console)
        self.lb_console.setObjectName(u"lb_console")
        self.lb_console.setFont(font)

        self.verticalLayout_4.addWidget(self.lb_console)


        self.gridLayout_2.addWidget(self.box_console, 5, 0, 1, 2)


        self.horizontalLayout_6.addWidget(self.frame_form)

        self.frame_courses = QFrame(self.page_automatic)
        self.frame_courses.setObjectName(u"frame_courses")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_courses.sizePolicy().hasHeightForWidth())
        self.frame_courses.setSizePolicy(sizePolicy2)
        self.frame_courses.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_courses.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_courses)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_6.addWidget(self.frame_courses)

        self.stackedWidget.addWidget(self.page_automatic)
        self.page_manualy = QWidget()
        self.page_manualy.setObjectName(u"page_manualy")
        self.stackedWidget.addWidget(self.page_manualy)

        self.horizontalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame_content)

        self.frame_menuBar = QFrame(self.mainFrame)
        self.frame_menuBar.setObjectName(u"frame_menuBar")
        self.frame_menuBar.setMinimumSize(QSize(0, 40))
        self.frame_menuBar.setMaximumSize(QSize(16777215, 50))
        self.frame_menuBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menuBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_menuBar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameOptions = QFrame(self.frame_menuBar)
        self.frameOptions.setObjectName(u"frameOptions")
        self.frameOptions.setMinimumSize(QSize(60, 30))
        self.frameOptions.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameOptions.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frameOptions)

        self.spacer_left_2 = QSpacerItem(210, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.spacer_left_2)

        self.menuOptions = QFrame(self.frame_menuBar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuOptions.setMinimumSize(QSize(80, 30))
        self.menuOptions.setMaximumSize(QSize(100, 100))
        self.menuOptions.setFrameShape(QFrame.Shape.StyledPanel)
        self.menuOptions.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.menuOptions)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.btn_automatic = QPushButton(self.menuOptions)
        self.btn_automatic.setObjectName(u"btn_automatic")
        self.btn_automatic.setMinimumSize(QSize(30, 30))
        self.btn_automatic.setMaximumSize(QSize(30, 30))


        self.horizontalLayout_5.addWidget(self.btn_automatic)

        self.btn_manual = QPushButton(self.menuOptions)
        self.btn_manual.setObjectName(u"btn_manual")
        self.btn_manual.setMinimumSize(QSize(30, 30))
        self.btn_manual.setMaximumSize(QSize(30, 30))

        self.btn_manual.setIconSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.btn_manual)


        self.horizontalLayout_2.addWidget(self.menuOptions)

        self.spacer_right_2 = QSpacerItem(209, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.spacer_right_2)

        self.ohterOptions = QFrame(self.frame_menuBar)
        self.ohterOptions.setObjectName(u"ohterOptions")
        self.ohterOptions.setMinimumSize(QSize(60, 30))
        self.ohterOptions.setFrameShape(QFrame.Shape.StyledPanel)
        self.ohterOptions.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.ohterOptions)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_help = QPushButton(self.ohterOptions)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setMinimumSize(QSize(20, 20))
        self.btn_help.setMaximumSize(QSize(30, 30))


        self.horizontalLayout_3.addWidget(self.btn_help)

        self.btn_colorMode = QPushButton(self.ohterOptions)
        self.btn_colorMode.setObjectName(u"btn_colorMode")
        self.btn_colorMode.setMinimumSize(QSize(20, 20))
        self.btn_colorMode.setMaximumSize(QSize(30, 30))


        self.horizontalLayout_3.addWidget(self.btn_colorMode)


        self.horizontalLayout_2.addWidget(self.ohterOptions)


        self.verticalLayout_2.addWidget(self.frame_menuBar)


        self.verticalLayout.addWidget(self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Timetable Converter", None))
        self.icon.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"Timetable Converter", None))
        self.btn_closeFullscreen.setText("")
        self.btn_close.setText("")
        self.box_dates.setTitle(QCoreApplication.translate("MainWindow", u"Fecha del ciclo", None))
        self.lbl_start.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.lbl_end.setText(QCoreApplication.translate("MainWindow", u"Fin", None))
        self.tbx_pwd.setPlaceholderText("")
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.tbx_user.setPlaceholderText("")
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.lbl_user.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.lbl_pwd.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.btn_get.setText(QCoreApplication.translate("MainWindow", u"Obtener", None))
        self.box_console.setTitle(QCoreApplication.translate("MainWindow", u"Mensajes", None))
        self.lb_console.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_automatic.setText("")
        self.btn_manual.setText("")
        self.btn_help.setText("")
        self.btn_colorMode.setText("")
    # retranslateUi

