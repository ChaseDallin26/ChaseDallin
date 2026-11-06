import random

num_gen = random.randint(1,100)
guess = False

while guess == False:
    guess = int(input ("guess a number 1-100\n>"))

    if guess == num_gen:
        guess = True
        print ("you guessed it")
    elif guess < num_gen:
        print ("the number is higher")
        guess = False
    elif guess > num_gen:
        guess = False
        print ("the number is lower")
    else:
        guess = False

