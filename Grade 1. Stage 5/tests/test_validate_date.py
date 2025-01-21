import unittest, datetime

class TestNoteManager(unittest.TestCase):
    # Тест проверки корректности ввода дат
    def test_validate_date(self):
        date = "05.01.2025"
        date_odj = datetime.datetime.strptime(date,"%d.%m.%Y").date()
        self.assertTrue(date_odj)

if __name__ == '__main__':
    unittest.main()

