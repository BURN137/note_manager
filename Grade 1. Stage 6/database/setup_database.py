import sqlite3

# Функция по созданию базы данных
def setup_database(db_name):
    # Создаем подключение к базе данных
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    # Создаем таблицу notes
    cursor.execute('''CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        status TEXT NOT NULL,
        created_date TEXT NOT NULL,
        issue_date TEXT NOT NULL)''')
    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


# Инициализация базы данных
if __name__ == "__main__":
    setup_database("notes.db")