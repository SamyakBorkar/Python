def dummy(name , age, /):
	return 'name is {} and age is {}'.format(name,age)
	
print(dummy('samyak',19))
print(dummy(age=20,name='samyak'))
