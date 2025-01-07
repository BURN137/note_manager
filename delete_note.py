# Данный функционал предназначен для создания множества заметок с добавлением их в список в виде словаря
# После ввода заметок пользователю предлагается удалить не нужные заметки
# Выполняется проверка на пустой ввод и ввод корректного формата даты (ДД.ММ.ГГГГ)
# Для работы используется библиотека datetime
# Также для работы используются функции:
# note_func() - добавление новых заметок
# delete_note() - удаление заметок по Имени пользователя и Заголовку
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

# Вносим данные первой заметки в список
multiple_notes.append(note_func())

# Функционал для добавления новой заметки
while True:
    add_new_note = input("\nХотите добавить ещё одну заметку? (Да/Нет): ") # Запрос на необходимость добавления
    if add_new_note.lower() in ["нет"]:
        print("\nТекущий список заметок")
        for i in range(len(multiple_notes)): # Выводим на экран содержимое всех заметок
            print(f"\nЗаметка №{i + 1}",
                  f"\nИмя: {multiple_notes[i]["username"]}",
                  f"\nЗаголовок: {multiple_notes[i]["title"]}",
                  f"\nОписание: {multiple_notes[i]["content"]}",
                  f"\nСтатус: {multiple_notes[i]["status"]}",
                  f"\nДата создания: {multiple_notes[i]["created_date"]}",
                  f"\nДедлайн: {multiple_notes[i]["issue_date"]}")
        break
    elif add_new_note.lower() in ["да"]:
        multiple_notes.append(note_func()) # Добавление новой заметки в конец списка
        continue
    else:
        print('Введите "Да" или "Нет"') # Сообщение, если не верно введено Да или Нет
        continue

# Функция по удалению заметок
def delete_note(counter = 0): # Вводим счетчик удаленных словарей, чтобы вносить правки на проверяемый индекс в списке после удаления словаря
    length_multiple_notes = len(multiple_notes) # Фиксируем длину исходного списка, чтобы по ней понять удалены ли словари из списка
    del_element = input("Введите имя пользователя или заголовок для удаления заметки: ") # Запрашиваем наименование Имени или Заголовка, чтобы удалить
    del_element = del_element.lower().capitalize()
    while True:
        accept_del_element = input("Вы уверены, что хотите удалить заметку/и? (Да/Нет): ")  # Подтверждение на удаление заметок
        accept_del_element = accept_del_element.lower().capitalize()
        if accept_del_element.lower() in ["да"]:
            for k in range(len(multiple_notes)):
                try: # Отлавливаем ошибку изменения длины списка при удалении словаря
                    if del_element in [multiple_notes[k - counter]["username"], # Проверяем условие с поправкой на удаленные ранее словари
                                       multiple_notes[k - counter]["title"]]:
                        del multiple_notes[k - counter] # Удаляем словари с поправкой на ранее удаленные словари
                        counter += 1 # Увеличиваем счетчик удаленных словарей после каждого удаления
                except IndexError: # Действие, когда длина списка изменилась
                    continue
            if counter == 0:
                print("\nЗаметок с таким именем пользователя или заголовком не найдено")
            break
        elif accept_del_element.lower() in ["нет"]:
            print("\nСписок заметок не изменен!")
            for i in range(len(multiple_notes)):  # Выводим на экран содержимое всех заметок
                print(f"\nЗаметка №{i + 1}",
                      f"\nИмя: {multiple_notes[i]["username"]}",
                      f"\nЗаголовок: {multiple_notes[i]["title"]}",
                      f"\nОписание: {multiple_notes[i]["content"]}",
                      f"\nСтатус: {multiple_notes[i]["status"]}",
                      f"\nДата создания: {multiple_notes[i]["created_date"]}",
                      f"\nДедлайн: {multiple_notes[i]["issue_date"]}")
            break
        else:
            print('Введите "Да" или "Нет"')
            continue
    if len(multiple_notes) == 0: # Выводим сообщение, если удалены все заметки
        print("\nУдалены все заметки!")
    elif length_multiple_notes > len(multiple_notes): # Выводим все заметки после удаления не нужных
        print("\nУспешно удалено. Остались следующие заметки:")
        for j in range(len(multiple_notes)):
            print(f"\nЗаметка №{j + 1}",
                  f"\nИмя: {multiple_notes[j]["username"]}",
                  f"\nЗаголовок: {multiple_notes[j]["title"]}",
                  f"\nОписание: {multiple_notes[j]["content"]}",
                  f"\nСтатус: {multiple_notes[j]["status"]}",
                  f"\nДата создания: {multiple_notes[j]["created_date"]}",
                  f"\nДедлайн: {multiple_notes[j]["issue_date"]}")

# Функционал для удаления заметки по Имени пользователя и Заголовку
while True:
    del_note = input("\nХотите удалить заметку/и? (Да/Нет): ") # Запрашиваем нужно ли удалить заметку
    if del_note.lower() in ["да"]:
        delete_note()
    elif del_note.lower() in ["нет"]: # Выводим все заметки, если не требуется удалять не нужные
        print("\nСписок заметок не изменен!")
        for i in range(len(multiple_notes)): # Выводим на экран содержимое всех заметок
            print(f"\nЗаметка №{i + 1}",
                  f"\nИмя: {multiple_notes[i]["username"]}",
                  f"\nЗаголовок: {multiple_notes[i]["title"]}",
                  f"\nОписание: {multiple_notes[i]["content"]}",
                  f"\nСтатус: {multiple_notes[i]["status"]}",
                  f"\nДата создания: {multiple_notes[i]["created_date"]}",
                  f"\nДедлайн: {multiple_notes[i]["issue_date"]}")
        break
    else: # Выводим сообщение, если не корректно введены Да или Нет
        print('Введите "Да" или "Нет"')
        continue
    break