# Предназначен для считывания заметки из файла и преобразования данных в словарь
# При вводе названия файла ищутся файлы с расширением yaml
# Выполняется обработка ошибок
# - при отсутствии указанного файла,
# - поврежденного файла или файла с не верными данными
# - доступа к файлу

# Обращаемся к библиотеке yaml для считывания из файла в формате YAML
import yaml

# Функция по считыванию заметки из файла и возвращению в виде словаря
def load_notes_from_file(filename):
    file = open(filename, mode="r", encoding="utf-8")
    from_yaml_notes = yaml.safe_load(file)
    for index in range(len(from_yaml_notes)):  # Преобразуем ключи словарей
        from_yaml_notes[index]["username"] = from_yaml_notes[index].pop("Имя пользователя")
        from_yaml_notes[index]["title"] = from_yaml_notes[index].pop("Заголовок")
        from_yaml_notes[index]["content"] = from_yaml_notes[index].pop("Описание")
        from_yaml_notes[index]["status"] = from_yaml_notes[index].pop("Статус")
        from_yaml_notes[index]["created_date"] = from_yaml_notes[index].pop("Дата создания")
        from_yaml_notes[index]["issue_date"] = from_yaml_notes[index].pop("Дедлайн")
    file.close()

# Вызываем функцию
filename_ = input("Введите название файла yaml: ") + ".yaml"
try:
    load_notes_from_file(filename_)
except  FileNotFoundError:
    print(f"\nФайл {filename_} не найден. Создан новый пустой файл.")
    open(filename_, mode="x")
except UnicodeDecodeError:
    print(f"\nОшибка при чтении файла {filename_}. Проверьте его содержимое.")
except PermissionError:
    print(f"\nДоступ к файлу {filename_} запрещен.")