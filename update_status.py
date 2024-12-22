# Запрашиваем текущий статус заметки с приведением статусов к виду "Выполнено", "В процессе", "Отложено"
print("\nВозможные статусы заметки:"
          "\nВыполнено"
          "\nВ процессе"
          "\nОтложено")
status = input("Введите статус заметки: ")
while True:
    if status.lower() == "выполнено":
        status = status.lower().capitalize()
        print("\nТекущий статус заметки:", status)
        break
    elif status.lower() == "в процессе":
        status = status.lower().capitalize()
        print("\nТекущий статус заметки:", status)
        break
    elif status.lower() == "отложено":
        status = status.lower().capitalize()
        print("\nТекущий статус заметки:", status)
        break
    else:
        print("\nВозможные статусы заметки:"
              "\nВыполнено"
              "\nВ процессе"
              "\nОтложено")
        status = input("Введите корректно статус заметки: ")

# Смена статуса заметки при необходимости с приведением статусов к виду "Выполнено", "В процессе", "Отложено"
status_changes = input("Хотите изменить статус заметки? (Да/Нет):")
while True:
    if status_changes.lower() == "да":
        new_status = input("Введите новый статус заметки: ")
        if new_status.lower() == "выполнено":
            new_status = new_status.lower().capitalize()
            print("Статус заметки успешно обновлен на:", new_status)
            break
        elif new_status.lower() == "в процессе":
            new_status = new_status.lower().capitalize()
            print("Статус заметки успешно обновлен на:", new_status)
            break
        elif new_status.lower() == "отложено":
            new_status = new_status.lower().capitalize()
            print("Статус заметки успешно обновлен на:", new_status)
            break
        else:
            print("\nДанный статус отсутствует")
    elif status_changes.lower() == "нет":
        new_status = status
        print("Текущий статус заметки не изменен")
        break
    else:
        status_changes = input("Пожалуйста, введите 'Да' или 'Нет': ")

# Создание словаря и его вывод
status_ = {"status": new_status}
print(status_)