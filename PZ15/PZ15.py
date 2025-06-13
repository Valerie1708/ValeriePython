#Программа должна обеспечивать функционал по вводу данных в БД (10 позиций), их
#поиску(SELECT), удалению(DELETE) и редактированию(UPDATE). При организации поиска, удаления и
#редактирования использовать WHERE, предусмотреть по три SQL-запроса для каждой
#операции
#

# Приложение НОТАРИАЛЬНАЯ КОНТОРА для некоторой организации. БД
# должна содержать таблицу Нотариальные услуги со следующей структурой записи: ФИО
# клиента, услуга, сумма сделки, комиссионные (доход конторы).

import sqlite3 as sq
with sq.connect('notary_services.db') as con:
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS services')
    cur.execute("""CREATE TABLE IF NOT EXISTS services
                (surname_klient varchar(20) not null,
                name_klient varchar(20) not null,
                lastname_klient varchar(20) not null,
                notary_type varchar(30) not null,
                sum_of_transaction decimal(10,2) not null,
                dohod decimal(10,2) not null)""")
    information = [
        ("Иванов", "Петр", "Сергеевич", "Договор купли-продажи квартиры", 3200, 1100),
        ("Смирнова", "Анна", "Владимировна", "Доверенность на имущество", 2500, 800),
        ("Козлов", "Максим", "Алексеевич", "Дарение автомобиля", 3800, 1400),
        ("Петрова", "Елена", "Николаевна", "Свидетельство о наследстве", 3000, 1000),
        ("Волков", "Дмитрий", "Игоревич", "Брачный договор", 2800, 900),
        ("Морозова", "Ольга", "Викторовна", "Продажа дачного участка", 3500, 1200),
        ("Лебедев", "Артем", "Романович", "Доверенность на представительство", 2200, 700),
        ("Новикова", "Татьяна", "Степановна", "Оформление завещания", 2600, 850),
        ("Соколов", "Игорь", "Викторович", "Договор займа", 3100, 1050),
        ("Федорова", "Мария", "Олеговна", "Продажа коммерческой недвижимости", 3400, 1300)
    ]
    cur.executemany("INSERT INTO services VALUES (?, ?, ?, ?, ?, ?)", information)

    #cur.execute("SELECT * FROM services WHERE surname_klient = ?", ("Морозова",))
    #print(cur.fetchall())
    #cur.execute("SELECT * FROM services WHERE notary_type = ?", ("Договор купли-продажи квартиры",))
    #print(cur.fetchall())
    #cur.execute("SELECT surname_klient,notary_type,sum_of_transaction,dohod FROM services WHERE dohod > ?",(1000,))
    #print(cur.fetchall())

    #cur.execute("DELETE FROM services WHERE surname_klient = ?", ("Петрова",))
    #cur.execute("DELETE FROM services WHERE sum_of_transaction < ?", (2600,))
    #cur.execute("DELETE FROM services WHERE dohod > ?", (1000,))

    #cur.execute("UPDATE services SET notary_type = ? WHERE surname_klient = ? AND name_klient = ? AND lastname_klient = ?",("Продажа дачного участка", "Федорова", "Мария", "Олеговна"))
    #cur.execute("UPDATE services SET sum_of_transaction = ? WHERE surname_klient = ? AND name_klient = ? AND lastname_klient = ?",(3500, "Смирнова", "Анна", "Владимировна"))
    #cur.execute("UPDATE services SET dohod = ? + 500 WHERE notary_type = ?",(1300, "Продажа коммерческой недвижимости"))