# Предназначен для сохранения заметок в файл JSON.
# Для работы используется библиотека json

# Обращаемся к библиотеке datetime
import json

# Функция по созданию заметок в формате JSON
def save_notes_json(notes, filename):
    file = open(filename, mode="w", encoding="utf-8")
    json.dump(notes, file, indent=4, ensure_ascii=False)
    file.close()