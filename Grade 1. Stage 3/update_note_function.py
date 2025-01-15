# Данный функционал предназначен для создания заметки с использованием функции:
# create_note() - функция по созданию новой заметки
# Выполняется проверка на пустой ввод и ввод корректного формата даты (ДД.ММ.ГГГГ)
# Для работы используется библиотека datetime
# Вводимый текст не чувствителен к регистру


# Обращаемся к библиотеке datetime
import datetime

# Создадим переменную для автоматического присвоения срока истечения заметки после создания заметки
delta = 7

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
    created_date = datetime.datetime.today().date().strftime("%d.%m.%Y") # Присвоение текущей даты создания заметки
    print(f"Дата создания заметки: {created_date}")
    issue_date = (datetime.datetime.today().date() + # Автоматический расчет срока истечения заметки
                  datetime.timedelta(days = delta)).strftime("%d.%m.%Y")
    print(f"Дата истечения заметки: {issue_date}")
    note = {"username": username, # Создаем словарь из данных заметки
            "title": title,
            "content": content,
            "status": status,
            "created_date": created_date,
            "issue_date": issue_date}
    return note

# Функция по изменению заметки
def update_note(note):
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
                                note[update_key] = update_value.lower().capitalize()
                            elif update_key in ["status"]:
                                print("\nЗаметка обновлена")
                                while True:
                                    if update_value.lower() in ["новая", "в процессе", "выполнено"]:
                                        note[update_key] = update_value.lower().capitalize()
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
                                        note[update_key] = update_value.date().strftime("%d.%m.%Y")
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
    return note

# Вызываем функцию create_note() и выводим на экран введенные данные заметки в виде словаря
note_ = create_note()
print(note_)

# Выводим на экран измененный словарь
print(update_note(note_))








