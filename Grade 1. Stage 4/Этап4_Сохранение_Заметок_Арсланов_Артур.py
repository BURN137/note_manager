# Предназначен для сохранения заметок в файл YAML. Название файла запрашивается у пользователя
# Для работы используется библиотека datetime и yaml

# Обращаемся к библиотеке datetime для работы с датами
import datetime

# Обращаемся к библиотеке yaml для сохранения в файл в формате YAML
import yaml

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

# Функция по сохранению заметок в файл в структурированном формате
def save_notes_to_file(notes, filename):
    yaml_notes = notes # Создаем копию списка словарей для дальнейшей работы
    for index in range(len(yaml_notes)): # Преобразуем ключи словарей в понятный для пользователя вид
        yaml_notes[index]["Имя пользователя"] = yaml_notes[index].pop("username")
        yaml_notes[index]["Заголовок"] = yaml_notes[index].pop("title")
        yaml_notes[index]["Описание"] = yaml_notes[index].pop("content")
        yaml_notes[index]["Статус"] = yaml_notes[index].pop("status")
        yaml_notes[index]["Дата создания"] = yaml_notes[index].pop("created_date")
        yaml_notes[index]["Дедлайн"] = yaml_notes[index].pop("issue_date")
    file = open(filename, mode="w", encoding="utf-8")
    yaml.dump(yaml_notes, file, allow_unicode=True, sort_keys=False)
    file.close()

# Создаем первую заметку и добавляем в список
notes_list = [create_note()]

# Запрашиваем необходимость добавления новой заметки
while True:
    add_new_note = input("\nХотите добавить ещё одну заметку? (Да/Нет): ")
    if add_new_note.lower() == "нет":
        break
    elif add_new_note.lower() == "да":
        notes_list.append(create_note())
        continue
    else:
        print('Введите "Да" или "Нет"')
        continue

# Сохраняем созданные заметки в файл YAML
while True:
    request_create_file = input("Вы хотите сохранить в файл? (Да/Нет): ")
    if request_create_file.lower() == "да":
        filename_ = input("Введите название файла: ") + ".yaml"
        save_notes_to_file(notes_list, filename_)
        break
    elif request_create_file.lower() == "нет":
        print('Файл не создан')
        break
    else:
        print('Введите "Да" или "Нет"')
        continue