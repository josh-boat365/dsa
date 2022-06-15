"""_summary_
    You ask a user to guess a number between 1 and 50.

If they guess outside that range, you prompt with an error encouraging them to choose a number within the proper range.

Whenever they guess the wrong number you ask if they want to keep playing or if they'd like to quit.

Finally, when the user eventually guesses the right number you congratulate them and show the number of attempts they had.

"""


import random


guess_count = 0
guess_limit = 3
my_number = random.randint(1,50)

while guess_count <= guess_limit:
    guess = int(input("Guess a number between 1 and 50: \n"))
    guess_count+=1
    if guess > my_number:
        print("You guess too High")
    elif guess < my_number:
        print("You guess too low")
    elif guess == my_number:
        print("Huraay!! you guessed it right")
        break
    
    if guess_count == 3:
        print("Game Over")
        break
    else:
        print("Try again")