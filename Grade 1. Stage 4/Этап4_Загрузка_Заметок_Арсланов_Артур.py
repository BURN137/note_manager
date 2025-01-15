# Предназначен для считывания заметки из файла и преобразования данных в словарь
# При вводе названия файла ищутся файлы с расширением yaml

# Обращаемся к библиотеке yaml для считывания из файла в формате YAML
import yaml

# Функция по считыванию заметки из файла и возвращению в виде словаря
def load_notes_from_file(filename):
    file = open(filename, mode="r", encoding="utf-8")
    from_yaml_notes = yaml.safe_load(file)
    for index in range(len(from_yaml_notes)): # Преобразуем ключи словарей
        from_yaml_notes[index]["username"] = from_yaml_notes[index].pop("Имя пользователя")
        from_yaml_notes[index]["title"] = from_yaml_notes[index].pop("Заголовок")
        from_yaml_notes[index]["content"] = from_yaml_notes[index].pop("Описание")
        from_yaml_notes[index]["status"] = from_yaml_notes[index].pop("Статус")
        from_yaml_notes[index]["created_date"] = from_yaml_notes[index].pop("Дата создания")
        from_yaml_notes[index]["issue_date"] = from_yaml_notes[index].pop("Дедлайн")
    print(from_yaml_notes)
    file.close()

# Вызываем функцию
while True:
    filename_ = input("Введите название файла yaml: ") + ".yaml"
    try:
        load_notes_from_file(filename_)
        break
    except  FileNotFoundError:
        print("\nФайла с таким именем в папке нет")