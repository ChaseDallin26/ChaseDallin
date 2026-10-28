def amazon_prime():

    age = int(input ("whats your age\n>"))
    money = float(input ("whats your bank acoont balence\n>")) 
    want = input ("do you want amazon prime subcription\n>")
    if age >= 18:
       if money >= 139.99:
            if want == "yes":
                print("perchase confirmed")
    elif age <18: 
        consent = input("do you have parent consent?\ntype yes or no\n> ")
        if money >= 139.99:
            if want == "yes":
                print("perchase confirmed")

    else:
        print("not confermd")

 

 
amazon_prime()