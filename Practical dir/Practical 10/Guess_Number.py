import random
def guess_Number():
	random_number=random.randint(1,10)
	print("Enter a number in range from 1  to 10")
	x=int(input())
	if x in range(0,11):
		if x==random_number:
			return "Congratulation Your guess is right"

		else:
			return "Sorry Your Guess is wrong"
		

print(guess_Number())