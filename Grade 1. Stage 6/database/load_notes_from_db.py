# Загружаем данные из базы данных

import sqlite3

# Функция по загрузке данных из базы данных
def load_notes_from_db(db_name):
    # Создаем подключение к базе данных
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    # Импортируем заметки из базы данных
    cursor.execute('SELECT * FROM notes')
    rows = cursor.fetchall()
    notes = []
    for row in rows:
        notes.append({'id': row[0],
                      'username': row[1],
                      'title': row[2],
                      'content': row[3],
                      'status': row[4],
                      'created_date': row[5],
                      'issue_date': row[6]})
    connection.close()
    return notes