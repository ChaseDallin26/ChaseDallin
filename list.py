list = ["pineapple", "apple", "grapes", "starburry", "rasbarry"] 

print(list[0])
print(list[-1])

add= input ("add a fruit to the list\n>")

list.append(add)

print (list)

sub= input ("remove a fruit\n>")

list.remove(sub)

print(list)

list.sort()
print("----------------------")
print (list)