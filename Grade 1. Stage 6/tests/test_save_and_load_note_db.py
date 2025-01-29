import unittest, os
from database import load_notes_from_db, setup_database, save_note_to_db

class TestNoteManager(unittest.TestCase):
    # Тест проверки корректности экспорта из базы данных
    def test_save_and_load_note_db(self):
        test_db_name = "test.db"
        note_dict = [{"id": 1,
                      "username": "Артур",
                      "title": "Покупка",
                      "content": "Продукты на вечер",
                      "status": "Новая",
                      "created_date": "05.01.2025",
                      "issue_date": "10.01.2025"},
                     {"id": 2,
                      "username": "Денис",
                      "title": "Кредит",
                      "content": "Оплатить кредит",
                      "status": "Выполнено",
                      "created_date": "06.01.2025",
                      "issue_date": "17.01.2025"}]
        if os.path.exists(test_db_name) is True:
            self.assertEqual(note_dict, load_notes_from_db(test_db_name))
        else:
            setup_database(test_db_name)
            save_note_to_db(note_dict,test_db_name)
            self.assertEqual(note_dict, load_notes_from_db(test_db_name))


if __name__ == '__main__':
    unittest.main()