import pymysql
from config import host, user, password, db_name
import datetime


def setConnection():
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


def searchFilm(filmName):
    try:
        connection = setConnection()
        result = ''
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM фильмы WHERE Название = %s", filmName)
            targetFilm = cursor.fetchone()
            if (targetFilm is not None) and (targetFilm.get("Общее количество") != 0):
                quantityInStock = targetFilm.get("Количество в наличии")
                filmID = targetFilm.get("id_фильма")
                if quantityInStock > 0:
                    result += 'Фильм есть в наличии'
                else:
                    result += 'Фильма нет в наличии\n'
                    cursor.execute(f"SELECT * \
                            FROM `арендованные фильмы` \
                            WHERE `id_копии_фильма` IN ( \
                            SELECT `id_копии_фильма` \
                            FROM `копии фильмов` \
                            WHERE `id_фильма` = {filmID}) \
                            AND ISNULL(`Дата возврата`);")
                    result += "Копии фильма должны вернуться в следующие даты: \n"
                    for row in cursor.fetchall():
                        result += (str)(
                            row.get("Дата выдачи") + datetime.timedelta(days=(row.get("Длительность, дней")))) + '\n'
            else:
                result += "Такого фильма нету в видеосалоне"
    finally:
        connection.close()
        return result


def checkVailabilityMovie(filmName):
    connection = setConnection()
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM `фильмы` WHERE `Название` = "{filmName}";')
        targetFilm = cursor.fetchone()
        if (targetFilm is None):
            return False
        else:
            return True
    connection.close()


def addExistingMovie(filmName):
    connection = setConnection()
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE `фильмы` SET `Количество в наличии` = `Количество в наличии` + 1, `Общее количество` = `Общее количество` + 1 WHERE `Название` = %s",
            (filmName,))
        cursor.execute(
            "INSERT INTO `копии фильмов` (`id_фильма`) VALUES ((SELECT `id_фильма` FROM `фильмы` WHERE `Название` = %s))",
            (filmName,))
    connection.commit()
    connection.close()


def addNewFilm(filmName, filmGenre, filmCost):
    connection = setConnection()
    with connection.cursor() as cursor:
        filmCost = int(filmCost)
        cursor.execute(
            f'INSERT INTO фильмы (Название, `Стоимость кассеты`, `Количество в наличии`, `Общее количество`, id_категории) VALUES ("{filmName}", {filmCost}, 1, 1, (SELECT id_категории FROM категории WHERE Название = "{filmGenre}"));')
        cursor.execute(
            f'INSERT INTO `копии фильмов` (id_фильма, id_копии_фильма) VALUES ((SELECT id_фильма FROM фильмы WHERE Название = "{filmName}"), NULL);')
    connection.commit()
    connection.close()


def checkAvailabilityUser(userNumber):
    connection = setConnection()
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM `клиенты` WHERE `Номер телефона` = "{userNumber}";')
        targetUser = cursor.fetchone()
        if targetUser is None:
            return False
        else:
            return True
    connection.close()

def addNewUser(userFIO, userNumber):
    connection = setConnection()
    with connection.cursor() as cursor:
        cursor.execute(f'INSERT INTO клиенты (ФИО, `Номер телефона`) VALUES ("{userFIO}", {userNumber});')
    connection.commit()
    connection.close()

def checkDebt(userNumber):
    connection = setConnection()
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM `арендованные фильмы` WHERE id_клиента = (SELECT id_клиента FROM клиенты WHERE `Номер телефона` = {userNumber}) AND (`Дата возврата` IS NULL OR `Дата возврата` = "1000-01-01");')
        takenCassettes = cursor.fetchall()
        for cassette in takenCassettes:
            filmID = getFilmIdByCopyId(cassette['id_копии_фильма'])
            if getFilmCost(filmID) + (cassette['Длительность, дней'] - (datetime.datetime.now() - datetime.datetime.combine(cassette['Дата выдачи'], datetime.time())).days) * getFilmTariff(filmID) < 0:
                connection.close()
                return 0
    connection.close()
    return 1

def getDept(userNumber):
    connection = setConnection()
    with connection.cursor() as cursor:
        deptSum = 0
        cursor.execute(
            f'SELECT * FROM `арендованные фильмы` WHERE id_клиента = (SELECT id_клиента FROM клиенты WHERE `Номер телефона` = {userNumber}) AND (`Дата возврата` IS NULL OR `Дата возврата` = "1000-01-01") ;')
        takenСassettes = cursor.fetchall()
        for cassette in takenСassettes:
            filmID = getFilmIdByCopyId(cassette['id_копии_фильма'])
            dept = getFilmCost(filmID) + (cassette['Длительность, дней'] - (
                    datetime.datetime.now() - datetime.datetime.combine(cassette['Дата выдачи'], datetime.time())).days) * getFilmTariff(filmID)
            if dept < 0:
                deptSum += abs(dept)
        connection.close()
        return deptSum

def getDeptOneMovie(userNumber, filmName):
    connection = setConnection()
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM `арендованные фильмы` WHERE id_клиента = {getUserId(userNumber)} AND id_копии_фильма IN (SELECT id_копии_фильма FROM `копии фильмов` WHERE id_фильма = {getFilmIdByFilmName(filmName)}) AND (`Дата возврата` IS NULL OR `Дата возврата` = "1000-01-01");')
        currentRents = cursor.fetchall()
        for rent in currentRents:
            debt = getFilmCost(getFilmIdByFilmName(filmName)) + (rent['Длительность, дней'] - (datetime.datetime.now() - datetime.datetime.combine(rent['Дата выдачи'], datetime.time())).days) * getFilmTariff(getFilmIdByFilmName(filmName))
            connection.close()
            return debt

def getOverdueDays(userNumber, filmName):
    connection = setConnection()
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM `арендованные фильмы` WHERE id_клиента = {getUserId(userNumber)} AND id_копии_фильма IN (SELECT id_копии_фильма FROM `копии фильмов` WHERE id_фильма = {getFilmIdByFilmName(filmName)}) AND (`Дата возврата` IS NULL OR `Дата возврата` = "1000-01-01");')
        currentRents = cursor.fetchall()
        for rent in currentRents:
            days = rent['Длительность, дней'] - (datetime.datetime.now() - datetime.datetime.combine(rent['Дата выдачи'], datetime.time())).days
            connection.close()
            return -days

def getFilmCost(filmID):
    connection = setConnection()
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT `Стоимость кассеты` FROM `фильмы` WHERE `id_фильма` = {filmID};')
        cost = cursor.fetchall()
    connection.close()
    return int(cost[0]['Стоимость кассеты'])

def getFilmTariff(filmID):
    connection = setConnection()
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT `категории`.`Стоимость за сутки`\
FROM `фильмы`\
JOIN `категории` ON `фильмы`.`id_категории` = `категории`.`id_категории`\
WHERE `фильмы`.`id_фильма` = {filmID};')
        tariff = cursor.fetchall()
    connection.close()
    return int(tariff[0]['Стоимость за сутки'])

def getNumOfFilmsByFilmId(filmID):
    connection = setConnection()
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT `Общее количество` FROM `фильмы` WHERE `id_фильма` = {filmID};')
        film = cursor.fetchall()
    connection.close()
    return int(film[0]['Общее количество'])

def getFilmIdByCopyId(copyID):
    connection = setConnection()
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT `id_фильма`\
FROM `копии фильмов`\
WHERE `id_копии_фильма` = {copyID};')
        cassette = cursor.fetchall()
    connection.close()
    return int(cassette[0].get('id_фильма'))

def getUserFio(userNumber):
    connection = setConnection()
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT `ФИО`\
    FROM `клиенты`\
    WHERE `Номер телефона` = {userNumber};')
        user = cursor.fetchall()
    connection.close()
    return user[0].get('ФИО')

def getUserId(userNumber):
    connection = setConnection()
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT `id_Клиента`\
    FROM `клиенты`\
    WHERE `Номер телефона` = {userNumber};')
        user = cursor.fetchall()
    connection.close()
    return int(user[0].get('id_Клиента'))

def generateReceiptReturn(userNumber, filmName, filmLost):
    filmTariff = getFilmTariff(getFilmIdByFilmName(filmName))
    days = -getOverdueDays(userNumber, filmName)
    filmCost = getFilmCost(getFilmIdByFilmName(filmName))
    if filmLost:
        receipt = f"""Квитанция о возврате кассеты

                    Клиент: {getUserFio(userNumber)}
                    Телефон: {userNumber}

                    Название фильма: {filmName}
                    Залог: {filmCost}

                    Стоимость аренды за одни сутки: {filmTariff}
                    Дней до конца аренды: {days}
                    Потеря кассеты: {filmCost}
                    
                    Итоговая сумма возврата: {days * filmTariff} руб.

                    Спасибо за обращение!"""
    else:
        receipt = f"""Квитанция о возврате кассеты
    
            Клиент: {getUserFio(userNumber)}
            Телефон: {userNumber}
    
            Название фильма: {filmName}
            Залог: {filmCost}
    
            Стоимость аренды за одни сутки: {filmTariff}
            Дней до конца аренды: {days}
            
            Итоговая сумма возврата: {filmCost + days * filmTariff} руб.
    
            Спасибо за обращение!"""
    return receipt

def generateReceiptDept(userNumber, filmName, filmLost):
    filmTariff = getFilmTariff(getFilmIdByFilmName(filmName))
    days = getOverdueDays(userNumber, filmName)
    filmCost = getFilmCost(getFilmIdByFilmName(filmName))
    if(filmLost):
        receipt = f"""Квитанция об оплате долга

        Клиент: {getUserFio(userNumber)}
        Телефон: {userNumber}
        
        Название фильма: {filmName}
        Залог: {filmCost}
        
        Стоимость аренды за одни сутки: {filmTariff}
        Количество просроченных дней: {days}
        Потеря фильма: {filmCost}
        
        Итоговая сумма долга: {days * filmTariff} руб.

        Спасибо за обращение!"""
    else:
        receipt = f"""Квитанция об оплате долга

               Клиент: {getUserFio(userNumber)}
               Телефон: {userNumber}

               Название фильма: {filmName}
               Залог: {filmCost}

               Стоимость аренды за одни сутки: {filmTariff}
               Количество просроченных дней: {days}
               
               Итоговая сумма долга: {days * filmTariff - filmCost} руб.

               Спасибо за обращение!"""
    return receipt

def calculateRentalPrice(filmName, rentalDays):
    filmID = getFilmIdByFilmName(filmName)
    return getFilmCost(filmID) + int(rentalDays) * getFilmTariff(filmID)

def getFilmIdByFilmName(filmName):
    connection = setConnection()
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT id_фильма FROM фильмы WHERE Название = "{filmName}";')
        film = cursor.fetchall()
    connection.close()
    return int(film[0].get('id_фильма'))

def getFilmNameByFilmId(filmID):
    connection = setConnection()
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT `Название`\
    FROM `фильмы`\
    WHERE `id_фильма` = {filmID};')
        film = cursor.fetchall()
    connection.close()
    return film[0].get('Название')

def generateReceiptRent(userNumber, filmName, rentDays):
    deposit = getFilmCost(getFilmIdByFilmName(filmName))
    rent = getFilmTariff(getFilmIdByFilmName(filmName)) * int(rentDays)
    receipt = f"""Квитанция об оплате аренды фильма

    Клиент: {getUserFio(userNumber)}
    Телефон: {userNumber}

    Сумма залога: {deposit} руб.
    Сумма аренды: {rent} руб.
    Итого: {deposit + rent} руб.

    Спасибо за обращение!"""
    return receipt

def issueCassette(userNumber, filmName, rentDays):
    connection = setConnection()
    with connection.cursor() as cursor:
        copyID = getFreeCassetteByFilmName(filmName)
        cursor.execute(f'INSERT INTO `арендованные фильмы` (`Дата выдачи`, `Длительность, дней`, id_копии_фильма, id_клиента)\
         VALUES ("{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}", {rentDays}, {copyID}, {getUserId(userNumber)});')
        cursor.execute(f"UPDATE фильмы SET `Количество в наличии` = `Количество в наличии` - 1 WHERE `Название` = '{filmName}';")
    connection.commit()
    connection.close()

def getFreeCassetteByFilmName(filmName):
    filmID = getFilmIdByFilmName(filmName)
    connection = setConnection()
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT id_копии_фильма FROM `копии фильмов` WHERE id_фильма = {filmID} AND id_копии_фильма NOT IN (SELECT id_копии_фильма FROM `арендованные фильмы` WHERE id_копии_фильма IS NOT NULL AND `Дата возврата` IS NULL);')
        cassette = cursor.fetchall()
    connection.close()
    return int(cassette[0].get('id_копии_фильма'))

def showDebtors():
    connection = setConnection()
    listDebtors = "Должники:\n"
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM `клиенты`")
        listUsers = cursor.fetchall()
        for user in listUsers:
            if not(checkDebt(user['Номер телефона'])):
                listDebtors += f"{user['ФИО']}  +{user['Номер телефона']}   Долг: {getDept(user['Номер телефона'])} руб.\n"
    connection.close()
    return listDebtors

def writeOffCassettes():
    connection = setConnection()
    listWriteOffCassettes = "Списанные кассеты:\n"
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM `арендованные фильмы` WHERE `Дата возврата` IS NULL;')
        rentals = cursor.fetchall()
        for rent in rentals:
            copyID = rent['id_копии_фильма']
            rentDate = rent['Дата выдачи']
            rentID = rent['id_аренды']
            current_date = datetime.date.today()
            if (current_date - rentDate).days > 365:
                listWriteOffCassettes += f'Копия фильма "{getFilmNameByFilmId(getFilmIdByCopyId(copyID))}"\n'
                cursor.execute(f"UPDATE фильмы SET `Общее количество` = `Общее количество` - 1 WHERE `id_фильма` = {getFilmIdByCopyId(copyID)};")
                cursor.execute(f'UPDATE `арендованные фильмы` SET `Дата возврата` = "1000-01-01" WHERE `id_аренды` = {rentID};')
    connection.commit()
    connection.close()
    if listWriteOffCassettes == "Списанные кассеты:\n":
        listWriteOffCassettes += "Нет подходящих кассет"
    return listWriteOffCassettes

def returnCassette(userNumber, filmName, filmLost):
    connection = setConnection()
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM `арендованные фильмы` WHERE id_клиента = {getUserId(userNumber)} AND id_копии_фильма IN (SELECT id_копии_фильма FROM `копии фильмов` WHERE id_фильма = {getFilmIdByFilmName(filmName)}) AND (`Дата возврата` IS NULL OR `Дата возврата` = "1000-01-01");')
        currentRents = cursor.fetchall()
        cursor.execute(f'UPDATE `арендованные фильмы` SET `Дата возврата` = "{datetime.datetime.now()}" WHERE id_клиента = {getUserId(userNumber)} AND id_копии_фильма IN (SELECT id_копии_фильма FROM `копии фильмов` WHERE id_фильма = {getFilmIdByFilmName(filmName)}) AND (`Дата возврата` IS NULL OR `Дата возврата` = "1000-01-01");')
        for rent in currentRents:
            if(filmLost):
                cursor.execute(f"UPDATE фильмы SET `Общее количество` = `Общее количество` - 1 \
WHERE id_фильма = (SELECT id_фильма FROM `копии фильмов` WHERE id_копии_фильма = {rent['id_копии_фильма']});")
                #cursor.execute(f"UPDATE `копии фильмов` SET id_фильма = NULL WHERE id_копии_фильма = {rent['id_копии_фильма']};")
            else:
                cursor.execute(f"UPDATE фильмы SET `Количество в наличии` = `Количество в наличии` + 1 WHERE id_фильма = (SELECT id_фильма FROM `копии фильмов` WHERE id_копии_фильма = {rent['id_копии_фильма']});")
    connection.commit()
    connection.close()

def calculateProfit(startingDate, endingDate):
    connection = setConnection()
    profit = 0
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM `арендованные фильмы` WHERE `Дата возврата` IS NOT NULL AND `Дата возврата` != "1000-01-01" AND `Дата выдачи` BETWEEN "{startingDate}" AND "{endingDate}"')
        currentRents = cursor.fetchall()
        for rent in currentRents:
            filmID = getFilmIdByCopyId(rent['id_копии_фильма'])
            profit += ((rent['Дата возврата'] - rent['Дата выдачи']).days) * getFilmTariff(filmID)
    connection.close()
    return profit

def calculateLoss(startingDate, endingDate):
    connection = setConnection()
    loss = 0
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM `арендованные фильмы` WHERE `Дата возврата` = "1000-01-01" AND `Дата выдачи` BETWEEN "{startingDate}" AND "{endingDate}"')
        currentRents = cursor.fetchall()
        for rent in currentRents:
            filmID = getFilmIdByCopyId(rent['id_копии_фильма'])
            loss += getFilmCost(filmID) - rent['Длительность, дней'] * getFilmTariff(filmID)
    connection.close()
    return loss


def showFinancialReport(year):
    profit_1 = calculateProfit(year + "-01-01", year + "-03-31")
    loss_1 = calculateLoss(year + "-01-01", year + "-03-31")
    profit_2 = calculateProfit(year + "-04-01", year + "-06-30")
    loss_2 = calculateLoss(year + "-04-01", year + "-06-30")
    profit_3 = calculateProfit(year + "-07-01", year + "-09-30")
    loss_3 = calculateLoss(year + "-07-01", year + "-09-30")
    profit_4 = calculateProfit(year + "-10-01", year + "-12-31")
    loss_4 = calculateLoss(year + "-10-01", year + "-12-31")
    FinancialReport = f"""Финансовый отчет за {year} год:\n
    1 Квартал: Прибыль: {profit_1} Убыток: {loss_1} Итог: {profit_1 - loss_1}
    2 Квартал: Прибыль: {profit_2} Убыток: {loss_2} Итог: {profit_2 - loss_2}
    3 Квартал: Прибыль: {profit_3} Убыток: {loss_3} Итог: {profit_3 - loss_3}
    4 Квартал: Прибыль: {profit_4} Убыток: {loss_4} Итог: {profit_4 - loss_4}
    """
    return FinancialReport