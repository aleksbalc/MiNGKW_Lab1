import re

regex = r'((?P<name>[a-z]+)\.(?P<surname>[a-z]+)[0-9]*@(?P<is_student>(student\.)?)(wat\.edu\.pl))'
pattern = re.compile(regex)
email = "aleksandra.balcerzak@student.wat.edu.pl"
res = pattern.findall(email)
print(res)