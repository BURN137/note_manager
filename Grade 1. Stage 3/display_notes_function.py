# Данный функционал предназначен для создания множества заметок с добавлением их в список в виде словаря
# Выполняется проверка на пустой ввод
# Для работы используется библиотека datetime
# Также для работы используются функции:
# note_func() - добавление новых заметок
# display_notes(notes) - отображение списка заметок в структурированном виде
#
# При необходимости выводится заметки в полном и кратком виде
# Имеется возможность отсортировать списки по дате создания и дате дедлайна
# Вводимый текст не чувствителен к регистру
# Используются библиотеки: datetime и colorama

# Обращаемся к библиотеке datetime
import datetime

# Обращаемся к библиотеке colorama
# import colorama

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
            content = content.lower().capitalize()
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
    while True:  # Цикл для проверки корректного ввода даты создания заметки
        created_date = input("Введите дату создания заметки (ДД.ММ.ГГГГ): ")
        try:  # Действие при правильном формате даты
            created_date_obj = datetime.datetime.strptime(created_date,"%d.%m.%Y")  # Преобразование в тип datetime.datetime
            break
        except ValueError:  # Действие при неправильном формате даты
            print("\nВведена не существующая дата или не корректный формат!")
    while True:  # Цикл для проверки корректного ввода даты дедлайна заметки
        issue_date = input("Введите дату истечения заметки (ДД.ММ.ГГГГ): ")
        try:  # Действие при правильном формате даты
            issue_date_obj = datetime.datetime.strptime(issue_date,"%d.%m.%Y")  # Преобразование в тип datetime.datetime
            break
        except ValueError:  # Действие при неправильном формате даты
            print("\nВведена не существующая дата или не корректный формат!")
    note = {"username": username, # Создаем словарь из данных заметки
            "title": title,
            "content": content,
            "status": status,
            "created_date": created_date,
            "issue_date": issue_date}
    return note

# Создаем пустой список для словарей заметок
multiple_notes = []

# Вносим данные первой заметки в список
multiple_notes.append(note_func())

# Функция по выводу заметок в структурированном формате
def display_notes(notes):
    while True:
        request = input("Заметки вывести в кратком или полном виде? (Краткий/Полный): ")
        if request.lower() in ["полный"]:
            while True:
                request = input("Сортировать по дате перед выводом на экран? (Да/Нет): ")
                if request.lower() in ["да"]:
                    while True: # Функционал по сортировке списка по дате создания или дедлайна
                        sort_request = input("По какой дате сортировать? (Создание/Дедлайн): ")
                        if sort_request.lower() in ["создание"]: # Сортируем список по дате создания
                            sort_notes = sorted(notes, key=lambda x: x["created_date"])
                            break
                        elif sort_request.lower() in ["дедлайн"]: # Сортируем список по дате дедлайна
                            sort_notes = sorted(notes, key=lambda x: x["issue_date"])
                            break
                        else:
                            print('Введите "Создание" или "Дедлайн"')  # Сообщение, если не верно введено Создание или Дедлайн
                            continue
                    print("\nСортированный список заметок")
                    print("-" * 25)
                    for i in range(len(sort_notes)):  # Выводим на экран заметки отсортированные по дате
                        print(f"\nЗаметка №{i + 1}",
                              f"\nИмя пользователя: {sort_notes[i]["username"]}",
                              f"\nЗаголовок: {sort_notes[i]["title"]}",
                              f"\nОписание: {sort_notes[i]["content"]}",
                              f"\nСтатус: {sort_notes[i]["status"]}",
                              f"\nДата создания: {sort_notes[i]["created_date"]}",
                              f"\nДедлайн: {sort_notes[i]["issue_date"]}")
                        print("-" * 25)
                    break
                elif request.lower() in ["нет"]:
                    print("\nТекущий список заметок")
                    print("-" * 25)
                    for i in range(len(notes)):  # Выводим на экран заметки отсортированные по дате
                        print(f"\nЗаметка №{i + 1}",
                              f"\nИмя пользователя: {notes[i]["username"]}",
                              f"\nЗаголовок: {notes[i]["title"]}",
                              f"\nОписание: {notes[i]["content"]}",
                              f"\nСтатус: {notes[i]["status"]}",
                              f"\nДата создания: {notes[i]["created_date"]}",
                              f"\nДедлайн: {notes[i]["issue_date"]}")
                        print("-" * 25)
                    break
                else:
                    print('Введите "Да" или "Нет"')  # Сообщение, если не верно введено Да или Нет
                    continue
            break
        elif request.lower() in ["краткий"]:
            print("\nТекущий список заметок")
            print("-" * 25)
            for i in range(len(notes)):  # Выводим на экран содержимое всех заметок
                print(f"\nЗаметка №{i + 1}",
                      f"\nЗаголовок: {notes[i]["title"]}")
                print("-" * 25)
            break
        else:
            print('Введите "Краткий" или "Полный"')  # Сообщение, если не верно введено Краткий или Полный

# Функционал для добавления новой заметки
while True:
    add_new_note = input("\nХотите добавить ещё одну заметку? (Да/Нет): ") # Запрос на необходимость добавления
    if add_new_note.lower() in ["нет"]:
        display_notes(multiple_notes)
        break
    elif add_new_note.lower() in ["да"]:
        multiple_notes.append(note_func()) # Добавление новой заметки в конец списка
        continue
    else:
        print('Введите "Да" или "Нет"') # Сообщение, если не верно введено Да или Нет
        continue