# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacermugPS.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGroupBox, QLabel,
    QLineEdit, QListView, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(527, 381)
        MainWindow.setMinimumSize(QSize(527, 381))
        MainWindow.setMaximumSize(QSize(527, 381))
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.UserAvailable))
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(260, 10, 251, 311))
        self.groupBox_dates = QGroupBox(self.centralwidget)
        self.groupBox_dates.setObjectName(u"groupBox_dates")
        self.groupBox_dates.setGeometry(QRect(20, 120, 221, 111))
        self.date_start = QDateEdit(self.groupBox_dates)
        self.date_start.setObjectName(u"date_start")
        self.date_start.setGeometry(QRect(60, 30, 116, 23))
        self.date_end = QDateEdit(self.groupBox_dates)
        self.date_end.setObjectName(u"date_end")
        self.date_end.setGeometry(QRect(60, 70, 116, 23))
        self.lbl_start_date = QLabel(self.groupBox_dates)
        self.lbl_start_date.setObjectName(u"lbl_start_date")
        self.lbl_start_date.setGeometry(QRect(20, 30, 31, 21))
        self.lbl_end_date = QLabel(self.groupBox_dates)
        self.lbl_end_date.setObjectName(u"lbl_end_date")
        self.lbl_end_date.setGeometry(QRect(20, 70, 31, 21))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 250, 211, 23))
        self.progressBar.setValue(24)
        self.tbx_user = QLineEdit(self.centralwidget)
        self.tbx_user.setObjectName(u"tbx_user")
        self.tbx_user.setGeometry(QRect(90, 40, 151, 21))
        self.tbx_pwd = QLineEdit(self.centralwidget)
        self.tbx_pwd.setObjectName(u"tbx_pwd")
        self.tbx_pwd.setGeometry(QRect(90, 80, 151, 21))
        self.lbl_user = QLabel(self.centralwidget)
        self.lbl_user.setObjectName(u"lbl_user")
        self.lbl_user.setGeometry(QRect(20, 40, 49, 16))
        self.lbl_pwd = QLabel(self.centralwidget)
        self.lbl_pwd.setObjectName(u"lbl_pwd")
        self.lbl_pwd.setGeometry(QRect(20, 80, 61, 16))
        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(70, 290, 75, 31))
        self.lbl_title = QLabel(self.centralwidget)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setGeometry(QRect(70, 10, 111, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 527, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Timetable Converter", None))
        self.groupBox_dates.setTitle(QCoreApplication.translate("MainWindow", u"Fechas del ciclo", None))
        self.lbl_start_date.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.lbl_end_date.setText(QCoreApplication.translate("MainWindow", u"Fin", None))
        self.lbl_user.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.lbl_pwd.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Empezar", None))
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"Timetable Converter", None))
    # retranslateUi

