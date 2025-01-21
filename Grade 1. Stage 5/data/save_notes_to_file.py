# Предназначен для сохранения заметок в файл YAML. Название файла запрашивается у пользователя
# Для работы используется библиотека yaml

# Обращаемся к библиотеке yaml для сохранения в файл в формате YAML
import yaml

# Обращаемся к библиотеке copy для создания копии списка словарей
import copy

# Функция по сохранению заметок в файл в структурированном формате
def save_notes_to_file(notes, filename):
    yaml_notes = copy.deepcopy(notes) # Создаем копию списка словарей для дальнейшей работы
    for index in range(len(yaml_notes)): # Преобразуем ключи словарей в понятный для пользователя вид
        yaml_notes[index]["Имя пользователя"] = yaml_notes[index].pop("username")
        yaml_notes[index]["Заголовок"] = yaml_notes[index].pop("title")
        yaml_notes[index]["Описание"] = yaml_notes[index].pop("content")
        yaml_notes[index]["Статус"] = yaml_notes[index].pop("status")
        yaml_notes[index]["Дата создания"] = yaml_notes[index].pop("created_date")
        yaml_notes[index]["Дедлайн"] = yaml_notes[index].pop("issue_date")
    with open(filename, mode="w", encoding="utf-8") as file:
        yaml.dump(yaml_notes, file, allow_unicode=True, sort_keys=False)