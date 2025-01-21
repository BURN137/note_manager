# Предназначен для проверки на корректность ввода даты

# Обращаемся к библиотеке datetime для работы с датами
import datetime

def validate_date(date):
    while True:
        try:  # Действие при правильном формате даты
            date = datetime.datetime.strptime(date,"%d.%m.%Y")  # Преобразование в тип datetime.datetime
            break
        except ValueError:  # Действие при неправильном формате даты
            print("\nВведена не существующая дата или не корректный формат!")
            date = input("Введите корректно дату: ")
            continue
    return date