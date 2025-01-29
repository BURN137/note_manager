# Фильтрация заметок по статусу
# Статус запрашивается у пользователя
# Фильтрация не чувствительна к регистру
# Для работы используется база с именем notes.db созданная ранее

import sqlite3

# Функция по фильтрации заметок по статусу
def filter_notes_by_status(status, db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM notes WHERE status = ?""",
                   (status,))
    rows = cursor.fetchall()
    connection.close()
    notes = []
    for row in rows:
        notes.append({'id': row[0],
                      'username': row[1],
                      'title': row[2],
                      'content': row[3],
                      'status': row[4],
                      'created_date': row[5],
                      'issue_date': row[6]})
    return notes