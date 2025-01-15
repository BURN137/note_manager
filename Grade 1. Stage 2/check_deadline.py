# Данный функционал предназначен для проверки пропущенных дедлайнов
# Используется встроенная библиотека datetime

# Выводим текущую дату в формате ДД.ММ.ГГГГ
import datetime
print("Текущая дата:", datetime.datetime.today().date().strftime("%d.%m.%Y"))

# Запрос даты дедлайна в формате ДД.ММ.ГГГГ с обработкой ошибки при неправильном введенном формата
while True:
    issue_date = input("Введите дату дедлайна в формате ДД.ММ.ГГГГ: ") # Запрашиваем дату дедлайна
    try: # Действие при правильном формате даты
        issue_date_obj = datetime.datetime.strptime(issue_date, "%d.%m.%Y") # Преобразование в тип datetime.datetime
        if issue_date_obj.date() > datetime.datetime.today().date(): # Вывод сообщения при не наступлении дедлайна
            deadline = issue_date_obj.date() - datetime.datetime.today().date()
            if int(deadline.days) % 100 in range(5, 21):
                print(f"До дедлайна осталось {deadline.days} дней")
            elif int(deadline.days) % 10 == 1:
                print(f"До дедлайна остался {deadline.days} день")
            elif int(deadline.days) % 10 in range(2, 5):
                print(f"До дедлайна осталось {deadline.days} дня")
            else:
                print(f"До дедлайна осталось {deadline.days} дней")
        elif issue_date_obj.date() < datetime.datetime.today().date(): # Вывод сообщения при наступлении дедлайна
            deadline = datetime.datetime.today().date() - issue_date_obj.date()
            if int(deadline.days) % 100 in range(5, 21):
                print(f"Внимание! Дедлайн истек {deadline.days} дней назад")
            elif int(deadline.days) % 10 == 1:
                print(f"Внимание! Дедлайн истек {deadline.days} день назад")
            elif int(deadline.days) % 10 in range(2, 5):
                print(f"Внимание! Дедлайн истек {deadline.days} дня назад")
            else:
                print(f"Внимание! Дедлайн истек {deadline.days} дней назад")
        else:
            print("Дедлайн сегодня!") # Вывод сообщения при совпадении текущей даты с дедлайном
        break
    except ValueError: # Действие при неправильном формате даты
        print("\nВведена не существующая дата или не корректный формат!")