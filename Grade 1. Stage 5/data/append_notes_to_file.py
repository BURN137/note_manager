# Предназначен для добавления новых заметок в конец файла.
# Название файла запрашивается у пользователя
# При вводе названия файла ищутся файлы с расширением yaml
# Для работы используется библиотеки datetime и yaml

# Обращаемся к библиотеке yaml для считывания из файла в формате YAML
import yaml

# Функция по добавлению заметок в существующий файл в структурированном формате
def append_notes_to_file(notes, filename):
    with open(filename, mode="a", encoding="utf-8") as file:
        yaml_notes = notes  # Создаем копию списка словарей для дальнейшей работы
        for index in range(len(yaml_notes)): # Преобразуем ключи словарей в понятный для пользователя вид
            yaml_notes[index]["Имя пользователя"] = yaml_notes[index].pop("username")
            yaml_notes[index]["Заголовок"] = yaml_notes[index].pop("title")
            yaml_notes[index]["Описание"] = yaml_notes[index].pop("content")
            yaml_notes[index]["Статус"] = yaml_notes[index].pop("status")
            yaml_notes[index]["Дата создания"] = yaml_notes[index].pop("created_date")
            yaml_notes[index]["Дедлайн"] = yaml_notes[index].pop("issue_date")
        yaml.dump(yaml_notes, file, allow_unicode=True, sort_keys=False)