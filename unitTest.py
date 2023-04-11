import unittest
from Lab1git.EmailExtractor import EmailExtractor

class EmailExtractorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            # email, is_student, is_male, name, surname
            ["norbert.waszkowiak@wat.edu.pl", False, True, "Norbert", "Waszkowiak"],
            ["jan.kowalski@student.wat.edu.pl", True, True, "Jan", "Kowalski"],
            ["anna.nowak@student.wat.edu.pl", True, False, "Anna", "Nowak"],
            ["adrianna.abacka01@student.wat.edu.pl", True, False, "Adrianna", "Abacka"],
            ["katarzyna.babacka@wat.edu.pl", False, False, "Katarzyna", "Babacka"],

            ["jan.nowak01@wat.edu.pl", False, True, "Jan", "Nowak"],
            ["maria.kowalczyk02@student.wat.edu.pl", True, False, "Maria", "Kowalczyk"],
            ["julian.malinowski@wat.edu.pl", False, True, "Julian", "Malinowski"],
            ["izabela.adamska01@student.wat.edu.pl", True, False, "Izabela", "Adamska"],
            ["marta.jakubowska@wat.edu.pl", False, False, "Marta", "Jakubowska"],
            ["piotr.wisniewski@student.wat.edu.pl", True, True, "Piotr", "Wiśniewski"], #ten test nie przejdzie pozytywnie, poniewaz w mailach nie mozemy miec polskich znakow
            ["karolina.jakubowska@student.wat.edu.pl", True, False, "Karolina", "Jakubowska"],
            ["andrzej.nowak@wat.edu.pl", False, True, "Andrzej", "Nowak"],
            ["katarzyna.kowalska@wat.edu.pl", False, False, "Katarzyna", "Kowalska"],
            ["piotr.janowski@wat.edu.pl", False, True, "Piotr", "Janowski"]
        ]

    def test_is_student(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                is_student = x[1]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(is_student, extractor.is_student())

    def test_is_male(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[3]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.get_name())

    def test_get_surname(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                surname = x[4]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(surname, extractor.get_surname())

    def test_get_name(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[3]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.get_name())


if __name__ == '__main__':
    unittest.main()