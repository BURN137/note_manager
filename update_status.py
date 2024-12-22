# status = "Активна"  # Статус заметки
# выполнено
# в процессе
# отложено
print("\nВозможные статусы заметки:"
          "\n1. Выполнено"
          "\n2. В процессе"
          "\n3. Отложено")
status = input("Введите статус заметки (1/2/3): ")
while True:
    if status == "1":
        print("\nТекущий статус заметки: Выполнено")
        break
    elif status == "2":
        print("\nТекущий статус заметки: В процессе")
        break
    elif status == "3":
        print("\nТекущий статус заметки: Отложено")
        break
    else:
        print("\nВозможные статусы заметки:"
              "\n1. Выполнено"
              "\n2. В процессе"
              "\n3. Отложено")
        status = input("Введите корректно статус заметки (1/2/3): ")
status_changes = input("Хотите изменить статус заметки? (Да/Нет) ")
while True:
    if status_changes.lower() == "да":
        new_status = input("Введите новый статус заметки (1/2/3): ")
        if new_status == "1":
            print("Статус заметки успешно обновлен на: Выполнено")
            break
        elif new_status == "2":
            print("Статус заметки успешно обновлен на: В процессе")
            break
        elif new_status == "3":
            print("Статус заметки успешно обновлен на: Отложено")
            break
    elif status_changes.lower() == "нет":
        new_status = status
        print("Текущий статус заметки не изменен")
        break
    else:
        status_changes = input("Пожалуйста, введите 'Да' или 'Нет': ")
print({"status": new_status})