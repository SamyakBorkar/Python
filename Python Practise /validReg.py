import re 
r='hey this is samyak borkar having reg no 2022BIT037 and boobzy 2022bcs067 and dummy person with 2022Ycces098'
pattern=r'\d{4}+[a-zA-Z]{3}+\d{3}'
data=re.findall(pattern, r)
print(data)
