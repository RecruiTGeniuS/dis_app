# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_addWindow(object):
    def setupUi(self, addWindow):
        if not addWindow.objectName():
            addWindow.setObjectName(u"addWindow")
        addWindow.resize(925, 585)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addWindow.sizePolicy().hasHeightForWidth())
        addWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(addWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(110, 480, 311, 31))
        self.cancelButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255,255,255);\n"
"    border-radius: 10px ;\n"
"	border: 3px solid rgb(72, 121, 185);\n"
"	font: bold;\n"
"}\n"
"")
        self.surnameEdit = QLineEdit(self.centralwidget)
        self.surnameEdit.setObjectName(u"surnameEdit")
        self.surnameEdit.setGeometry(QRect(220, 140, 171, 22))
        self.nameEdit = QLineEdit(self.centralwidget)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setGeometry(QRect(220, 170, 171, 22))
        self.patronymicEdit = QLineEdit(self.centralwidget)
        self.patronymicEdit.setObjectName(u"patronymicEdit")
        self.patronymicEdit.setGeometry(QRect(220, 200, 171, 22))
        self.codeEmployeeEdit = QLineEdit(self.centralwidget)
        self.codeEmployeeEdit.setObjectName(u"codeEmployeeEdit")
        self.codeEmployeeEdit.setGeometry(QRect(110, 150, 101, 51))
        self.divisionEdit = QLineEdit(self.centralwidget)
        self.divisionEdit.setObjectName(u"divisionEdit")
        self.divisionEdit.setGeometry(QRect(110, 260, 171, 22))
        self.postEdit = QLineEdit(self.centralwidget)
        self.postEdit.setObjectName(u"postEdit")
        self.postEdit.setGeometry(QRect(110, 230, 281, 22))
        self.employementDateEdit = QLineEdit(self.centralwidget)
        self.employementDateEdit.setObjectName(u"employementDateEdit")
        self.employementDateEdit.setGeometry(QRect(110, 290, 141, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 0, 671, 51))
        self.label.setStyleSheet(u"font-weght: bold;\n"
"font-size: 20pt;\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 90, 201, 31))
        self.label_2.setStyleSheet(u"font-weght: bold;\n"
"font-size: 12pt;\n"
"")
        self.dismissalDateEdit = QLineEdit(self.centralwidget)
        self.dismissalDateEdit.setObjectName(u"dismissalDateEdit")
        self.dismissalDateEdit.setGeometry(QRect(110, 320, 141, 22))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 360, 31, 21))
        self.compensationEdit = QLineEdit(self.centralwidget)
        self.compensationEdit.setObjectName(u"compensationEdit")
        self.compensationEdit.setGeometry(QRect(110, 360, 141, 22))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(520, 90, 261, 31))
        self.label_4.setStyleSheet(u"font-weght: bold;\n"
"font-size: 12pt;\n"
"")
        self.numDocumentEdit = QLineEdit(self.centralwidget)
        self.numDocumentEdit.setObjectName(u"numDocumentEdit")
        self.numDocumentEdit.setGeometry(QRect(530, 140, 91, 22))
        self.codeDismissalEdit = QLineEdit(self.centralwidget)
        self.codeDismissalEdit.setObjectName(u"codeDismissalEdit")
        self.codeDismissalEdit.setGeometry(QRect(570, 230, 111, 22))
        self.subNumEdit = QLineEdit(self.centralwidget)
        self.subNumEdit.setObjectName(u"subNumEdit")
        self.subNumEdit.setGeometry(QRect(630, 200, 151, 22))
        self.registrationDateEdit = QLineEdit(self.centralwidget)
        self.registrationDateEdit.setObjectName(u"registrationDateEdit")
        self.registrationDateEdit.setGeometry(QRect(630, 140, 131, 22))
        self.dismissalReasonTextEdit = QPlainTextEdit(self.centralwidget)
        self.dismissalReasonTextEdit.setObjectName(u"dismissalReasonTextEdit")
        self.dismissalReasonTextEdit.setGeometry(QRect(530, 320, 251, 71))
        self.dismissalNameTextEdit = QPlainTextEdit(self.centralwidget)
        self.dismissalNameTextEdit.setObjectName(u"dismissalNameTextEdit")
        self.dismissalNameTextEdit.setGeometry(QRect(530, 260, 251, 51))
        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(480, 480, 311, 31))
        self.addButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(72, 121, 185);\n"
"    border-width: 5px;\n"
"    border-radius: 10px;\n"
"	font: bold;\n"
"    border-color: rgb(0, 0, 0);\n"
"    min-width: 5em;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QPushButton#evilButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setGeometry(QRect(810, 430, 91, 31))
        self.clearButton.setStyleSheet(u"font: bold;\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(173,173,173);\n"
"background-color: rgb(225,225,225);\n"
"\n"
"")
        self.numDismissalEdit = QLineEdit(self.centralwidget)
        self.numDismissalEdit.setObjectName(u"numDismissalEdit")
        self.numDismissalEdit.setGeometry(QRect(530, 200, 91, 22))
        self.codeDocumentEdit = QLineEdit(self.centralwidget)
        self.codeDocumentEdit.setObjectName(u"codeDocumentEdit")
        self.codeDocumentEdit.setGeometry(QRect(570, 170, 91, 22))
        addWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(addWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 925, 22))
        addWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(addWindow)
        self.statusbar.setObjectName(u"statusbar")
        addWindow.setStatusBar(self.statusbar)

        self.retranslateUi(addWindow)

        QMetaObject.connectSlotsByName(addWindow)
    # setupUi

    def retranslateUi(self, addWindow):
        addWindow.setWindowTitle(QCoreApplication.translate("addWindow", u"MainWindow", None))
        self.cancelButton.setText(QCoreApplication.translate("addWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.surnameEdit.setPlaceholderText(QCoreApplication.translate("addWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.nameEdit.setPlaceholderText(QCoreApplication.translate("addWindow", u"\u0418\u043c\u044f", None))
        self.patronymicEdit.setPlaceholderText(QCoreApplication.translate("addWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.codeEmployeeEdit.setPlaceholderText(QCoreApplication.translate("addWindow", u"\u041a\u043e\u0434 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.divisionEdit.setPlaceholderText(QCoreApplication.translate("addWindow", u"\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.postEdit.setPlaceholderText(QCoreApplication.translate("addWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.employementDateEdit.setText("")
        self.employementDateEdit.setPlaceholderText(QCoreApplication.translate("addWindow", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u0451\u043c\u0430 \u043d\u0430 \u0440\u0430\u0431\u043e\u0442\u0443", None))
        self.label.setText(QCoreApplication.translate("addWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0443\u0432\u043e\u043b\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 \u0432 \u0431\u0430\u0437\u0443 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.label_2.setText(QCoreApplication.translate("addWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0435", None))
        self.dismissalDateEdit.setText("")
        self.dismissalDateEdit.setPlaceholderText(QCoreApplication.translate("addWindow", u"\u0414\u0430\u0442\u0430 \u0443\u0432\u043e\u043b\u044c\u043d\u0435\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("addWindow", u"\u0440\u0443\u0431.", None))
        self.compensationEdit.setText("")
        self.compensationEdit.setPlaceholderText(QCoreApplication.translate("addWindow", u"\u0414\u0435\u043d\u0435\u0436\u043d\u0430\u044f \u043a\u043e\u043c\u043f\u0435\u043d\u0441\u0430\u0446\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("addWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043f\u043e \u0441\u0442\u0430\u0442\u044c\u0435 \u0443\u0432\u043e\u043b\u044c\u043d\u0435\u043d\u0438\u044f", None))
        self.numDocumentEdit.setPlaceholderText(QCoreApplication.translate("addWindow", u"\u2116 \u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430", None))
        self.codeDismissalEdit.setText("")
        self.codeDismissalEdit.setPlaceholderText(QCoreApplication.translate("addWindow", u"\u041a\u043e\u0434 \u0441\u0442\u0430\u0442\u044c\u0438", None))
        self.subNumEdit.setInputMask("")
        self.subNumEdit.setText("")
        self.subNumEdit.setPlaceholderText(QCoreApplication.translate("addWindow", u"\u2116 \u041f\u0443\u043d\u043a\u0442\u0430/\u041f\u043e\u0434\u043f\u0443\u043d\u043a\u0442\u0430", None))
        self.registrationDateEdit.setPlaceholderText(QCoreApplication.translate("addWindow", u"\u0414\u0430\u0442\u0430 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438", None))
        self.dismissalReasonTextEdit.setPlaceholderText(QCoreApplication.translate("addWindow", u"\u041f\u0440\u0438\u0447\u0438\u043d\u0430 \u0443\u0432\u043e\u043b\u044c\u043d\u0435\u043d\u0438\u044f", None))
        self.dismissalNameTextEdit.setPlaceholderText(QCoreApplication.translate("addWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u0430\u0442\u044c\u0438", None))
        self.addButton.setText(QCoreApplication.translate("addWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.clearButton.setText(QCoreApplication.translate("addWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043f\u043e\u043b\u044f", None))
        self.numDismissalEdit.setPlaceholderText(QCoreApplication.translate("addWindow", u"\u2116 \u0421\u0442\u0430\u0442\u044c\u0438", None))
        self.codeDocumentEdit.setPlaceholderText(QCoreApplication.translate("addWindow", u"\u041a\u043e\u0434 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430", None))
    # retranslateUi

