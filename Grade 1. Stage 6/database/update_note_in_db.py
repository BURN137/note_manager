# Обновление поля заметки в базе данных.
# Поле заметки и значение этого поля запрашиваются у пользователя.
# Имеется возможность внести правки в несколько полей одной заметки
# Для работы используется база с именем notes.db созданная ранее

import sqlite3

# Функция по загрузке из базы данных заметки указанной пользователем
def load_note_from_db(db_name, note_id):
    # Создаем подключение к базе данных
    connection = sqlite3.connect(f"./{db_name}")
    cursor = connection.cursor()
    # Импортируем указанную пользователем заметку из базы данных
    cursor.execute('SELECT * FROM notes')
    rows = cursor.fetchall()
    rows_len = len(rows)
    note = []
    for row in range(rows_len):
        if row == note_id - 1:
                note = {'title': rows[row][2],
                        'content': rows[row][3],
                        'status': rows[row][4],
                        'issue_date': rows[row][6]}
    connection.close()
    return rows_len, note

# Функция по обновлению данных в базе данных
def update_note_in_db(note_id, updates, db_name):
    # Создаем подключение к базе данных
    connection = sqlite3.connect(f"./{db_name}")
    cursor = connection.cursor()
    cursor.execute("""UPDATE notes
                       SET title = ?, content = ?, status = ?, issue_date = ?
                       WHERE id = ?""",
                   (updates['title'],
                    updates['content'],
                    updates['status'],
                    updates['issue_date'], note_id))
    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()

