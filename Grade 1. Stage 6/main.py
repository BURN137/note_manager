# Пункты меню выбираются последовательно по порядку
import database, datetime, copy

# Имя файла базы данных по умолчанию
db_name = "notes.db"

# Список заметок для загрузки в базу данных
note_dict = [{"id": 1,
          "username": "Артур",
          "title": "Покупка",
          "content": "Продукты на вечер",
          "status": "Новая",
          "created_date": "05.01.2025",
          "issue_date": "10.01.2025"},
             {"id": 2,
              "username": "Денис",
              "title": "Кредит",
              "content": "Оплатить кредит",
              "status": "Выполнено",
              "created_date": "06.01.2025",
              "issue_date": "17.01.2025"}]

while True:
    print("\nМеню:",
          "\n1. Создать базу данных SQLite",
          "\n2. Сохранить заметки в базу данных",
          "\n3. Загрузить заметки из базы данных",
          "\n4. Обновить заметки в базе данных",
          "\n5. Удалить заметку из базы данных",
          "\n6. Поиск заметки по ключевому слову в полях 'Заголовок' и 'Описание'",
          "\n7. Фильтрация по статусу",
          "\n8. Завершить работу с базой данных")
    menu_item = input("Укажите пункт меню: ")
    if menu_item == "1":
        database.setup_database(db_name)
        print(f"\nБаза данных {db_name} успешно создана")
    elif menu_item == "2":
        database.save_note_to_db(note_dict, db_name)
    elif menu_item == "3":
        print(database.load_notes_from_db(db_name))
    elif menu_item == "4":
        while True: # Запрашиваем номер заметки, чтобы в ней изменить поля
            note_id_ = int(input("Укажите номер заметки, которую хотите изменить: "))
            if database.load_note_from_db("notes.db", note_id_)[0] < int(note_id_):
                print("Заметки с таким номером нет в базе данных")
            else:
                update_note = copy.deepcopy(database.load_note_from_db("notes.db", note_id_)[1])
                break
        while True: # Запрашиваем поле заметки и новое значение для указанного поля
            print("\nПоля заметки, которые можно изменить:",
                  "\ntitle",
                  "\ncontent",
                  "\nstatus",
                  "\nissue_date")
            update_key = input("Укажите изменяемое поле или оставьте пустым, чтобы оставить закончить правки: ")
            if update_key == "":
                print("Внесение правок завершено")
                break
            elif update_key in ["title", "content", "status", "issue_date"]:
                while True:
                    accept_update = input(
                        "Вы уверены, что хотите изменить заметку? (Да/Нет): ")  # Подтверждение на изменение заметки
                    if accept_update.lower() == "да":
                        update_value = input(f"Введите новое значение для {update_key} "
                                             f"или оставьте пустым, чтобы оставить без изменений: ")
                        if update_value == "":
                            print("\nЗаметка в базе данных не изменена")
                            break
                        elif update_key in ["title", "content"]:
                            update_note[update_key] = update_value.lower().capitalize()
                        elif update_key == "status":
                            while True:
                                if update_value.lower() in ["новая", "в процессе", "выполнено"]:
                                    update_note[update_key] = update_value.lower().capitalize()
                                    break
                                else:
                                    print('\nВведите корректно статус заметки "Новая", "В процессе", "Выполнено"')
                                    update_value = input(f"Введите новое значение для {update_key}: ")
                        elif update_key == "issue_date":
                            while True:
                                try:
                                    update_value = datetime.datetime.strptime(update_value,
                                                                              "%d.%m.%Y")  # Преобразование в тип datetime.datetime
                                    update_note[update_key] = update_value.date().strftime("%d.%m.%Y")
                                    break
                                except ValueError:  # Действие при неправильном формате даты
                                    print("\nВведена не существующая дата или не корректный формат!")
                                    update_value = input(f"Введите новое значение для {update_key}: ")
                        break
                    elif accept_update.lower() == "нет":
                        print("\nЗаметка в базе данных не изменена")
                        break
                    else:
                        print('\nВведите "Да" или "Нет"')
            else:
                print("\nНе верно указано поле")
        database.update_note_in_db(note_id_, update_note, db_name) # Вносим изменения заметки в базу данных
    elif menu_item == "5":
        while True: # Запрашиваем номер заметки, чтобы ее удалить
            note_id_ = input("Укажите номер заметки, которую хотите удалить: ")
            if database.quantity_rows_in_db(db_name) < int(note_id_):
                print(f"\nЗаметки с №{note_id_} нет в базе данных")
            else:
                database.delete_note_from_db(note_id_, db_name)
                print(f"Заметка №{note_id_} успешно удалена из базы данных")
                break
    elif menu_item == "6":
        keyword_ = input("Введите ключевое слово для поиска в полях 'Заголовок' и 'Описание': ")
        search_notes = database.search_notes_by_keyword(keyword_, db_name)
        if len(search_notes) == 0:
            print(f"Заметок с ключевым словом '{keyword_}' нет")
        else:
            print(search_notes)
    elif menu_item == "7":
        status_ = input("Введите статус заметок: ").lower().capitalize()
        filter_notes = database.filter_notes_by_status(status_, db_name)
        if len(filter_notes) == 0:
            print(f"Заметки со статусом {status_} не найдены")
        else:
            print(filter_notes)
    elif menu_item == "8":
        print("\nРабота с базой данных закончена")
        break