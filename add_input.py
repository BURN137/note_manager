# Запрашиваемая информация у пользователя
username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки ('Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'ДД.ММ.ГГГГ': ")
issue_date = input("Введите дату истечения заметки в формате 'ДД.ММ.ГГГГ': ")

# Выводим все данные заметки
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date[:5:]) # Вывод даты без года
print("Дата истечения заметки:", issue_date[:5:]) # Вывод даты без года