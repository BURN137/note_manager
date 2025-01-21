# Обращаемся к модулям
import interface, data

notes = []
# Функционал по работе с Меню
while True:
    item_menu_ = interface.menu()
    if int(item_menu_) == 1: # Создаем заметки
        notes.append(data.create_note())
        while True:
            request_new_note = input("\nХотите добавить ещё одну заметку? (Да/Нет): ")
            if request_new_note.lower() == "нет":
                break
            elif request_new_note.lower() == "да":
                notes.append(data.create_note())
                continue
            else:
                print('Введите "Да" или "Нет"')
                continue
        continue
    elif int(item_menu_) == 2: # Отображаем созданные заметки
        if len(notes) == 0:
            print("\nСписок заметок пуст")
            continue
        else:
            interface.display_notes(notes)
        continue
    elif int(item_menu_) == 3: # Сохраняем созданные заметки в файл YAML
        while True:
            request_create_file = input("Вы хотите сохранить в файл YAML? (Да/Нет): ")
            if request_create_file.lower() == "да":
                filename_ = input("Введите название файла: ") + ".yaml"
                data.save_notes_to_file(notes, filename_)
                print(f"\nФайл {filename_} создан")
                break
            elif request_create_file.lower() == "нет":
                print('Файл YAML не создан')
                break
            else:
                print('Введите "Да" или "Нет"')
                continue
        continue
    elif int(item_menu_) == 4: # Импортируем заметки из существующего файла
        filename_ = input("Введите название файла YAML: ") + ".yaml"
        try:
            notes = data.load_notes_from_file(filename_).copy()
        except  FileNotFoundError:
            print(f"\nФайл {filename_} не найден.")
        except UnicodeDecodeError:
            print(f"\nОшибка при чтении файла {filename_}. Проверьте его содержимое.")
        except PermissionError:
            print(f"\nДоступ к файлу {filename_} запрещен.")
    elif int(item_menu_) == 5: # Добавляем новые заметки в существующий файл YAML
        while True:
            request_append_new_note = input(f"\nХотите добавить новые заметки в файл YAML? (Да/Нет): ")
            if request_append_new_note.lower() == "да":
                filename_ = input("Введите название существующего файла YAML: ") + ".yaml"
                try:
                    file = open(filename_, mode="r", encoding="utf-8")
                    file.close()
                    data.append_notes_to_file(notes, filename_)
                    print(f"\nЗаметки добавлены в файл {filename_}")
                except  FileNotFoundError:
                    print(f"\nФайл {filename_} не найден. Создан новый файл.")
                    open(filename_, mode="x")
                    data.append_notes_to_file(notes, filename_)
                except UnicodeDecodeError:
                    print(f"\nОшибка при чтении файла {filename_}. Проверьте его содержимое.")
                except PermissionError:
                    print(f"\nДоступ к файлу {filename_} запрещен.")
                break
            elif request_append_new_note.lower() == "нет":
                print('Файл не создан')
                break
            else:
                print('Введите "Да" или "Нет"')
                continue
        continue
    elif int(item_menu_) == 6:
        while True:  # Сохраняем созданные заметки в файл JSON
            request_create_file = input("Вы хотите сохранить в файл JSON? (Да/Нет): ")
            if request_create_file.lower() == "да":
                filename_ = input("Введите название файла: ") + ".json"
                data.save_notes_json(notes, filename_)
                print(f"\nФайл {filename_} создан")
                break
            elif request_create_file.lower() == "нет":
                print('Файл JSON не создан')
                break
            else:
                print('Введите "Да" или "Нет"')
                continue
        continue
    elif int(item_menu_) == 7:
        print("\nПрограмма завершена. Спасибо за использование!")
        break