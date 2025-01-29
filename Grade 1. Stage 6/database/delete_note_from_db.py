# Удаление заметки по ее ID.
# ID запрашиваются у пользователя
# Для работы используется база с именем notes.db созданная ранее

import sqlite3

# Функция для подсчета количества заметок в базе данных
def quantity_rows_in_db(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM notes')
    quantity_rows = len(cursor.fetchall())
    return quantity_rows

# Функция по удалению заметки по ее ID из базы данных
def delete_note_from_db(note_id, db_name):
    # Создаем подключение к базе данных
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM notes
                   WHERE id = ?""", note_id)
    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()

