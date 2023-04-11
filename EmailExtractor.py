import re

class EmailExtractor:

    def __init__(self, email):
        self.email = email
        self.regex = r'((?P<name>[a-z]+)\.(?P<surname>[a-z]+)([0-9]{2})?@(?P<is_student>(student\.)?)(wat\.edu\.pl))'

    def is_student(self) -> bool:
        pattern = re.compile(self.regex)
        res = pattern.findall(self.email)
        if res[0][4] == '':
            return False
        else:
            return True

    def get_name(self):
        pattern = re.compile(self.regex)
        res = pattern.findall(self.email)
        name = res[0][1]
        return name.capitalize()

    def get_surname(self):
        pattern = re.compile(self.regex)
        res = pattern.findall(self.email)
        surname = res[0][2]
        return surname.capitalize()

    def is_male(self) -> bool:
        name = self.get_name()
        last_char = name[-1]
        if last_char == 'a':
            return False
        else:
            return True

