# Предназначен для создания заметок
# Для работы используется библиотека datetime

# Подключаем модуль для проверки корректности ввода даты
import utils

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
    status = utils.validate_status(input("Введите статус заметки (Новая, В процессе, Выполнено): "))
    created_date = utils.validate_date(input("Введите дату создания заметки (ДД.ММ.ГГГГ): "))
    issue_date = utils.validate_date(input("Введите дату истечения заметки (ДД.ММ.ГГГГ): "))
    # Создаем словарь из данных заметки
    note = {"id": utils.generate_unique_id(),
            "username": username,
            "title": title,
            "content": content,
            "status": status,
            "created_date": created_date.date().strftime("%d.%m.%Y"),
            "issue_date": issue_date.date().strftime("%d.%m.%Y")}
    return note