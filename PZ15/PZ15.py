#Приложение УЧЕБНЫЙ ПЛАН для автоматизированного контроля учебной
#нагрузки по кафедре. Таблица Дисциплины должна иметь следующую структуру записи:
#Код дисциплины, Наименование дисциплины, Специальность, Лекции (колич.часов),
#Практические (колич.часов), Лабораторные (колич.часов), Форма отчетности.
#создай код
import sqlite3 as sq

def create_database(db_name="educational_plan.db"):
    try:
        with sq.connect(db_name) as con:
            cur = con.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS Дисциплины (
                    Код_дисциплины INTEGER PRIMARY KEY,
                    Наименование_дисциплины TEXT NOT NULL,
                    Специальность TEXT NOT NULL,
                    Лекции INTEGER NOT NULL,
                    Практические INTEGER NOT NULL,
                    Лабораторные INTEGER NOT NULL,
                    Форма_отчетности TEXT NOT NULL
                )
            ''')
            print(f"База данных '{db_name}' и таблица 'Дисциплины' успешно созданы.")
    except sq.Error as e:
        print(f"Ошибка при создании базы данных: {e}")
def add_discipline(db_name="educational_plan.db",
                   code: int = None,
                   name: str = None,
                   speciality: str = None,
                   lectures: int = None,
                   practical: int = None,
                   lab: int = None,
                   report_form: str = None):
    try:
        with sq.connect(db_name) as con:
            cur = con.cursor()
            if not all([code, name, speciality, lectures, practical, lab, report_form]):
                print("Ошибка: Не все обязательные поля заполнены.")
                return

            sql = '''INSERT INTO Дисциплины (Код_дисциплины, Наименование_дисциплины, Специальность,
                    Лекции, Практические, Лабораторные, Форма_отчетности)
                    VALUES (?, ?, ?, ?, ?, ?, ?)'''
            data = (code, name, speciality, lectures, practical, lab, report_form)

            cur.execute(sql, data)
            con.commit()
            print(f"Дисциплина '{name}' успешно добавлена.")

    except sq.Error as e:
        print(f"Ошибка при добавлении дисциплины: {e}")
def view_all_disciplines(db_name="educational_plan.db"):
    try:
        with sq.connect(db_name) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Дисциплины")
            rows = cur.fetchall()
            if not rows:
                print("Таблица 'Дисциплины' пуста.")
                return

            print("Список дисциплин:")
            for row in rows:
                print(row)
    except sq.Error as e:
        print(f"Ошибка при чтении данных: {e}")
def main():
    db_name = "educational_plan.db"
    create_database(db_name)

    while True:
        print("\nМеню:")
        print("1. Добавить дисциплину")
        print("2. Посмотреть все дисциплины")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            try:
                code = int(input("Код дисциплины: "))
                name = input("Наименование дисциплины: ")
                speciality = input("Специальность: ")
                lectures = int(input("Лекции (колич.часов): "))
                practical = int(input("Практические (колич.часов): "))
                lab = int(input("Лабораторные (колич.часов): "))
                report_form = input("Форма отчетности: ")

                add_discipline(db_name, code, name, speciality, lectures, practical, lab, report_form)
            except ValueError:
                print("Ошибка: Некорректный ввод числовых данных.")
        elif choice == "2":
            view_all_disciplines(db_name)
        elif choice == "3":
            print("Выход из приложения.")
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
