def PhoneNumber(digits):
	result=[""]
	numbers={'2':'abc',
		 '3':'def',
		 '4':'ghi',
		 '5':'jkl',
		 '6':'mno',
		 '7':'pqr',
		 '8':'stu',
		 '9':'wxyz',
	}
	
	for digit in digits:
		new_list=[]
		for elements in result:
			for letter in numbers[digit]:
				new_list.append(elements+letter)
				result=new_list
				
	return result
	
	
print(PhoneNumber("23"))
	
			
