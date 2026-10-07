number_apples = float(input ("how many apples do you have"))
number_people = float(input ("how many people are there"))



def portion (apples, people):
    return (apples/people)

apples_per_person = str(portion(number_apples, number_people))

def served (people, apples):
    print ("served" + number_people + " a glasses of apple jucie at " + apples_per_person + "per glass" )


served (number_people,apples_per_person)
