import random
def fortune():
    try:
        print("greatings travaler i am bob the ultimate world eater.\n i am here to tell your forture")
        Q_one = input ("whats your favorite number\n>")
        Q_two = input ("whats you least favorite number\n>")
        Q_three = input ("whats the magic number\n>")
    except:
        print ("come agian soon")
        fortune()
    if int(Q_one) + int(Q_two) + int(Q_three) + random.randint(1, 10) >=100:
        print ("you have richs coming your way")
    elif int(Q_one) + int(Q_two) + int(Q_three)+ random.randint(1, 10) <=80:
        print("you will be very lucky in the near future")
    elif int(Q_one) + int(Q_two) + int(Q_three)+ random.randint(1, 10) <=60:
        print("you will have lots of fun today")
    elif int(Q_one) + int(Q_two) + int(Q_three)+ random.randint(1, 10) <=40:
         print("you will find love soon")
    elif int(Q_one) + int(Q_two) + int(Q_three)+ random.randint(1, 10) <=20:
         print("you will get everthing you want in the next second")
         
fortune()