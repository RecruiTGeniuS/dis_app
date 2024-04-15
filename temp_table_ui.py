# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'temp_table.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_tempWindow(object):
    def setupUi(self, tempWindow):
        if not tempWindow.objectName():
            tempWindow.setObjectName(u"tempWindow")
        tempWindow.resize(550, 405)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tempWindow.sizePolicy().hasHeightForWidth())
        tempWindow.setSizePolicy(sizePolicy)
        tempWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.centralwidget = QWidget(tempWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.closeButton = QPushButton(self.centralwidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(230, 330, 91, 31))
        self.closeButton.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid rgb(173,173,173);\n"
"background-color: rgb(225,225,225);")
        self.tempTable = QTableWidget(self.centralwidget)
        if (self.tempTable.columnCount() < 2):
            self.tempTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tempTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tempTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tempTable.setObjectName(u"tempTable")
        self.tempTable.setGeometry(QRect(0, 0, 550, 331))
        sizePolicy.setHeightForWidth(self.tempTable.sizePolicy().hasHeightForWidth())
        self.tempTable.setSizePolicy(sizePolicy)
        self.tempTable.setAutoFillBackground(True)
        self.tempTable.horizontalHeader().setStretchLastSection(True)
        tempWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(tempWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 550, 22))
        tempWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(tempWindow)
        self.statusbar.setObjectName(u"statusbar")
        tempWindow.setStatusBar(self.statusbar)

        self.retranslateUi(tempWindow)

        QMetaObject.connectSlotsByName(tempWindow)
    # setupUi

    def retranslateUi(self, tempWindow):
        tempWindow.setWindowTitle(QCoreApplication.translate("tempWindow", u"\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u0430\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u0430", None))
        self.closeButton.setText(QCoreApplication.translate("tempWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        ___qtablewidgetitem = self.tempTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("tempWindow", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem1 = self.tempTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("tempWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0430", None));
    # retranslateUi

