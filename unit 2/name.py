input_band = input ("whats your favorite band")
number_people = float(input ("how many people are going to the show"))
ticket_price = float(input ("how much money are the tickets selling for"))



def show_cost (band, people, price):
    print ("you are seeing " + band +" this is how many people are going"+ people + "this is how much you are spending" + price)

show_cost(input_band,str(number_people), str(ticket_price))


