# Предназначен для создания и сохранения заметок в файл JSON.
# Название файла запрашивается у пользователя
# Для работы используется библиотека datetime и json

# Обращаемся к библиотеке datetime
import datetime

# Обращаемся к библиотеке datetime
import json

# Функция по созданию новой заметки
def create_note():
    while True:  # Цикл для проверки пустого имени пользователя
        username = input("\nВведите имя пользователя: ")  # Запрос на ввод имени пользователя
        if username != "":  # Проверка ввода пустого имени пользователя
            username = username.lower().capitalize()
            break  # Остановка цикла
        else:
            print("\nИмя пользователя не может быть пустым")  # Вывод сообщения если имя пользователя пустое
            continue  # Перезапуск цикла
    while True:  # Цикл для проверки пустого заголовка заметки
        title = input("Введите заголовок заметки: ")  # Запрос на ввод заголовка
        if title != "":  # Проверка ввода пустого заголовка
            title = title.lower().capitalize()
            break  # Остановка цикла
        else:
            print("\nЗаголовок не может быть пустым")  # Вывод сообщения если заголовок пустой
            continue  # Перезапуск цикла
    while True:  # Цикл для проверки пустого описания заметки
        content = input("Введите описание заметки: ")  # Запрос на ввод описания заметки
        if content != "":  # Проверка ввода пустого описания
            content = content.lower().capitalize()
            break  # Остановка цикла
        else:
            print("\nОписание не может быть пустым")  # Вывод сообщения если описание пустое
            continue  # Перезапуск цикла
    while True:  # Цикл для проверки корректного ввода статуса заметки
        status = input("Введите статус заметки (Новая, В процессе, Выполнено): ")
        if status.lower() in ["новая", "в процессе", "выполнено"]:
            status = status.lower().capitalize()
            break
        else:
            print("\nВведите корректно статус заметки")
    while True:  # Цикл для проверки корректного ввода даты создания заметки
        created_date = input("Введите дату создания заметки (ДД.ММ.ГГГГ): ")
        try:  # Действие при правильном формате даты
            created_date_obj = datetime.datetime.strptime(created_date,
                                                          "%d.%m.%Y")  # Преобразование в тип datetime.datetime
            break
        except ValueError:  # Действие при неправильном формате даты
            print("\nВведена не существующая дата или не корректный формат!")
    while True:  # Цикл для проверки корректного ввода даты дедлайна заметки
        issue_date = input("Введите дату истечения заметки (ДД.ММ.ГГГГ): ")
        try:  # Действие при правильном формате даты
            issue_date_obj = datetime.datetime.strptime(issue_date,
                                                        "%d.%m.%Y")  # Преобразование в тип datetime.datetime
            break
        except ValueError:  # Действие при неправильном формате даты
            print("\nВведена не существующая дата или не корректный формат!")
    note = {"username": username,  # Создаем словарь из данных заметки
            "title": title,
            "content": content,
            "status": status,
            "created_date": created_date_obj.date().strftime("%d.%m.%Y"),
            "issue_date": issue_date_obj.date().strftime("%d.%m.%Y")}
    return note

# Функция по созданию заметок в формате JSON
def save_notes_json(notes, filename):
    file = open(filename, mode="w", encoding="utf-8")
    json.dump(notes, file, indent=4, ensure_ascii=False)
    file.close()

# Создаем первую заметку и добавляем в список
notes_list = [create_note()]

# Запрашиваем необходимость добавления новой заметки
while True:
    add_new_note = input("\nХотите добавить ещё одну заметку? (Да/Нет): ")
    if add_new_note.lower() in ["нет"]:
        break
    elif add_new_note.lower() in ["да"]:
        notes_list.append(create_note())
        continue
    else:
        print('Введите "Да" или "Нет"')
        continue

# Сохраняем созданные заметки в файл
while True:
    request_create_file = input("Вы хотите сохранить в файл JSON? (Да/Нет): ")
    if request_create_file.lower() == "да":
        filename_ = input("Введите название файла: ") + ".json"
        save_notes_json(notes_list, filename_)
        break
    elif request_create_file.lower() == "нет":
        print('Файл не создан')
        break
    else:
        print('Введите "Да" или "Нет"')
        continue
