# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_delEmployeeWindow(object):
    def setupUi(self, delEmployeeWindow):
        if not delEmployeeWindow.objectName():
            delEmployeeWindow.setObjectName(u"delEmployeeWindow")
        delEmployeeWindow.resize(290, 147)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(delEmployeeWindow.sizePolicy().hasHeightForWidth())
        delEmployeeWindow.setSizePolicy(sizePolicy)
        delEmployeeWindow.setMouseTracking(False)
        delEmployeeWindow.setFocusPolicy(Qt.StrongFocus)
        self.centralwidget = QWidget(delEmployeeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(180, 10, 81, 31))
        self.deleteButton.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid rgb(173,173,173);\n"
"background-color: rgb(225,225,225);")
        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(180, 50, 81, 31))
        self.cancelButton.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid rgb(173,173,173);\n"
"background-color: rgb(225,225,225);")
        self.codeEmpolyee = QLineEdit(self.centralwidget)
        self.codeEmpolyee.setObjectName(u"codeEmpolyee")
        self.codeEmpolyee.setGeometry(QRect(40, 10, 121, 71))
        sizePolicy.setHeightForWidth(self.codeEmpolyee.sizePolicy().hasHeightForWidth())
        self.codeEmpolyee.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        self.codeEmpolyee.setFont(font)
        delEmployeeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(delEmployeeWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 290, 22))
        delEmployeeWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(delEmployeeWindow)
        self.statusbar.setObjectName(u"statusbar")
        delEmployeeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(delEmployeeWindow)

        QMetaObject.connectSlotsByName(delEmployeeWindow)
    # setupUi

    def retranslateUi(self, delEmployeeWindow):
        delEmployeeWindow.setWindowTitle(QCoreApplication.translate("delEmployeeWindow", u"MainWindow", None))
        self.deleteButton.setText(QCoreApplication.translate("delEmployeeWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.cancelButton.setText(QCoreApplication.translate("delEmployeeWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.codeEmpolyee.setText("")
        self.codeEmpolyee.setPlaceholderText(QCoreApplication.translate("delEmployeeWindow", u"\u041a\u043e\u0434 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430", None))
    # retranslateUi

