import random

def guess_Number_and_prize():
    n, i = 5, 0
    print("Welcome to the Guess the Number Game")
    print("This game consists of 5 chances in total. If you guess correctly, you will be rewarded, otherwise, your money will be lost.")
    print("If you want to proceed further, enter Y for Yes, otherwise N for No.")
    
    num = input()
    if num in ['y', 'Y']:
        money = int(input("Enter the money amount: "))
        print("Guess the number between 1 and 100")
        
        random_number = random.randint(1, 100)
        
        while n > 0:
            i += 1
            print(f"Chance {i}")
            ip_number = int(input("Enter your guess: "))
            
            if random_number == ip_number:
                prize = prize_money(i, money)
                print(f"Congratulations! You won %.2f" % prize)
                break
            
            else:
                difference = abs(random_number - ip_number)
                if difference <= 25:
                    print("You are very close!")
                elif difference <= 50:
                    print("You are close!")
                elif difference <= 75:
                    print("You are far from the answer!")
                else:
                    print("You are very far from the answer!")

                n -= 1
                print(f"Remaining chances: {n}")
        
        if n == 0:
            print(f"Sorry, you've used all your chances!")
    else:
        return "Bye! Have a nice day."

def prize_money(chance, money):
    if chance == 1:
        return money * 5
    elif chance == 2:
        return money * 3
    elif chance == 3:
        return money * 2
    elif chance == 4:
        return money * 1.5
    else:
        return money

#print(guess_Number_and_prize())
guess_Number_and_prize()