import random 

buy_another = True
spent = 0
money =0

while buy_another:
    spent += 5
    print("you purchased a crate for $5!\/-$5\n")

    roll = random.random()

    if roll <0.40:
        print("you got a green....")
        money += 0.05
    elif roll < 0.75:
        print ("you got a blue....")
        money += 0.50
    elif roll < 0.95:
        print ("you got a purple....")
        money += 1
    else:
        print ("you got a gold...")
        money += 40  
    choice = input("do you want to buy another crate???")

    if choice == "yes":
          buy_another = True
    else:
          buy_another = False