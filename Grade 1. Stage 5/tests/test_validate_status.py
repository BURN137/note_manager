import unittest

class TestNoteManager(unittest.TestCase):
    # Тест проверки корректности ввода статуса
    def test_validate_status(self):
        status = "Новая"
        list = ["Новая", "В процессе", "Выполнено"]
        self.assertTrue(list.index(status)>=0)

if __name__ == '__main__':
    unittest.main()

