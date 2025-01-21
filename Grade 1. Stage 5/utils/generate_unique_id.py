# Функционал для генерации уникального идентификатора для заметок
# Используется библиотека uuid

# Подключаем модуль uuid
import uuid

def generate_unique_id():
    id = str(uuid.uuid4())
    return id
