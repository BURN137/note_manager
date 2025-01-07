# Данный функционал предназначен для создания множества заметок с добавлением их в список в виде словаря
# Выполняется проверка на пустой ввод и ввод корректного формата даты (ДД.ММ.ГГГГ)
# Для работы используется библиотека datetime
# Также для работы используется функция (note_func)
# Вводимый текст не чувствителен к регистру

# Обращаемся к библиотеке datetime
import datetime

# Приветствие пользователя
print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')

# Функция по созданию новой заметки
def note_func():
    while True: # Цикл для проверки пустого имени пользователя
        username = input("\nВведите имя пользователя: ") # Запрос на ввод имени пользователя
        if username != "": # Проверка ввода пустого имени пользователя
            username = username.lower().capitalize()
            break # Остановка цикла
        else:
            print("\nИмя пользователя не может быть пустым") # Вывод сообщения если имя пользователя пустое
            continue # Перезапуск цикла
    while True: # Цикл для проверки пустого заголовка заметки
        title = input("Введите заголовок заметки: ") # Запрос на ввод заголовка
        if title != "": # Проверка ввода пустого заголовка
            title = title.lower().capitalize()
            break # Остановка цикла
        else:
            print("\nЗаголовок не может быть пустым") # Вывод сообщения если заголовок пустой
            continue # Перезапуск цикла
    while True: # Цикл для проверки пустого описания заметки
        content = input("Введите описание заметки: ")  # Запрос на ввод описания заметки
        if content != "":  # Проверка ввода пустого описания
            break  # Остановка цикла
        else:
            print("\nОписание не может быть пустым")  # Вывод сообщения если описание пустое
            continue  # Перезапуск цикла
    while True: # Цикл для проверки корректного ввода статуса заметки
        status = input("Введите статус заметки (Новая, В процессе, Выполнено): ")
        if status.lower() in ["новая", "в процессе", "выполнено"]:
            status = status.lower().capitalize()
            break
        else:
            print("\nВведите корректно статус заметки")
    while True: # Цикл для проверки корректного ввода даты создания заметки
        created_date = input("Введите дату создания заметки (ДД.ММ.ГГГГ): ")
        try:  # Действие при правильном формате даты
            created_date_obj = datetime.datetime.strptime(created_date, "%d.%m.%Y")  # Преобразование в тип datetime.datetime
            break
        except ValueError:  # Действие при неправильном формате даты
            print("\nВведена не существующая дата или не корректный формат!")
    while True: # Цикл для проверки корректного ввода даты дедлайна заметки
        issue_date = input("Введите дату истечения заметки (ДД.ММ.ГГГГ): ")
        try:  # Действие при правильном формате даты
            issue_date_obj = datetime.datetime.strptime(issue_date, "%d.%m.%Y")  # Преобразование в тип datetime.datetime
            break
        except ValueError:  # Действие при неправильном формате даты
            print("\nВведена не существующая дата или не корректный формат!")
    note = {"username": username, # Создаем словарь из данных заметки
            "title": title,
            "content": content,
            "status": status,
            "created_date": created_date_obj.date().strftime("%d.%m.%Y"),
            "issue_date": issue_date_obj.date().strftime("%d.%m.%Y")}
    return note

# Создаем пустой список для словарей заметок
multiple_notes = []

# Вносим данные первой заметки в словарь
multiple_notes.append(note_func())

# Запрашиваем необходимость добавления новой заметки
while True:
    add_new_note = input("\nХотите добавить ещё одну заметку? (Да/Нет): ")
    if add_new_note.lower() in ["нет"]:
        for i in range(len(multiple_notes)): # Выводим на экран содержимое всех заметок
            print(f"\nЗаметка №{i+1}",
                  f"\nИмя: {multiple_notes[i]["username"]}",
                  f"\nЗаголовок: {multiple_notes[i]["title"]}",
                  f"\nОписание: {multiple_notes[i]["content"]}",
                  f"\nСтатус: {multiple_notes[i]["status"]}",
                  f"\nДата создания: {multiple_notes[i]["created_date"]}",
                  f"\nДедлайн: {multiple_notes[i]["issue_date"]}")
        break
    elif add_new_note.lower() in ["да"]:
        multiple_notes.append(note_func())
        continue
    else:
        print('Введите "Да" или "Нет"')
        continue