import random

num_gen = random.randint(1,100)
guess = False
num_guess = 0
while guess == False:
    guess = int(input ("guess a number 1-100\n>"))

    if guess == num_gen:
        guess = True
        num_guess += 1
        print ("you guessed it")
        print ("you guessed it in " + str(num_guess) + " atempts")
    elif guess < num_gen:
        num_guess += 1
        print ("the number is higher")
        guess = False
    elif guess > num_gen:
        num_guess += 1
        guess = False
        print ("the number is lower")
    else:
        num_guess += 1
        guess = False

