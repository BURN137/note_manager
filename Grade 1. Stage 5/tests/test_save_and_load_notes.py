import unittest
from data import save_notes_to_file, load_notes_from_file

class TestNoteManager(unittest.TestCase):
    # Тест проверки корректности импорта/экспорта в файл YAML
    def test_save_and_load_notes(self):
        notes = [{"username": "username",
            "title": "title",
            "content": "content",
            "status": "Новая",
            "created_date": "05.01.2025",
            "issue_date": "10.01.2025"}]
        save_notes_to_file(notes, "test.yaml")
        loaded_notes = load_notes_from_file("test.yaml")
        self.assertEqual(notes, loaded_notes)

if __name__ == '__main__':
    unittest.main()

