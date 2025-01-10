# Обеспечивает пользователю работу с "Меню". Каждый пункт меню привязан к функции
# Для работы используется библиотека datetime

# Пункты Меню - функции
# 1. Создать новую заметку - create_note()
# 2. Показать все заметки - display_notes()
# 3. Обновить заметку - update_note()
# 4. Удалить заметку - delete_note()
# 5. Найти заметки - search_notes()
# 6. Выйти из программы

# Обращаемся к библиотеке datetime
import datetime

# Создаем пустой список для словарей заметок
notes = []

# Функция отображения Меню
def menu():
    while True:
        print("\nМеню:",
              "\n1. Создать новую заметку",
              "\n2. Показать все заметки",
              "\n3. Обновить заметку",
              "\n4. Удалить заметку",
              "\n5. Найти заметки",
              "\n6. Выйти из программы")
        item_menu = input("Укажите пункт меню: ")
        if int(item_menu) in range(1, 7):
            break
        elif int(item_menu) not in range(1, 7):
            print("\nНеверный выбор. Пожалуйста, выберите действие из списка.")
            continue
    return item_menu

# Функция по созданию новой заметки
def create_note():
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
        content = content.lower().capitalize()
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
    note_tuple = {"username": username, # Создаем словарь из данных заметки
            "title": title,
            "content": content,
            "status": status,
            "created_date": created_date_obj.date().strftime("%d.%m.%Y"),
            "issue_date": issue_date_obj.date().strftime("%d.%m.%Y")}
    return note_tuple

# Функция по выводу заметок в структурированном формате
def display_notes(notes):
    if len(notes) == 0:
        print("\nСписок заметок пуст")
    else:
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

# Функция по изменению заметки
def update_note(note):
    while True:
        if len(note) == 0:
            print("\nСписок заметок пуст")
            break
        else:
            request_update_number_note = input("Укажите номер заметки, которую необходимо изменить: ")
            if int(request_update_number_note) in range(1, len(note)+1):
                while True:
                    request_change_note = input("\nХотите изменить заметку? (Да/Нет): ")  # Запрос на изменение заметки
                    if request_change_note.lower() in ["да"]:
                        print("\nПоля заметки, которые можно изменить:",
                              "\nusername",
                              "\ntitle",
                              "\ncontent",
                              "\nstatus",
                              "\nissue_date")
                        while True:
                            update_key = input("Укажите изменяемое поле: ")
                            if update_key in ["username", "title", "content", "status", "issue_date"]:
                                while True:
                                    accept_update = input("Вы уверены, что хотите изменить заметку? (Да/Нет): ")  # Подтверждение на удаление заметок
                                    if accept_update.lower() in ["да"]:
                                        update_value = input(f"Введите новое значение для {update_key} "
                                                             f"или оставьте пустым, чтобы оставить без изменений: ")
                                        if update_value in [""]:
                                            print("\nЗаметка не изменена!")
                                        elif update_key in ["username", "title", "content"]:
                                            print("\nЗаметка обновлена")
                                            note[int(request_update_number_note)-1][update_key] = update_value.lower().capitalize()
                                        elif update_key in ["status"]:
                                            print("\nЗаметка обновлена")
                                            while True:
                                                if update_value.lower() in ["новая", "в процессе", "выполнено"]:
                                                    note[int(request_update_number_note)-1][update_key] = update_value.lower().capitalize()
                                                    break
                                                else:
                                                    print("\nВведите корректно статус заметки")
                                                    update_value = input(f"Введите новое значение для {update_key}: ")
                                                    continue
                                        elif update_key in ["issue_date"]:
                                            print("\nЗаметка обновлена")
                                            while True:
                                                try:
                                                    update_value = datetime.datetime.strptime(update_value,"%d.%m.%Y")  # Преобразование в тип datetime.datetime
                                                    note[int(request_update_number_note)-1][update_key] = update_value.date().strftime("%d.%m.%Y")
                                                    break
                                                except ValueError: # Действие при неправильном формате даты
                                                    print("\nВведена не существующая дата или не корректный формат!")
                                                    update_value = input(f"Введите новое значение для {update_key}: ")
                                                    continue
                                        break
                                    elif accept_update.lower() in ["нет"]:
                                        print("\nЗаметка не изменена!")
                                        break
                                    else:
                                        print('\nВведите "Да" или "Нет"')
                                        continue
                                break
                            else:
                                print("\nНе верно указано поле")
                                continue
                        break
                    elif request_change_note.lower() in ["нет"]:
                        print("\nЗаметка не изменена!")
                        break
                    else:
                        print('\nВведите "Да" или "Нет"')
                        continue
            elif int(request_update_number_note) != len(note):
                print("\nЗаметки с таким номером нет")
                continue
            break
    return note

# Функция по удалению заметок
def delete_note(note):
    counter = 0 # Вводим счетчик удаленных словарей, чтобы вносить правки на проверяемый индекс в списке после удаления словаря
    while True:
        if len(note) == 0:
            print("\nСписок заметок пуст")
            break
        else:
            length_notes = len(note) # Фиксируем длину исходного списка, чтобы по ней понять удалены ли словари из списка
            del_element = input("Введите имя пользователя или заголовок для удаления заметки: ") # Запрашиваем наименование Имени или Заголовка, чтобы удалить
            del_element = del_element.lower().capitalize()
            while True:
                accept_del_element = input("Вы уверены, что хотите удалить заметку/и? (Да/Нет): ")  # Подтверждение на удаление заметок
                accept_del_element = accept_del_element.lower().capitalize()
                if accept_del_element.lower() in ["да"]:
                    for k in range(len(note)):
                        try: # Отлавливаем ошибку изменения длины списка при удалении словаря
                            if del_element in [note[k - counter]["username"], # Проверяем условие с поправкой на удаленные ранее словари
                                               note[k - counter]["title"]]:
                                del note[k - counter] # Удаляем словари с поправкой на ранее удаленные словари
                                counter += 1 # Увеличиваем счетчик удаленных словарей после каждого удаления
                        except IndexError: # Действие, когда длина списка изменилась
                            continue
                    if counter == 0:
                        print("\nЗаметок с таким именем пользователя или заголовком не найдено")
                    break
                elif accept_del_element.lower() in ["нет"]:
                    print("\nСписок заметок не изменен!")
                    for i in range(len(note)):  # Выводим на экран содержимое всех заметок
                        print(f"\nЗаметка №{i + 1}",
                              f"\nИмя: {note[i]["username"]}",
                              f"\nЗаголовок: {note[i]["title"]}",
                              f"\nОписание: {note[i]["content"]}",
                              f"\nСтатус: {note[i]["status"]}",
                              f"\nДата создания: {note[i]["created_date"]}",
                              f"\nДедлайн: {note[i]["issue_date"]}")
                    break
                else:
                    print('Введите "Да" или "Нет"')
                    continue
            if len(note) == 0: # Выводим сообщение, если удалены все заметки
                print("\nУдалены все заметки!")
            elif length_notes > len(note): # Выводим все заметки после удаления не нужных
                print("\nУспешно удалено. Остались следующие заметки:")
                for j in range(len(note)):
                    print(f"\nЗаметка №{j + 1}",
                          f"\nИмя: {note[j]["username"]}",
                          f"\nЗаголовок: {note[j]["title"]}",
                          f"\nОписание: {note[j]["content"]}",
                          f"\nСтатус: {note[j]["status"]}",
                          f"\nДата создания: {note[j]["created_date"]}",
                          f"\nДедлайн: {note[j]["issue_date"]}")
            break
    return note

# Функция поиска:
# - по ключевому слову в полях title, content и username
# - по статусу
def search_notes(note, keyword=None, status=None):
    while True:
        if len(note) == 0:
            print("\nСписок заметок пуст")
            break
        else:
            counter = 0  # Счетчик для подсчета количества совпадений
            for i in range(len(notes)):
                if keyword == "" and status == "":
                    print("\nЗаметки, соответствующие запросу, не найдены")
                elif ((keyword.lower() in notes[i]["username"].lower()
                       or keyword.lower() in notes[i]["title"].lower()
                       or keyword.lower() in notes[i]["content"].lower())
                      and (status.lower() == notes[i]["status"].lower())):
                    counter += 1
                    print(f"\nЗаметка №{i + 1}",
                          f"\nИмя: {notes[i]["username"]}",
                          f"\nЗаголовок: {notes[i]["title"]}",
                          f"\nОписание: {notes[i]["content"]}",
                          f"\nСтатус: {notes[i]["status"]}",
                          f"\nДата создания: {notes[i]["created_date"]}",
                          f"\nДедлайн: {notes[i]["issue_date"]}")
                elif (keyword.lower() in notes[i]["username"].lower()
                      or keyword.lower() in notes[i]["title"].lower()
                      or keyword.lower() in notes[i]["content"].lower()
                      or status.lower() == notes[i]["status"].lower()):
                    counter += 1
                    print(f"\nЗаметка №{i + 1}",
                          f"\nИмя: {notes[i]["username"]}",
                          f"\nЗаголовок: {notes[i]["title"]}",
                          f"\nОписание: {notes[i]["content"]}",
                          f"\nСтатус: {notes[i]["status"]}",
                          f"\nДата создания: {notes[i]["created_date"]}",
                          f"\nДедлайн: {notes[i]["issue_date"]}")
            if (counter == 0) and (keyword != "" or status != ""):
                print("\nЗаметки, соответствующие запросу, не найдены")
            break
    return note

# Функционал по работе с Меню
while True:
    item_menu_ = menu()
    if int(item_menu_) == 1:
        notes.append(create_note())
        continue
    elif int(item_menu_) == 2:
        display_notes(notes)
        continue
    elif int(item_menu_) == 3:
        display_notes(notes)
        if len(notes) != 0:
            update_note(notes)
            continue
        continue
    elif int(item_menu_) == 4:
        display_notes(notes)
        delete_note(notes)
        continue
    elif int(item_menu_) == 5:
        if len(notes) == 0:
            display_notes(notes)
        else:
            print("\nВыполним поиск по ключевому слову (имя пользователя, заголовок и описание) и статусу")
            keyword_ = input("Введите ключевое слово или оставьте пустым: ")
            status_ = input("Введите статус или оставьте пустым: ")
            search_notes(notes, keyword_, status_)
        continue
    elif int(item_menu_) == 6:
        print("\nПрограмма завершена. Спасибо за использование!")
        break