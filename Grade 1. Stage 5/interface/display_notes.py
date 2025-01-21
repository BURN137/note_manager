# Функция по выводу заметок в структурированном формате
def display_notes(notes):
    for i in range(len(notes)):  # Выводим на экран заметки отсортированные по дате
        print(f"\nid: {notes[i]["id"]}",
              f"\nИмя пользователя: {notes[i]["username"]}",
              f"\nЗаголовок: {notes[i]["title"]}",
              f"\nОписание: {notes[i]["content"]}",
              f"\nСтатус: {notes[i]["status"]}",
              f"\nДата создания: {notes[i]["created_date"]}",
              f"\nДедлайн: {notes[i]["issue_date"]}")
        print("-" * 25)