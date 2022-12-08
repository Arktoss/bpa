from random import randrange
import os
os.system("cls")

dial = int(input(print(f"Each lock has how many dials? ")))
combination = int(input(print(f"How many combinations should I generate? ")))

while combination > 1:
    one = 0
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print('''This application generates possible lock combinations; assuming that the numbers will be 
    ''')
    print("----------------------------")
    number = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
    if dial < 3:
        print("You can only make a combination with a minimum of 3 numbers")
    else:
        range = print(randrange(1, 9))
    print(f"Number{one+1}: {range}")

combination -= 1