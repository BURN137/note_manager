import unittest
from data import save_notes_json

import json

class TestNoteManager(unittest.TestCase):
    # Тест проверки корректности импорта/экспорта в файл JSON
    def test_save_and_load_notes_json(self):
        notes = [{"username": "username",
            "title": "title",
            "content": "content",
            "status": "Новая",
            "created_date": "05.01.2025",
            "issue_date": "10.01.2025"}]
        save_notes_json(notes, "test.json")
        with open("test.json", mode="r", encoding="utf-8") as file:
            loaded_notes_json = json.loads(file.read())
            # print(notes)
            # print(loaded_notes_json)
        self.assertEqual(notes, loaded_notes_json)

if __name__ == '__main__':
    unittest.main()

