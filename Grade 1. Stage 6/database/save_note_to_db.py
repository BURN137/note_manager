import sqlite3

# Функция для добавления заметок в базу данных
def save_note_to_db(notes, db_name):
    # Создаем подключение к базе данных
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    # Загружаем заметки в базу данных
    for note in notes:
        cursor.execute('''INSERT INTO notes (id, username, title, content, status, created_date, issue_date) 
                        VALUES (?, ?, ?, ?, ?, ?, ?)''',
                       (note['id'],
                        note['username'],
                        note['title'],
                        note['content'],
                        note['status'],
                        note['created_date'],
                        note['issue_date']))
    print("\nЗаметки успешно сохранены в базу данных")
    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()