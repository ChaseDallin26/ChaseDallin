
item=input("what item are you buying\n")
price = float(input("how much dose it cost\n"))
tax_rate = 1.06875

def calculate_tax (item, price, rate):
    print(item + price + "befor tax and " +str(round(item_price * rate, 2)) + "after tax")

calculate_tax(item, price, tax_rate)


