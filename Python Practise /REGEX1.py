import re 
text = "Contact us at hello@example.com or support@test.org."
data = re.findall(r'[a-zA-Z0-9]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}',text)
print(data)
