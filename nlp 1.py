import re
t = "The workshop is on 14/08/2026. Mail: test@gmail.com Call 9876543210 or 044-27654321 before 15/04/2026"
print(re.findall(r'\S+@\S+\.\S+|\d{10}|\d{3,4}-\d{7,8}|\d{2}/\d{2}/\d{4}', t))
