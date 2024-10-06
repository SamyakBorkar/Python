import re 
dummy='hey this is samyak 9604450984 and fathers number is 9860805811 some fake number are 86745-322'
pattern=r'\d+'
data=re.findall(pattern,dummy)
print(data)
