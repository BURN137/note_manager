# Предназначен для считывания заметки из файла и преобразования данных в словарь
# При вводе названия файла ищутся файлы с расширением yaml

# Обращаемся к библиотеке yaml для считывания из файла в формате YAML
import yaml

# Функция по считыванию заметки из файла и возвращению в виде словаря
def load_notes_from_file(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        notes = yaml.safe_load(file)
        for index in range(len(notes)): # Преобразуем ключи словарей
            notes[index]["username"] = notes[index].pop("Имя пользователя")
            notes[index]["title"] = notes[index].pop("Заголовок")
            notes[index]["content"] = notes[index].pop("Описание")
            notes[index]["status"] = notes[index].pop("Статус")
            notes[index]["created_date"] = notes[index].pop("Дата создания")
            notes[index]["issue_date"] = notes[index].pop("Дедлайн")
        print(f"\nИмпорт данных из файла {filename} выполнен")
    return notes