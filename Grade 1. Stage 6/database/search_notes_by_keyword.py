# Поиск заметок по ключевым словам в полях title и content
# Ключевое слово запрашивается у пользователя
# Для работы используется база с именем notes.db созданная ранее
# Поиск чувствителен к регистру (в SQlite поиск кириллицы осуществляется только с учетом регистра)

import sqlite3

# Функция по поиску заметок по ключевым словам в полях title и content
def search_notes_by_keyword(keyword, db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM notes
            WHERE title LIKE ? OR content LIKE ?""",
                   (f"%{keyword}%", f"%{keyword}%"))
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