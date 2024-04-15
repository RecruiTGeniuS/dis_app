# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(925, 585)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(248, 248, 248)\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.addEmployee = QPushButton(self.centralwidget)
        self.addEmployee.setObjectName(u"addEmployee")
        self.addEmployee.setGeometry(QRect(720, 170, 161, 51))
        icon = QIcon()
        icon.addFile(u":/C:/Users/04kir/Downloads/add_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addEmployee.setIcon(icon)
        self.employeeTable = QTableWidget(self.centralwidget)
        if (self.employeeTable.columnCount() < 8):
            self.employeeTable.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.employeeTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.employeeTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.employeeTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.employeeTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.employeeTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.employeeTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.employeeTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.employeeTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.employeeTable.setObjectName(u"employeeTable")
        self.employeeTable.setGeometry(QRect(10, 280, 901, 221))
        self.employeeTable.setStyleSheet(u"border: 1px solid rgb(173, 173, 173);\n"
"border-radius: 5px;")
        self.employeeTable.setFrameShape(QFrame.StyledPanel)
        self.employeeTable.setLineWidth(1)
        self.employeeTable.setMidLineWidth(0)
        self.employeeTable.setSortingEnabled(False)
        self.employeeTable.horizontalHeader().setVisible(True)
        self.employeeTable.horizontalHeader().setCascadingSectionResizes(False)
        self.employeeTable.horizontalHeader().setMinimumSectionSize(2)
        self.employeeTable.horizontalHeader().setDefaultSectionSize(105)
        self.employeeTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.employeeTable.horizontalHeader().setStretchLastSection(True)
        self.employeeTable.verticalHeader().setVisible(False)
        self.employeeTable.verticalHeader().setCascadingSectionResizes(False)
        self.employeeTable.verticalHeader().setMinimumSectionSize(10)
        self.employeeTable.verticalHeader().setDefaultSectionSize(20)
        self.rowLabel = QLabel(self.centralwidget)
        self.rowLabel.setObjectName(u"rowLabel")
        self.rowLabel.setGeometry(QRect(30, 90, 201, 61))
        self.rowLabel.setStyleSheet(u"font-weght: bold;\n"
"font-size: 20pt;\n"
"")
        self.rowNum = QLabel(self.centralwidget)
        self.rowNum.setObjectName(u"rowNum")
        self.rowNum.setGeometry(QRect(30, 150, 181, 31))
        self.rowNum.setStyleSheet(u"font-weght: bold;\n"
"font-size: 18pt;\n"
"")
        self.rowNum.setAlignment(Qt.AlignCenter)
        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(810, 40, 71, 31))
        icon1 = QIcon()
        icon1.addFile(u":/C:/Users/04kir/Downloads/power_settings_new_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitButton.setIcon(icon1)
        self.dismisLabel = QLabel(self.centralwidget)
        self.dismisLabel.setObjectName(u"dismisLabel")
        self.dismisLabel.setGeometry(QRect(340, 240, 241, 31))
        self.dismisLabel.setStyleSheet(u"font-weght: bold;\n"
"font-size: 15pt;\n"
"")
        self.dismisLabel.setAlignment(Qt.AlignCenter)
        self.updateEmployee = QPushButton(self.centralwidget)
        self.updateEmployee.setObjectName(u"updateEmployee")
        self.updateEmployee.setGeometry(QRect(20, 510, 82, 24))
        self.updateEmployee.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(72, 121, 185);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"	font: bold;\n"
"    border-color: rgb(0, 0, 0);\n"
"    min-width: 5em;\n"
"    padding: 1px;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/C:/Users/04kir/Downloads/restart_alt_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.updateEmployee.setIcon(icon2)
        self.deleteEmployee = QPushButton(self.centralwidget)
        self.deleteEmployee.setObjectName(u"deleteEmployee")
        self.deleteEmployee.setGeometry(QRect(110, 510, 91, 24))
        self.deleteEmployee.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(201, 101, 103);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"	font: bold;\n"
"    border-color: rgb(0, 0, 0);\n"
"    min-width: 5em;\n"
"    padding: 1px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/C:/Users/04kir/Downloads/close_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteEmployee.setIcon(icon3)
        self.makeTempTable = QPushButton(self.centralwidget)
        self.makeTempTable.setObjectName(u"makeTempTable")
        self.makeTempTable.setGeometry(QRect(720, 100, 161, 51))
        icon4 = QIcon()
        icon4.addFile(u":/C:/Users/04kir/Downloads/table_rows_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.makeTempTable.setIcon(icon4)
        self.summLabel = QLabel(self.centralwidget)
        self.summLabel.setObjectName(u"summLabel")
        self.summLabel.setGeometry(QRect(270, 90, 271, 61))
        self.summLabel.setStyleSheet(u"font-weght: bold;\n"
"font-size: 20pt;\n"
"")
        self.sumNum = QLabel(self.centralwidget)
        self.sumNum.setObjectName(u"sumNum")
        self.sumNum.setGeometry(QRect(260, 150, 281, 31))
        self.sumNum.setStyleSheet(u"font-weght: bold;\n"
"font-size: 18pt;\n"
"")
        self.sumNum.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 0, 531, 51))
        self.label.setStyleSheet(u"font: italic 26pt \"Segoe UI\";\n"
"font-weght: bold;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 925, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.addEmployee.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        ___qtablewidgetitem = self.employeeTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430", None));
        ___qtablewidgetitem1 = self.employeeTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None));
        ___qtablewidgetitem2 = self.employeeTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None));
        ___qtablewidgetitem3 = self.employeeTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem4 = self.employeeTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None));
        ___qtablewidgetitem5 = self.employeeTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None));
        ___qtablewidgetitem6 = self.employeeTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None));
        ___qtablewidgetitem7 = self.employeeTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u0451\u043c\u0430 \u043d\u0430 \u0440\u0430\u0431\u043e\u0442\u0443", None));
        self.rowLabel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        self.rowNum.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.dismisLabel.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u043e\u043b\u0435\u043d\u043d\u044b\u0435 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.updateEmployee.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.deleteEmployee.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; color:#777777;\">\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 \u0438\u0437 \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445 \u0443\u0432\u043e\u043b\u0435\u043d\u043d\u044b\u0445 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.deleteEmployee.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.makeTempTable.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.makeTempTable.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0432\u0440\u0435\u043c. \u0442\u0430\u0431.", None))
        self.summLabel.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 \u043a\u043e\u043c\u043f\u0435\u043d\u0441\u0430\u0446\u0438\u0439", None))
#if QT_CONFIG(tooltip)
        self.sumNum.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sumNum.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0451\u0442 \u0443\u0432\u043e\u043b\u044c\u043d\u0435\u043d\u0438\u0439 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432", None))
    # retranslateUi

