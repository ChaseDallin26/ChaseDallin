correct_answer = 0
 
def tally_score():
    q1 = input ("is mario in super smash bors ultimte\n>")
    q2 = input ("is darth vader in super smash bors ultimte\n>")
    q3 = input ("is sora in super smash bors ultimte\n>")
    q4 = input ("is sponge bob in super smash bors ultimte \n>")
    q5 = input ("is kazuya mshima in super smash bors ultimte \n>")
    global correct_answer 
    if q1 == "yes":
        correct_answer = correct_answer + 1
   
    if q2 == "no":
        correct_answer = correct_answer + 1

    if q3 == "yes":
        correct_answer = correct_answer + 1
    
    if q4 == "no":
        correct_answer = correct_answer + 1

    if q5 == "yes":
        correct_answer = correct_answer + 1
    print (str(correct_answer) + " correct answer")
    
tally_score()
