# Form implementation generated from reading ui file 'C:\Users\serge\OneDrive\Рабочий стол\учеба\4 сем\это база\интерфейс\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_menu(object):
    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.setEnabled(True)
        menu.resize(684, 543)
        self.centralwidget = QtWidgets.QWidget(parent=menu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.searchFilmButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.searchFilmButton.setObjectName("searchFilm")
        self.verticalLayout_2.addWidget(self.searchFilmButton)
        self.returnCassetteButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.returnCassetteButton.setObjectName("returnCassette")
        self.verticalLayout_2.addWidget(self.returnCassetteButton)
        self.issueCassetteButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.issueCassetteButton.setObjectName("issueCassette")
        self.verticalLayout_2.addWidget(self.issueCassetteButton)
        self.arriveNewFilm = QtWidgets.QPushButton(parent=self.centralwidget)
        self.arriveNewFilm.setObjectName("arriveNewFilm")
        self.verticalLayout_2.addWidget(self.arriveNewFilm)
        self.writeOffCassettesButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.writeOffCassettesButton.setObjectName("writeOffCassettes")
        self.verticalLayout_2.addWidget(self.writeOffCassettesButton)
        self.listDebtors = QtWidgets.QPushButton(parent=self.centralwidget)
        self.listDebtors.setObjectName("listDebtors")
        self.verticalLayout_2.addWidget(self.listDebtors)
        self.financialReportButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.financialReportButton.setObjectName("financialReport")
        self.verticalLayout_2.addWidget(self.financialReportButton)
        menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)
        menu.setTabOrder(self.searchFilmButton, self.returnCassetteButton)
        menu.setTabOrder(self.returnCassetteButton, self.issueCassetteButton)
        menu.setTabOrder(self.issueCassetteButton, self.arriveNewFilm)
        menu.setTabOrder(self.arriveNewFilm, self.writeOffCassettesButton)
        menu.setTabOrder(self.writeOffCassettesButton, self.listDebtors)
        menu.setTabOrder(self.listDebtors, self.financialReportButton)

    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "Видеосалон"))
        self.searchFilmButton.setText(_translate("menu", "Поиск фильма в базе"))
        self.returnCassetteButton.setText(_translate("menu", "Возврат кассеты"))
        self.issueCassetteButton.setText(_translate("menu", "Выдача кассеты"))
        self.arriveNewFilm.setText(_translate("menu", "Приход новых фильмов"))
        self.writeOffCassettesButton.setText(_translate("menu", "Проивзести списание невозвращенных кассет"))
        self.listDebtors.setText(_translate("menu", "Список должников"))
        self.financialReportButton.setText(_translate("menu", "Финансовый отчет за год"))

class Ui_search_film(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(327, 141)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.InputFilm = QtWidgets.QLineEdit(parent=Form)
        self.InputFilm.setObjectName("InputFilm")
        self.verticalLayout.addWidget(self.InputFilm)
        self.find = QtWidgets.QPushButton(parent=Form)
        self.find.setObjectName("find")
        self.verticalLayout.addWidget(self.find)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Введите название фильма:"))
        self.find.setText(_translate("Form", "Найти"))

class Ui_result(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 400)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.result = QtWidgets.QLabel(parent=Dialog)
        self.result.setObjectName("result")
        self.horizontalLayout.addWidget(self.result)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Результат"))

class Ui_add_new_film(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(505, 137)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.addCost = QtWidgets.QLineEdit(parent=Form)
        self.addCost.setObjectName("addCost")
        self.verticalLayout.addWidget(self.addCost)
        self.genreSelection = QtWidgets.QComboBox(parent=Form)
        self.genreSelection.setObjectName("genreSelection")
        self.genreSelection.addItem("")
        self.genreSelection.addItem("")
        self.genreSelection.addItem("")
        self.genreSelection.addItem("")
        self.genreSelection.addItem("")
        self.genreSelection.addItem("")
        self.genreSelection.addItem("")
        self.genreSelection.addItem("")
        self.genreSelection.addItem("")
        self.genreSelection.addItem("")
        self.genreSelection.addItem("")
        self.verticalLayout.addWidget(self.genreSelection)
        self.addButton = QtWidgets.QPushButton(parent=Form)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление фильма"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Вы добавляете новый фильм. Укажите его жанр и стоимость касеты </span></p></body></html>"))
        #self.addCost.setText(_translate("Form", "Стоимость касеты:"))
        self.genreSelection.setItemText(0, _translate("Form", "боевик"))
        self.genreSelection.setItemText(1, _translate("Form", "вестерн"))
        self.genreSelection.setItemText(2, _translate("Form", "детектив"))
        self.genreSelection.setItemText(3, _translate("Form", "исторический"))
        self.genreSelection.setItemText(4, _translate("Form", "драма"))
        self.genreSelection.setItemText(5, _translate("Form", "комедия"))
        self.genreSelection.setItemText(6, _translate("Form", "мелодрама"))
        self.genreSelection.setItemText(7, _translate("Form", "приключения"))
        self.genreSelection.setItemText(8, _translate("Form", "триллер"))
        self.genreSelection.setItemText(9, _translate("Form", "ужастик"))
        self.genreSelection.setItemText(10, _translate("Form", "фантастика"))
        self.addButton.setText(_translate("Form", "Добавить"))

class Ui_input_number(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 98)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inputNumber = QtWidgets.QLineEdit(parent=Form)
        self.inputNumber.setObjectName("inputNumber")
        self.horizontalLayout.addWidget(self.inputNumber)
        self.nextButton = QtWidgets.QPushButton(parent=Form)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout.addWidget(self.nextButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Введите номер телефона клиента:"))
        self.nextButton.setText(_translate("Form", "Далее"))

class Ui_registration(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(278, 119)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.inputFIO = QtWidgets.QLineEdit(parent=Form)
        self.inputFIO.setObjectName("inputFIO")
        self.verticalLayout.addWidget(self.inputFIO)
        self.buttonNext = QtWidgets.QPushButton(parent=Form)
        self.buttonNext.setObjectName("buttonNext")
        self.verticalLayout.addWidget(self.buttonNext)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Регистрация пользователя"))
        self.label.setText(_translate("Form", "<html><head/><body><p>Пользователь с таким номером не обнаружен.</p><p>Для регистрации нужно вести его ФИО:</p></body></html>"))
        self.buttonNext.setText(_translate("Form", "Зарегистрировать"))

class Ui_result_with_button(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 168)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.result = QtWidgets.QLabel(parent=Form)
        self.result.setText("")
        self.result.setObjectName("result")
        self.verticalLayout.addWidget(self.result)
        self.buttonNext = QtWidgets.QPushButton(parent=Form)
        self.buttonNext.setObjectName("buttonNext")
        self.verticalLayout.addWidget(self.buttonNext)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "результат"))
        self.buttonNext.setText(_translate("Form", "ОК"))

class Ui_pay_dept(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 109)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dept = QtWidgets.QLabel(parent=Form)
        self.dept.setText("")
        self.dept.setObjectName("dept")
        self.verticalLayout.addWidget(self.dept)
        self.payDept = QtWidgets.QPushButton(parent=Form)
        self.payDept.setObjectName("payDept")
        self.verticalLayout.addWidget(self.payDept)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Оплата долга"))
        self.payDept.setText(_translate("Form", "Оплачено"))

class Ui_issue_cassette(object):
    def setupUi(self, issueCassette):
        issueCassette.setObjectName("issueCassette")
        issueCassette.resize(399, 136)
        self.formLayout = QtWidgets.QFormLayout(issueCassette)
        self.formLayout.setObjectName("formLayout")
        self.buttonNext = QtWidgets.QPushButton(parent=issueCassette)
        self.buttonNext.setObjectName("buttonNext")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.buttonNext)
        self.label = QtWidgets.QLabel(parent=issueCassette)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label)
        self.inputRentalDays = QtWidgets.QSpinBox(parent=issueCassette)
        self.inputRentalDays.setObjectName("inputRentalDays")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputRentalDays)
        self.inputFilm = QtWidgets.QLineEdit(parent=issueCassette)
        self.inputFilm.setObjectName("inputFilm")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputFilm)

        self.retranslateUi(issueCassette)
        QtCore.QMetaObject.connectSlotsByName(issueCassette)

    def retranslateUi(self, issueCassette):
        _translate = QtCore.QCoreApplication.translate
        issueCassette.setWindowTitle(_translate("issueCassette", "выдача кассеты"))
        self.buttonNext.setText(_translate("issueCassette", "Далее"))
        self.label.setText(_translate("issueCassette", "Укажите название фильма и количество дней аренды:"))

class Ui_film_return(object):
    def setupUi(self, film_return):
        film_return.setObjectName("film_return")
        film_return.resize(400, 133)
        self.verticalLayout = QtWidgets.QVBoxLayout(film_return)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=film_return)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.inputFilm = QtWidgets.QLineEdit(parent=film_return)
        self.inputFilm.setObjectName("inputFilm")
        self.verticalLayout.addWidget(self.inputFilm)
        self.isLost = QtWidgets.QCheckBox(parent=film_return)
        self.isLost.setObjectName("isLost")
        self.verticalLayout.addWidget(self.isLost)
        self.buttonNext = QtWidgets.QPushButton(parent=film_return)
        self.buttonNext.setObjectName("buttonNext")
        self.verticalLayout.addWidget(self.buttonNext)

        self.retranslateUi(film_return)
        QtCore.QMetaObject.connectSlotsByName(film_return)

    def retranslateUi(self, film_return):
        _translate = QtCore.QCoreApplication.translate
        film_return.setWindowTitle(_translate("film_return", "Возврат кассеты"))
        self.label.setText(_translate("film_return", "Введите название возвращаемой кассеты:"))
        self.isLost.setText(_translate("film_return", "Кассета потеряна"))
        self.buttonNext.setText(_translate("film_return", "Далее"))

class Ui_financial_report(object):
    def setupUi(self, financialReport):
        financialReport.setObjectName("financialReport")
        financialReport.resize(400, 126)
        self.verticalLayout = QtWidgets.QVBoxLayout(financialReport)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=financialReport)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.inputYear = QtWidgets.QLineEdit(parent=financialReport)
        self.inputYear.setObjectName("inputYear")
        self.verticalLayout.addWidget(self.inputYear)
        self.buttonNext = QtWidgets.QPushButton(parent=financialReport)
        self.buttonNext.setObjectName("buttonNext")
        self.verticalLayout.addWidget(self.buttonNext)

        self.retranslateUi(financialReport)
        QtCore.QMetaObject.connectSlotsByName(financialReport)

    def retranslateUi(self, financialReport):
        _translate = QtCore.QCoreApplication.translate
        financialReport.setWindowTitle(_translate("financialReport", "Финансовый отчет"))
        self.label.setText(_translate("financialReport", "Введите год, за который хотите получить финаносвый отчет:"))
        self.buttonNext.setText(_translate("financialReport", "Получить"))