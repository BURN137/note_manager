# Запрашиваемая информация у пользователя
username = input("Введите имя пользователя: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки ('Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'ДД.ММ.ГГГГ': ")
issue_date = input("Введите дату истечения заметки в формате 'ДД.ММ.ГГГГ': ")

# Запрашиваем несколько заголовков и добавляем их в список
title1 = input("Введите первый заголовок заметки: ")
title2 = input("Введите второй заголовок заметки: ")
title3 = input("Введите третий заголовок заметки: ")
titles = [title1, title2, title3]

# Создаем список для хранения информации о заметке, даты без года
note = {"username": username,
        "content": content,
        "status": status,
        "created_date": created_date[:5:],
        "issue_date": issue_date[:5:],
        "titles": titles}

# Выводим все данные заметки списком
print(note)