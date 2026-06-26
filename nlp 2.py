import re
t = "22/11/2027 mail a@gmail.com call 9123456780 or 080-23456789"
print("Emails:", re.findall(r'\S+@\S+\.\S+', t))
print("Phones:", re.findall(r'\d{10}|\d{3,4}-\d{7,8}', t))
print("Dates:", re.findall(r'\d{2}/\d{2}/\d{4}', t))
