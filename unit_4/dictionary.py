students = {
    "Alice" : "A",
    "chance" : "A++",
    "seth" :  "F------------------------------------------------",
    "Dane" : "A",
    "Matt" : "B",
}
for key in students:

    print (key + " : " + str(students[key]))

student = {"name": "Alice", "Age": 16, "Grade" : "A"}

print("-----------------------------------------------------------")

print (str(student["name"]))
print (str(student["Age"]))

student["Grade"] = "A+"

print (str(student["Grade"]))

movies = { 
    "bee movie" : "2007",
    "star wars" : "1977",
    "space balls" : "1987",
}
movie = input ("name your fav movie")
year = input ("what year was the movie created")

movies[movie] = year

for key in movies:
    print (key + " : " + str(movies[key]))

fruit = {"banana" : "10",
    "pineapple": "19",
    "watermelon": "20",
    "apple": "11",
    "strawberry" : "12",       
}
for key in fruit:
    print (key + " : " + str(fruit[key]))
remove = input ("remove a fruit")

del fruit [remove]

for key in fruit:
    print (key + " : " + str(fruit[key]))

inventory = {"apples": 10, "bananas": 5, "oranges": 8}
for key in inventory :
    print (key + " : " + str(inventory[key]))

words = [ "hi","bye","hi","pie",]
answer_data = {}
for word in words:
    if word in answer_data:
        answer_data[word] += 1
    else:
        answer_data[word] =1
print (answer_data)

employ_data = {
    "seth" : 1,
    "seilic" : 100000,
    "chase"  : 80000,
    "cooooooooooooooooopah D": 120000
}






