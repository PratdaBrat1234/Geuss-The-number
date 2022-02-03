import random
level = (input('Choose a level Easy, Medium, or Hard: '))
level = str(level)
if level == 'Easy':
    value = random.randint(1,10)
    num = (input('Guess the number(1 - 10): '))
    num = int(num)
    if num == value:
        print("CORRECT")
    else:
        print('INCORRECT, the number was', value)
elif level == 'Medium':
    value1 = random.randint(1,20)
    num1 = (input('Guess the number (1 - 20): '))
    num1 = int(num1)
    if num1 == value1:
        print("CORRECT")
    else:
        print('INCORRECT, the number was', value1)
elif level == 'Hard':
    value2 = random.randint(1,30)
    num2 = (input('Guess the number (1 - 30):  '))
    num2 = int(num2)
    if num2 == value2:
        print("CORRECT")
    else:
        print('INCORRECT, the number was', value2)
else:
    print("Please enter one of the given levels")
