import sys

import sqlFunctions

from PyQt6 import QtWidgets

import design

class video_rental(QtWidgets.QMainWindow, design.Ui_menu):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.searchFilmButton.clicked.connect(self.searchFilm)
        self.issueCassetteButton.clicked.connect(self.inputNumber)
        self.returnCassetteButton.clicked.connect(self.returnCassetteInputNumber)
        self.arriveNewFilm.clicked.connect(self.addMovie)
        self.listDebtors.clicked.connect(self.showDebtors)
        self.writeOffCassettesButton.clicked.connect(self.writeOffCassettes)
        self.financialReportButton.clicked.connect(self.getFinancialReport)

    def setWindow(self, windowUi):
        self.secondWindow = QtWidgets.QWidget()
        self.secondWindowUi = windowUi
        self.secondWindowUi.setupUi(self.secondWindow)
        self.secondWindow.show()

    def showResult(self, resultText):
        self.setWindow(design.Ui_result())
        self.secondWindowUi.result.setText(resultText)

    def showResultWithButton(self, resultText):
        self.setWindow(design.Ui_result_with_button())
        self.secondWindowUi.result.setText(resultText)

    def searchFilm(self):
        self.setWindow(design.Ui_search_film())
        self.secondWindowUi.find.clicked.connect(self.searchFilmResult)

    def searchFilmResult(self):
        filmName = self.secondWindowUi.InputFilm.text()
        self.setWindow(design.Ui_result())
        self.secondWindowUi.result.setText(sqlFunctions.searchFilm(filmName))

    def addMovie(self):
        self.setWindow(design.Ui_search_film())
        self.secondWindowUi.find.clicked.connect(self.checkAvailabilityFilm)

    def checkAvailabilityFilm(self):
        filmName = self.secondWindowUi.InputFilm.text()
        if sqlFunctions.checkVailabilityMovie(filmName):
            self.addExistingFilmResult(filmName)
        else:
            self.addNewFilm(filmName)

    def addNewFilm(self, filmName):
        self.setWindow(design.Ui_add_new_film())
        self.secondWindowUi.addButton.clicked.connect(lambda: self.addNewFilmResult(filmName))

    def addExistingFilmResult(self, filmName):
        sqlFunctions.addExistingMovie(filmName)
        self.showResult(f"Фильм `{filmName}` успешно добавлен")

    def addNewFilmResult(self, filmName):
        filmCost = self.secondWindowUi.addCost.text()
        filmGenre = self.secondWindowUi.genreSelection.currentText()
        sqlFunctions.addNewFilm(filmName, filmGenre, filmCost)
        self.showResult(f"Фильм `{filmName}` успешно добавлен")

    def inputNumber(self):
        self.setWindow(design.Ui_input_number())
        self.secondWindowUi.nextButton.clicked.connect(self.checkAvailabilityUser)

    def checkAvailabilityUser(self):
        userNumber = self.secondWindowUi.inputNumber.text()
        if sqlFunctions.checkAvailabilityUser(userNumber):
            self.checkDebt(userNumber)
        else:
            self.addNewUser(userNumber)

    def addNewUser(self, userNumber):
        self.setWindow(design.Ui_registration())
        self.secondWindowUi.buttonNext.clicked.connect(lambda: self.addNewUserResult(userNumber))

    def addNewUserResult(self, userNumber):
        userFIO = self.secondWindowUi.inputFIO.text()
        sqlFunctions.addNewUser(userFIO, userNumber)
        self.showResultWithButton(f"Пользователь {userFIO} успешно добавлен")
        self.secondWindowUi.buttonNext.clicked.connect(lambda: self.issueCassette(userNumber))

    def checkDebt(self, userNumber):
        if sqlFunctions.checkDebt(userNumber):
            self.issueCassette(userNumber)
        else:
            self.payDept(userNumber)

    def payDept(self, userNumber):
        self.setWindow(design.Ui_result())
        self.secondWindowUi.result.setText(f"У клиента есть долг и он состовляет {sqlFunctions.getDept(userNumber)} рублей на сегодняшний день. Для выдачи кассеты клиент должен вернуть кассеты погасить долг.")

    def issueCassette(self, userNumber):
        self.setWindow(design.Ui_issue_cassette())
        self.secondWindowUi.buttonNext.clicked.connect(lambda: self.issueCassettePayment(userNumber))

    def issueCassettePayment(self, userNumber):
        filmName = self.secondWindowUi.inputFilm.text()
        rentDays = self.secondWindowUi.inputRentalDays.text()
        self.showResultWithButton(f"К оплате {sqlFunctions.calculateRentalPrice(filmName, rentDays)} рублей")
        self.secondWindowUi.buttonNext.setText("Опалачено")
        self.secondWindowUi.buttonNext.clicked.connect(lambda: self.issueCassettePaymentResult(userNumber, filmName, rentDays))

    def issueCassettePaymentResult(self, userNumber, filmName, rentDays):
        sqlFunctions.issueCassette(userNumber, filmName, rentDays)
        receipt = sqlFunctions.generateReceiptRent(userNumber, filmName, rentDays)
        self.showResult(receipt)

    def returnCassetteInputNumber(self):
        self.setWindow(design.Ui_input_number())
        self.secondWindowUi.nextButton.clicked.connect(self.returnCassetteInputFilm)

    def returnCassetteInputFilm(self):
        userNumber = self.secondWindowUi.inputNumber.text()
        self.setWindow(design.Ui_film_return())
        self.secondWindowUi.buttonNext.clicked.connect(lambda: self.returnCassetteCheckDebt(userNumber))

    def returnCassetteCheckDebt(self, userNumber):
        filmLost = self.secondWindowUi.isLost.isChecked()
        filmName = self.secondWindowUi.inputFilm.text()
        debt = sqlFunctions.getDeptOneMovie(userNumber, filmName)
        if (filmLost):
            debt -= sqlFunctions.getFilmCost(sqlFunctions.getFilmIdByFilmName(filmName))
        if (debt < 0):
            self.showResultWithButton(f"У клиента по этой кассете есть долг, равный {-debt}. Его нужно оплатить")
            self.secondWindowUi.buttonNext.setText("Оплачено")
            self.secondWindowUi.buttonNext.clicked.connect(lambda: self.returnCassetteDebtReceipt(userNumber, filmName, filmLost))
        else:
            self.showResult(sqlFunctions.generateReceiptReturn(userNumber, filmName, filmLost))
            sqlFunctions.returnCassette(userNumber,filmName,filmLost)

    def returnCassetteDebtReceipt(self, userNumber, filmName, filmLost):
        self.showResult(sqlFunctions.generateReceiptDept(userNumber,filmName,filmLost))
        sqlFunctions.returnCassette(userNumber, filmName, filmLost)

    def showDebtors(self):
        self.showResult(sqlFunctions.showDebtors())

    def writeOffCassettes(self):
        self.showResult(sqlFunctions.writeOffCassettes())

    def getFinancialReport(self):
        self.setWindow(design.Ui_financial_report())
        self.secondWindowUi.buttonNext.clicked.connect(self.getFinancialReportResult)

    def getFinancialReportResult(self):
        year = self.secondWindowUi.inputYear.text()
        self.showResult(sqlFunctions.showFinancialReport(year))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = video_rental()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()