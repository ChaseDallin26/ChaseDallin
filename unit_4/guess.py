import random

num_gen = random.randint(1,100)
guess = False
num_guess = 0
while guess == False:
    guess = int(input ("guess a number 1-100\n>"))

    if guess == num_gen:
        guess = True
        num_guess += 1
        print ("spot on")
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
if num_guess == 1:
    print ("your rank is unreal")
elif num_guess == 2 or num_guess == 3:
    print ("your rank is champion")
elif num_guess == 4 or num_guess == 5:
    print ("your rank is elite")
elif num_guess == 6 or num_guess == 7:
    print ("your rank is diamond")
elif num_guess == 8 or num_guess == 9:
    print ("your rank is platimum")
elif num_guess == 10 or num_guess == 11:
    print ("your rank is gold")
elif num_guess == 12 or num_guess == 13:
    print ("your rank is silver")
elif num_guess == 14 or num_guess == 15:
    print ("your rank is bronze")
elif num_guess >15:
    print ("your rank is wood")
