def Decimal_Subtraction(num1, num2):
	return (Str_to_Int(num1)-Str_to_Int(num2))
	
def Str_to_Int(n1):
	return eval(n1)
	

num1= "10.98"
num2= "7.5"
print(Decimal_Subtraction(num1, num2))
