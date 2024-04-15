import sys

import mariadb

import re

from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel, QLineEdit, QApplication, QPushButton, QMainWindow, QTableView, QTableWidget, QTableWidgetItem, QMessageBox, QPlainTextEdit
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6 import QtCore


from main_window_ui import Ui_MainWindow
from delete_window_ui import Ui_delEmployeeWindow
from temp_table_ui import Ui_tempWindow 
from add_window_ui import Ui_addWindow



# Подключение к базе данных
try:
    connection = mariadb.connect(
        user = "root",
        password = "1234",
        host = "localhost",
        port = 3306,
        database = "db_dismissal"
    )

    print("Подключение к базе данных прошло успешно \n") 
except mariadb.Error as exception:
    print("! Ошибка подключения к базе данных:")
    print(exception, "\n")
    sys.exit(1)

# Создание курсора для взаимодействия с БД
cursor = connection.cursor()


# Функция, выполняющая запрос по подсчёту кол-ва записей в БД на основании таблицы emloyee:
def count_row(cursor):
    query = "SELECT COUNT(*) FROM employee"
    cursor.execute(query)
    return cursor.fetchone()[0]
    

# Класс главного экрана
class MainScreen(QMainWindow):
    # Конструктор
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Объявление элементов
        self.add_employee = self.ui.addEmployee # Кнопка для ввода
        self.delete_button = self.ui.deleteEmployee # Кнопка для удаления сотрудникаи из таблицы
        self.temp_table_button = self.ui.makeTempTable # Кнопка для создания временной таблицы
        self.exit_button = self.ui.exitButton # Кнопка для выхода из программы
        self.update_table_button = self.ui.updateEmployee # Кнопка для обновления данных в таблице уволенных сотрдудников
        self.row_num = self.ui.rowNum # Поле на котором выводится кол-во записей в таблице employee
        self.sum_num = self.ui.sumNum # Поле на котором выводится сумма компенсаций
        self.employee_table = self.ui.employeeTable # Таблица уволенных сотрудников
        

        # Подключение функций/значений на элементы
        self.add_employee.clicked.connect(self.gotoAddScreen)
        self.update_table_button.clicked.connect(self.updateEmployeeTable)
        self.delete_button.clicked.connect(self.openDelWindow)
        self.temp_table_button.clicked.connect(self.openTempTable)
        self.exit_button.clicked.connect(self.appExit)
        self.row_num.setText(str(count_row(cursor))) # Показывает кол-во записей в employee


        # Заполнение таблицы на главно экране начальными занчениями
        query = "SELECT * FROM employee"
        rows = count_row(cursor)
        self.employee_table.setRowCount(rows)
        cursor.execute(query)
        query_result = cursor.fetchall()

        self.updateEmployeeTable()



    # Метод для выхода из программы:
    def appExit(self):
        cursor.close()
        connection.close()
        print("Успешное отключение от базы данных \n")
        print("Работа программы завершена")
        sys.exit()

    # Метод для кнопки, выполняющей переход с главного экрана на экран добавления сотрудника
    def gotoAddScreen(self):
        addScreen = AddScreen()
        widget.addWidget(addScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
    # Метод для обновления данных в таблице уволенных на главном экране
    def updateEmployeeTable(self):
        # Очистка таблицы от данных
        self.employee_table.clearContents()

         # Обновляем отображение кол-ва записей в таблице
        rows = count_row(cursor)
        self.row_num.setText(str(rows))
        self.employee_table.setRowCount(rows)

        # Обновляем отобржаение суммы компенсаций
        sum_query = "SELECT SUM(Compensation) FROM document"
        cursor.execute(sum_query)
        sum = cursor.fetchone()[0]
        if sum == None:
            self.sum_num.setText("0")
        else:
            self.sum_num.setText(str(sum))
            
        query = "SELECT Code_document, Code_employee FROM document"
        cursor.execute(query)
        document_codes = cursor.fetchall()
        
        row = 0

        for i in range(len(document_codes)):
            self.employee_table.setItem(row, 0, QTableWidgetItem(f"{document_codes[i][0]}"))
            query = f"SELECT * FROM employee WHERE Code_employee = {document_codes[i][1]}"
            cursor.execute(query)
            employee_info = cursor.fetchone()
            
            for j in range(1, 8):
                self.employee_table.setItem(row, j, QTableWidgetItem(f"{employee_info[j - 1]}"))
            row += 1

        print("Таблица уволеных на главном экране обновлена \n")
        
        
    # Функция октрытия окна для удаления сотрудника из базы
    def openDelWindow(self):
        print("Открытие окна для удаления успешно \n")
        #self.setDisabled(True) # Это чтобы не лазить по главному эарну во время удаления Но оно кривое
        self.delete_window = QtWidgets.QMainWindow(main)
        self.ui = Ui_delEmployeeWindow()
        self.ui.setupUi(self.delete_window)
        self.delete_window.setFixedSize(290, 165)
        self.delete_window.setWindowTitle("Удаление сотрудника")
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.delete_window.show()

        # Объявление элементов
        self.cancel_button = self.ui.cancelButton
        self.delete_employee_button = self.ui.deleteButton
        self.code_employee = self.ui.codeEmpolyee
        
        # Такое же и во временную таблицу
        self.cancel_button.clicked.connect(self.delete_window.close)
        self.delete_employee_button.clicked.connect(self.delFromDb)
          

    # Функция для удаления сотрудника из БД по ключу
    def delFromDb(self):
        # Взятие кода сотрудника и проверка его соответсвия
        try:
            code = int(self.code_employee.text())
        except Exception as error:
            QMessageBox.critical(self, "Ошибка", "Некорректно введён код", QMessageBox.Ok)
            
        # Нужно узнать существует ли такой код в БД
        query = f"SELECT Code_document, Code_dismissal, Code_employee FROM document WHERE Code_document = {code}"
        cursor.execute(query)
        result = cursor.fetchone()
        if result == None:
            QMessageBox.critical(self, "Ошибка", "Такого кода не существует", QMessageBox.Ok)
        else:
            # Тут запросы, которые удаляют строки из базы данных по нужным кодам
            print(result[0])
            q1 = f"DELETE FROM document WHERE Code_document = {result[0]}"
            cursor.execute(q1)
            connection.commit()
            print(result[1])
            q2 = f"DELETE FROM dismissal WHERE Code_dismissal = '{result[1]}'"
            cursor.execute(q2)
            connection.commit()
            print(result[2])
            q3 = f"DELETE FROM employee WHERE Code_employee = {result[2]}"
            cursor.execute(q3)
            connection.commit()

            self.delete_window.close()
            self.updateEmployeeTable()
            QMessageBox.information(self, "А", "Сотрудник удалён из базы данных", QMessageBox.Ok)

    # Метод для открытия временной таблицы
    def openTempTable(self):
        print("Открытие временной таблицы прошло успешно \n")
        self.temporary_table = QtWidgets.QMainWindow(main)
        self.ui = Ui_tempWindow()
        self.ui.setupUi(self.temporary_table)
        self.temporary_table.setFixedSize(550, 405)
        self.temporary_table.setWindowTitle("Временная таблица")
        self.temporary_table.show()

        # Объявление элементов
        self.close_button = self.ui.closeButton
        self.temp_table = self.ui.tempTable

        # Назначение функций на элементы
        self.close_button.clicked.connect(self.temporary_table.close)
        self.temp_table.setRowCount(10)

        query = """CREATE TEMPORARY TABLE temp
                   (
                        Code_temp BIGINT AUTO_INCREMENT PRIMARY KEY,
                        some_date DATETIME,
                        some_strng VARCHAR(55)
                   )
                """
        cursor.execute(query)

    

# Класс окна для добавления сотрудника в БД
class AddScreen(QMainWindow):
    # Конструктор
    def __init__(self):
        super().__init__()
        self.ui = Ui_addWindow()
        self.ui.setupUi(self)

        # Объявление элементов
        self.surname = self.ui.surnameEdit
        self.name = self.ui.nameEdit
        self.patronymic = self.ui.patronymicEdit
        self.post = self.ui.postEdit
        self.division = self.ui.divisionEdit
        self.employement_date = self.ui.employementDateEdit
        self.dismissal_date = self.ui.dismissalDateEdit
        self.compensation = self.ui.compensationEdit
        self.registration_date = self.ui.registrationDateEdit
        self.dis_num = self.ui.numDismissalEdit
        self.sub_num = self.ui.subNumEdit
        self.dismissal_name = self.ui.dismissalNameTextEdit
        self.dismissal_reason = self.ui.dismissalReasonTextEdit
        self.doc_num = self.ui.numDocumentEdit

        self.code_employee = self.ui.codeEmployeeEdit
        self.code_dismissal = self.ui.codeDismissalEdit
        self.code_document = self.ui.codeDocumentEdit

        
        self.add_button = self.ui.addButton
        self.cancel_button = self.ui.cancelButton
        self.clear_button = self.ui.clearButton

        # Добавление функций/значений на элементы
        self.add_button.clicked.connect(self.addIntoDb)
        self.cancel_button.clicked.connect(self.gotoMainScreen)
        self.clear_button.clicked.connect(self.clearAddLines)

        self.surname.textChanged.connect(self.inputValidation)
        self.name.textChanged.connect(self.inputValidation)
        self.patronymic.textChanged.connect(self.inputValidation)
        self.post.textChanged.connect(self.inputValidation)
        self.division.textChanged.connect(self.inputValidation)
        self.employement_date.textChanged.connect(self.inputValidation)
        self.dismissal_date.textChanged.connect(self.inputValidation)
        self.compensation.textChanged.connect(self.inputValidation)
        self.registration_date.textChanged.connect(self.inputValidation)
        self.dis_num.textChanged.connect(self.inputValidation)
        self.sub_num.textChanged.connect(self.inputValidation)
        self.dismissal_name.textChanged.connect(self.inputValidation)
        self.dismissal_reason.textChanged.connect(self.inputValidation)
        self.code_employee.textChanged.connect(self.inputValidation)
        self.code_dismissal.textChanged.connect(self.inputValidation)
        self.doc_num.textChanged.connect(self.inputValidation)
        self.code_document.textChanged.connect(self.inputValidation)


    # Метод для возвращения на главный экран
    def gotoMainScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(self)
        main.updateEmployeeTable()

    # Метод для добавления сотрудника в БД
    def addIntoDb(self):
        # Счётчик ошибок
        check_errors = 0

        # Считывание данных из полей для ввода в локальные переменные и проверка правильности ввода
        surname = str(self.surname.text())
        if re.match(r"^([А-ЯЁ][а-яё]{0,30}(( |-)([А-ЯЁ][а-яё]{0,30})){0,2})|([A-Z][a-z]{0,30}(( |-)([A-Z][a-z]{0,30})){0,2})$", surname) == None:
            self.surname.setStyleSheet('background: rgb(245, 188, 188);')
            check_errors += 1
        else:
            pass

        name = self.name.text()
        if re.match(r"^([А-Я]{1}[а-яё]{0,50}|[A-Z]{1}[a-z]{0,50})$", name) == None:
            self.name.setStyleSheet('background: rgb(245, 188, 188);')
            check_errors += 1
        else:
            pass

        patronymic = self.patronymic.text()
        if re.match(r"^([А-Я]{1}[а-яё]{0,50}|[A-Z]{1}[a-z]{0,50})$", patronymic) == None:
            self.patronymic.setStyleSheet('background: rgb(245, 188, 188);')
            check_errors += 1
        else:
            pass

        post = self.post.text()
        if len(post) == 0:
            self.post.setStyleSheet('background: rgb(245, 188, 188);')
            check_errors += 1
        else:
            pass

        division = self.division.text()
        if len(division) == 0:
            self.division.setStyleSheet('background: rgb(245, 188, 188);')
            check_errors += 1
        else:
            pass

        employement_date = self.employement_date.text()
        if re.match(r"^\d{4}-((0\d)|(1[012]))-(([012]\d)|3[01])$", employement_date) == None:
            self.employement_date.setStyleSheet('background: rgb(245, 188, 188);')
            check_errors += 1
        else:
            pass

        dismissal_date = self.dismissal_date.text()
        if re.match(r"^\d{4}-((0\d)|(1[012]))-(([012]\d)|3[01])$", dismissal_date) == None:
            self.dismissal_date.setStyleSheet('background: rgb(245, 188, 188);')
            check_errors += 1
        else:
            pass

        try:
            compensation = int(self.compensation.text())
        except Exception as e:
            self.compensation.setStyleSheet('background: rgb(245, 188, 188);')
            check_errors += 1
        
        registration_date = self.registration_date.text()
        if re.match(r"^\d{4}-((0\d)|(1[012]))-(([012]\d)|3[01])$", registration_date) == None:
            self.registration_date.setStyleSheet('background: rgb(245, 188, 188);')
            check_errors += 1
        else:
            pass

        try:
            dis_num = int(self.sub_num.text())
        except Exception as e:
            self.dis_num.setStyleSheet('background: rgb(245, 188, 188);')
            check_errors += 1

        try:
            sub_num = int(self.sub_num.text())
        except Exception as e:
            self.sub_num.setStyleSheet('background: rgb(245, 188, 188);')
            check_errors += 1

        dismissal_name = self.dismissal_name.toPlainText()
        if len(dismissal_name) == 0:
            self.dismissal_name.setStyleSheet('background: rgb(245, 188, 188);')
            check_errors += 1
        else:
            pass

        dismissal_reason = self.dismissal_reason.toPlainText()
        if len(dismissal_reason) == 0:
            self.dismissal_reason.setStyleSheet('background: rgb(245, 188, 188);')
            check_errors += 1
        else:
            pass

        
        try:
            doc_num = int(self.doc_num.text())
        except Exception as e:
            self.doc_num.setStyleSheet('background: rgb(245, 188, 188);')
            check_errors += 1

        try:
            code_employee = int(self.code_employee.text())
        except Exception as e:
            self.code_employee.setStyleSheet('background: rgb(245, 188, 188);')
            check_errors += 1
        
        
        code_dismissal = str(self.code_dismissal.text())
        if len(code_dismissal) == 0:
            self.code_dismissal.setStyleSheet('background: rgb(245, 188, 188);')
            check_errors += 1
        else:
            pass
        

        try:
            code_document = int(self.code_document.text())
        except Exception as e:
            self.code_document.setStyleSheet('background: rgb(245, 188, 188);')
            check_errors += 1

        if check_errors == 0:
            # Добавляем сотрудника в базу данных
            try:
                query_employee = f"""INSERT INTO employee (Code_employee, surname_employee, name_employee, patronymic_employee, Post_employee, Division_employee, Date_employement)
                                    VALUES
                                    ({code_employee}, "{surname}", "{name}", "{patronymic}", "{post}", "{division}", "{employement_date}")
                                """
                cursor.execute(query_employee)
                connection.commit()

                query_dismissal = f"""INSERT INTO dismissal (Code_dismissal, name_dismissal, Reason_dismissal, Number_dismissal, Number_SubDismissal)
                                    VALUES
                                    ("{code_dismissal}", "{dismissal_name}", "{dismissal_reason}", {dis_num}, {sub_num})
                                """
                cursor.execute(query_dismissal)
                connection.commit()

                query_document = f"""INSERT INTO document (Code_document, Number_document, Date_registration, Date_dismissal, Code_dismissal, Code_employee, Compensation)
                                    VALUES
                                    ({code_document}, {doc_num}, "{registration_date}", "{dismissal_date}", "{code_dismissal}", {code_employee}, {compensation})
                                """
                cursor.execute(query_document)
                connection.commit()

                QMessageBox.information(self, "Информация", "Сотрудник добавлен в Базу данных", QMessageBox.Ok)
                self.gotoMainScreen()
                

            except mariadb.Error as error:
                QMessageBox.critical(self, "Ошибка", "Неверные данные для добавления в Базу Данных", QMessageBox.Ok)
                print(error)
            
        else:
            QMessageBox.critical(self, "Ошибка", "Неправильно введены данные", QMessageBox.Ok)
            print(check_errors)

    # Метод для очистки всех полей для ввода
    def clearAddLines(self):
        lines = [self.surname, self.name, self.patronymic, self.post, self.division, self.employement_date, self.dismissal_date, self.compensation, self.registration_date, self.sub_num, self.dismissal_name, self.dismissal_reason, self.code_employee, self.code_dismissal, self.code_document, self.dis_num, self.doc_num]

        for i in range(17):
            lines[i].clear()
            lines[i].setStyleSheet('background: rgb(255, 255, 255);')

    # Метод для проверки ввода данных в поля
    def inputValidation(self):
        sender = self.sender()
        if isinstance(sender, QLineEdit) or isinstance(sender, QPlainTextEdit):
            sender.setStyleSheet('background: rgb(255, 255, 255);')
        else:
            pass



# Функция main
if __name__ in '__main__':
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    main = MainScreen()

    widget.addWidget(main)

    widget.setFixedSize(925, 585)
    widget.setWindowTitle("УВС")
    widget.show()


    app.exec()