# Предназначен для проверки на корректность ввода статуса

def validate_status(status):
    while True:
        if status.lower() in ["новая", "в процессе", "выполнено"]:
            status = status.lower().capitalize()
            break
        else:
            status = input("\nВведите корректно статус заметки: ")
    return status