# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceV02iWlZHk.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTimeEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 600)
        MainWindow.setMinimumSize(QSize(780, 600))
        MainWindow.setMaximumSize(QSize(950, 670))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u"gui/source/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 0)
        self.titlebar = QFrame(self.centralwidget)
        self.titlebar.setObjectName(u"titlebar")
        self.titlebar.setMinimumSize(QSize(0, 35))
        self.titlebar.setMaximumSize(QSize(16777215, 35))
        self.titlebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.titlebar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titlebar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 4, 10, 5)
        self.icon = QLabel(self.titlebar)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(25, 25))
        self.icon.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.icon)

        self.spacer_left = QSpacerItem(256, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.spacer_left)

        self.title = QLabel(self.titlebar)
        self.title.setObjectName(u"title")

        self.horizontalLayout_2.addWidget(self.title)

        self.spacer_right = QSpacerItem(255, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.spacer_right)

        self.btn_fullscreen = QPushButton(self.titlebar)
        self.btn_fullscreen.setObjectName(u"btn_fullscreen")
        self.btn_fullscreen.setMinimumSize(QSize(26, 26))
        self.btn_fullscreen.setMaximumSize(QSize(26, 26))

        self.horizontalLayout_2.addWidget(self.btn_fullscreen)

        self.btn_close = QPushButton(self.titlebar)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(25, 25))
        self.btn_close.setMaximumSize(QSize(25, 25))
        self.btn_close.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.btn_close.setAutoDefault(False)
        self.btn_close.setFlat(False)

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.verticalLayout.addWidget(self.titlebar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_auto = QWidget()
        self.page_auto.setObjectName(u"page_auto")
        self.horizontalLayout_6 = QHBoxLayout(self.page_auto)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.form = QFrame(self.page_auto)
        self.form.setObjectName(u"form")
        self.form.setMinimumSize(QSize(350, 0))
        self.form.setMaximumSize(QSize(450, 16777215))
        self.form.setFrameShape(QFrame.Shape.StyledPanel)
        self.form.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_2 = QFormLayout(self.form)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lbl_user = QLabel(self.form)
        self.lbl_user.setObjectName(u"lbl_user")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbl_user)

        self.tbx_user = QLineEdit(self.form)
        self.tbx_user.setObjectName(u"tbx_user")
        self.tbx_user.setMinimumSize(QSize(0, 25))
        self.tbx_user.setMaximumSize(QSize(150, 16777215))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.tbx_user)

        self.lbl_pwd = QLabel(self.form)
        self.lbl_pwd.setObjectName(u"lbl_pwd")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lbl_pwd)

        self.tbx_pwd = QLineEdit(self.form)
        self.tbx_pwd.setObjectName(u"tbx_pwd")
        self.tbx_pwd.setMinimumSize(QSize(0, 25))
        self.tbx_pwd.setMaximumSize(QSize(150, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.tbx_pwd)

        self.btn_login = QPushButton(self.form)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(80, 35))
        self.btn_login.setMaximumSize(QSize(80, 35))

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.btn_login)

        self.box_dates = QGroupBox(self.form)
        self.box_dates.setObjectName(u"box_dates")
        self.box_dates.setMinimumSize(QSize(0, 120))
        self.box_dates.setMaximumSize(QSize(400, 150))
        self.box_dates.setFlat(False)
        self.box_dates.setCheckable(False)
        self.formLayout = QFormLayout(self.box_dates)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lbl_start = QLabel(self.box_dates)
        self.lbl_start.setObjectName(u"lbl_start")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_start)

        self.date_start = QDateEdit(self.box_dates)
        self.date_start.setObjectName(u"date_start")
        self.date_start.setMinimumSize(QSize(130, 30))
        self.date_start.setMaximumSize(QSize(130, 30))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.date_start)

        self.lbl_end = QLabel(self.box_dates)
        self.lbl_end.setObjectName(u"lbl_end")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_end)

        self.date_end = QDateEdit(self.box_dates)
        self.date_end.setObjectName(u"date_end")
        self.date_end.setMinimumSize(QSize(0, 30))
        self.date_end.setMaximumSize(QSize(130, 30))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.date_end)


        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.box_dates)

        self.progressBar = QProgressBar(self.form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(200, 40))
        self.progressBar.setMaximumSize(QSize(400, 40))
        self.progressBar.setValue(24)

        self.formLayout_2.setWidget(4, QFormLayout.SpanningRole, self.progressBar)

        self.btn_save = QPushButton(self.form)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(80, 35))
        self.btn_save.setMaximumSize(QSize(80, 35))

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.btn_save)

        self.box_console = QGroupBox(self.form)
        self.box_console.setObjectName(u"box_console")
        self.box_console.setMaximumSize(QSize(400, 16777215))
        self.horizontalLayout_7 = QHBoxLayout(self.box_console)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.obj_console = QPlainTextEdit(self.box_console)
        self.obj_console.setObjectName(u"obj_console")
        self.obj_console.setReadOnly(True)
        self.obj_console.setBackgroundVisible(False)
        self.obj_console.setCenterOnScroll(False)

        self.horizontalLayout_7.addWidget(self.obj_console)


        self.formLayout_2.setWidget(6, QFormLayout.SpanningRole, self.box_console)


        self.horizontalLayout_6.addWidget(self.form)

        self.courses = QFrame(self.page_auto)
        self.courses.setObjectName(u"courses")
        self.courses.setMinimumSize(QSize(400, 0))
        self.courses.setFrameShape(QFrame.Shape.StyledPanel)
        self.courses.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.courses)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.filter = QFrame(self.courses)
        self.filter.setObjectName(u"filter")
        self.filter.setMinimumSize(QSize(0, 40))
        self.filter.setMaximumSize(QSize(16777215, 40))
        self.filter.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.filter.setFrameShape(QFrame.Shape.StyledPanel)
        self.filter.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.filter)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.lbl_filterCode = QLabel(self.filter)
        self.lbl_filterCode.setObjectName(u"lbl_filterCode")
        self.lbl_filterCode.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_8.addWidget(self.lbl_filterCode)

        self.cbx_code = QComboBox(self.filter)
        self.cbx_code.setObjectName(u"cbx_code")
        self.cbx_code.setMinimumSize(QSize(120, 30))
        self.cbx_code.setMaximumSize(QSize(160, 30))

        self.horizontalLayout_8.addWidget(self.cbx_code)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.filter)

        self.info = QFrame(self.courses)
        self.info.setObjectName(u"info")
        self.info.setFrameShape(QFrame.Shape.StyledPanel)
        self.info.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.info)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tbx_section = QLineEdit(self.info)
        self.tbx_section.setObjectName(u"tbx_section")
        self.tbx_section.setMinimumSize(QSize(120, 25))
        self.tbx_section.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.tbx_section, 3, 1, 1, 1)

        self.lbl_section = QLabel(self.info)
        self.lbl_section.setObjectName(u"lbl_section")

        self.gridLayout.addWidget(self.lbl_section, 3, 0, 1, 1)

        self.tbx_code = QLineEdit(self.info)
        self.tbx_code.setObjectName(u"tbx_code")
        self.tbx_code.setMinimumSize(QSize(120, 25))
        self.tbx_code.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.tbx_code, 0, 1, 1, 1)

        self.box_day = QGroupBox(self.info)
        self.box_day.setObjectName(u"box_day")
        self.box_day.setMinimumSize(QSize(0, 150))
        self.box_day.setMaximumSize(QSize(16777215, 160))
        self.formLayout_3 = QFormLayout(self.box_day)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout_3.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout_3.setContentsMargins(-1, -1, -1, 9)
        self.lbl_day = QLabel(self.box_day)
        self.lbl_day.setObjectName(u"lbl_day")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lbl_day)

        self.cbx_day = QComboBox(self.box_day)
        self.cbx_day.setObjectName(u"cbx_day")
        self.cbx_day.setMinimumSize(QSize(0, 30))
        self.cbx_day.setMaximumSize(QSize(130, 30))

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.cbx_day)

        self.lbl_hourStart = QLabel(self.box_day)
        self.lbl_hourStart.setObjectName(u"lbl_hourStart")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.lbl_hourStart)

        self.time_start = QTimeEdit(self.box_day)
        self.time_start.setObjectName(u"time_start")
        self.time_start.setMinimumSize(QSize(0, 30))
        self.time_start.setMaximumSize(QSize(130, 30))

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.time_start)

        self.lbl_hourEnd = QLabel(self.box_day)
        self.lbl_hourEnd.setObjectName(u"lbl_hourEnd")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.lbl_hourEnd)

        self.time_end = QTimeEdit(self.box_day)
        self.time_end.setObjectName(u"time_end")
        self.time_end.setMinimumSize(QSize(0, 30))
        self.time_end.setMaximumSize(QSize(130, 30))

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.time_end)


        self.gridLayout.addWidget(self.box_day, 10, 0, 1, 6)

        self.tbx_lection = QLineEdit(self.info)
        self.tbx_lection.setObjectName(u"tbx_lection")
        self.tbx_lection.setMinimumSize(QSize(120, 25))
        self.tbx_lection.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.tbx_lection, 0, 5, 1, 1)

        self.tbx_group = QLineEdit(self.info)
        self.tbx_group.setObjectName(u"tbx_group")
        self.tbx_group.setMinimumSize(QSize(120, 25))
        self.tbx_group.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.tbx_group, 4, 1, 1, 1)

        self.lbl_group = QLabel(self.info)
        self.lbl_group.setObjectName(u"lbl_group")

        self.gridLayout.addWidget(self.lbl_group, 4, 0, 1, 1)

        self.lbl_lection = QLabel(self.info)
        self.lbl_lection.setObjectName(u"lbl_lection")

        self.gridLayout.addWidget(self.lbl_lection, 0, 4, 1, 1)

        self.separator = QFrame(self.info)
        self.separator.setObjectName(u"separator")
        self.separator.setMinimumSize(QSize(0, 20))
        self.separator.setFrameShape(QFrame.Shape.VLine)
        self.separator.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.separator, 0, 3, 1, 1)

        self.lbl_code = QLabel(self.info)
        self.lbl_code.setObjectName(u"lbl_code")

        self.gridLayout.addWidget(self.lbl_code, 0, 0, 1, 1)

        self.lbl_name = QLabel(self.info)
        self.lbl_name.setObjectName(u"lbl_name")

        self.gridLayout.addWidget(self.lbl_name, 2, 0, 1, 1)

        self.tbx_local = QLineEdit(self.info)
        self.tbx_local.setObjectName(u"tbx_local")
        self.tbx_local.setMinimumSize(QSize(120, 25))
        self.tbx_local.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.tbx_local, 3, 5, 1, 1)

        self.lbl_mode = QLabel(self.info)
        self.lbl_mode.setObjectName(u"lbl_mode")

        self.gridLayout.addWidget(self.lbl_mode, 4, 4, 1, 1)

        self.lbl_instructor = QLabel(self.info)
        self.lbl_instructor.setObjectName(u"lbl_instructor")

        self.gridLayout.addWidget(self.lbl_instructor, 2, 4, 1, 1)

        self.lbl_local = QLabel(self.info)
        self.lbl_local.setObjectName(u"lbl_local")

        self.gridLayout.addWidget(self.lbl_local, 3, 4, 1, 1)

        self.tbx_instructor = QLineEdit(self.info)
        self.tbx_instructor.setObjectName(u"tbx_instructor")
        self.tbx_instructor.setMinimumSize(QSize(120, 25))
        self.tbx_instructor.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.tbx_instructor, 2, 5, 1, 1)

        self.tbx_name = QLineEdit(self.info)
        self.tbx_name.setObjectName(u"tbx_name")
        self.tbx_name.setMinimumSize(QSize(120, 25))
        self.tbx_name.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.tbx_name, 2, 1, 1, 1)

        self.btn_refresh = QPushButton(self.info)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setMinimumSize(QSize(40, 40))
        self.btn_refresh.setMaximumSize(QSize(40, 40))
        self.btn_refresh.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout.addWidget(self.btn_refresh, 11, 5, 1, 1)

        self.cbx_mode = QComboBox(self.info)
        self.cbx_mode.addItem("")
        self.cbx_mode.addItem("")
        self.cbx_mode.setObjectName(u"cbx_mode")
        self.cbx_mode.setMinimumSize(QSize(120, 25))

        self.gridLayout.addWidget(self.cbx_mode, 4, 5, 1, 1)


        self.verticalLayout_2.addWidget(self.info)


        self.horizontalLayout_6.addWidget(self.courses)

        self.stackedWidget.addWidget(self.page_auto)
        self.page_manual = QWidget()
        self.page_manual.setObjectName(u"page_manual")
        self.stackedWidget.addWidget(self.page_manual)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.content)

        self.menubar = QFrame(self.centralwidget)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setMinimumSize(QSize(0, 50))
        self.menubar.setMaximumSize(QSize(16777215, 50))
        self.menubar.setFrameShape(QFrame.Shape.StyledPanel)
        self.menubar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.menubar)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.leftFrame = QFrame(self.menubar)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setMinimumSize(QSize(80, 0))
        self.leftFrame.setMaximumSize(QSize(80, 50))
        self.leftFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.leftFrame)

        self.spacer_left_2 = QSpacerItem(237, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.spacer_left_2)

        self.menuoptions = QFrame(self.menubar)
        self.menuoptions.setObjectName(u"menuoptions")
        self.menuoptions.setMinimumSize(QSize(90, 50))
        self.menuoptions.setMaximumSize(QSize(90, 50))
        self.menuoptions.setFrameShape(QFrame.Shape.StyledPanel)
        self.menuoptions.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.menuoptions)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.btn_auto = QPushButton(self.menuoptions)
        self.btn_auto.setObjectName(u"btn_auto")
        self.btn_auto.setMinimumSize(QSize(30, 30))
        self.btn_auto.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_auto)

        self.btn_manual = QPushButton(self.menuoptions)
        self.btn_manual.setObjectName(u"btn_manual")
        self.btn_manual.setMinimumSize(QSize(30, 30))
        self.btn_manual.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_manual)


        self.horizontalLayout_5.addWidget(self.menuoptions)

        self.spacer_right_2 = QSpacerItem(237, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.spacer_right_2)

        self.otherOptions = QFrame(self.menubar)
        self.otherOptions.setObjectName(u"otherOptions")
        self.otherOptions.setMinimumSize(QSize(80, 50))
        self.otherOptions.setMaximumSize(QSize(16777215, 50))
        self.otherOptions.setFrameShape(QFrame.Shape.StyledPanel)
        self.otherOptions.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.otherOptions)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_help = QPushButton(self.otherOptions)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setMinimumSize(QSize(30, 30))
        self.btn_help.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.btn_help)

        self.btn_themes = QPushButton(self.otherOptions)
        self.btn_themes.setObjectName(u"btn_themes")
        self.btn_themes.setMinimumSize(QSize(30, 30))
        self.btn_themes.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.btn_themes)


        self.horizontalLayout_5.addWidget(self.otherOptions)


        self.verticalLayout.addWidget(self.menubar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.btn_close.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.icon.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"Timetable Converter", None))
        self.btn_fullscreen.setText("")
        self.btn_close.setText("")
        self.lbl_user.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.lbl_pwd.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Obtener", None))
        self.box_dates.setTitle(QCoreApplication.translate("MainWindow", u"Fecha del ciclo", None))
        self.lbl_start.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.lbl_end.setText(QCoreApplication.translate("MainWindow", u"Fin", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.box_console.setTitle(QCoreApplication.translate("MainWindow", u"Mensajes", None))
        self.obj_console.setPlainText("")
        self.obj_console.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Consola de mensajes sobre el programa", None))
        self.lbl_filterCode.setText(QCoreApplication.translate("MainWindow", u"Codigo", None))
        self.lbl_section.setText(QCoreApplication.translate("MainWindow", u"Seccion", None))
        self.box_day.setTitle("")
        self.lbl_day.setText(QCoreApplication.translate("MainWindow", u"Dia", None))
        self.lbl_hourStart.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.lbl_hourEnd.setText(QCoreApplication.translate("MainWindow", u"Fin", None))
        self.lbl_group.setText(QCoreApplication.translate("MainWindow", u"Grupo", None))
        self.lbl_lection.setText(QCoreApplication.translate("MainWindow", u"Lecci\u00f3n", None))
        self.lbl_code.setText(QCoreApplication.translate("MainWindow", u"Codigo", None))
        self.lbl_name.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.lbl_mode.setText(QCoreApplication.translate("MainWindow", u"Modalidad", None))
        self.lbl_instructor.setText(QCoreApplication.translate("MainWindow", u"Instructor", None))
        self.lbl_local.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.btn_refresh.setText("")
        self.cbx_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"Presencial", None))
        self.cbx_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Virtual", None))

        self.btn_auto.setText("")
        self.btn_manual.setText("")
        self.btn_help.setText("")
        self.btn_themes.setText("")
    # retranslateUi

