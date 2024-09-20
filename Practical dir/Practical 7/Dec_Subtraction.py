Number_Map_Dict={
"0":0,
"1":1,
"2":2,
"3":3,
"4":4,
"5":5,
"6":6,
"7":7,
"8":8,
"9":9
}

def Dec_subtraction(num1, num2):
	n1= str_to_int(num1)
	n2= str_to_int(num2)
	return abs(n1-n2)
	
def str_to_int(num):
	num_length=len(num)
	if num_length ==1:
		return Number_Map_Dict[num]
	else:
		return Number_Map_Dict[num[0]]*pow(10, num_length-1)+str_to_int(num[1:])
		


number_1="50"
number_2="30"
print(Dec_subtraction(number_1, number_2))
