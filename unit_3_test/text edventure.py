import os
import pygame
import time

pygame.mixer.init()

folder = os.path.dirname(os.path.abspath(__file__))

music_file = os.path.join(folder, "steves-lava-chicken.mp3")

folder = os.path.dirname(os.path.abspath(__file__))

music_file_2 = os.path.join(folder, "heres-johnny_1.mp3")

folder = os.path.dirname(os.path.abspath(__file__))

music_file_3 = os.path.join(folder, "ialwayscomeback.mp3")

folder = os.path.dirname(os.path.abspath(__file__))

music_file_4 = os.path.join(folder, "chucky-laugh.mp3")

folder = os.path.dirname(os.path.abspath(__file__))

music_file_5 = os.path.join(folder, "darth-vader-theme.mp3")

folder = os.path.dirname(os.path.abspath(__file__))

music_file_6 = os.path.join(folder, "SpaceBalls_OST_-_Theme_vocal_by_The_Spinners_(mp3.pm).mp3")

folder = os.path.dirname(os.path.abspath(__file__))

music_file_7 = os.path.join(folder, "Star_Wars_-_End_Credits_(mp3.pm).mp3")

folder = os.path.dirname(os.path.abspath(__file__))

music_file_8 = os.path.join(folder, "Monty Python and the Holy Grail - Intermission.mp3")

folder = os.path.dirname(os.path.abspath(__file__))

music_file_9 = os.path.join(folder, "OST_Lord_Of_The_Rings_The_fellowship_of_the_rings_-_The_Bridge_Of_Khazad_Dum_(mp3.pm).mp3")

name = input ("Enter your name before you start.\n>")
def start_adventure():
    print (name + " is sitting and thinking to themself wondering what to do today")
    print ("1. Watch a movie")
    print ("2. find out what to eat")

    choice = input (">")

    if choice == "1":
        pick_movie()
  
    elif choice == "2":
        food_choice()
    else:
        start_adventure()

def pick_movie():
    print (name + " is trying to pick a movie help them out")
    print ("1. Lord Of The Rings")
    print ("2. Monty Python And The Holy Grail ")
    print ("3. Space Balls")
    print ("4. Star Wars")

    choice = input (">")

    if choice == "1":
        find_Lord_Rings()
    elif choice == "2":
        find_Monty_Python()
    elif choice == "3":
        find_Space_balls()
    elif choice == "4":
        find_star_wars()
    else:
        pick_movie()
def food_choice():
    print (name + " is trying to figure out what they wants to eat help them out")
    print ("1. durian")
    print ("2. MC. Donalds")
    print ("3. Burger King")
    print ("4. Applebees")  

    choice = input (">")

    if choice == "1":
        durian()
    elif choice == "2":
        mc_donalds()
    elif choice == "3":
        burger_king()
    elif choice == "4":
        Applebees()
    else:
        food_choice()

def find_Lord_Rings():
    print (name + " is looking for Lord Of The Rings help them out")
    print ("1. look under the couch")   
    print ("2. Go ask a freind ")

    choice = input (">")

    if choice == "1":
        found_lord_ring()
    elif choice == "2":
        outside()
    else:
        find_Lord_Rings()

def  find_Monty_Python():
    print (name + " is looking for Monty Python And The Holy Grail help them out")
    print ("1. look under the couch")   
    print ("2. Go ask a freind ")

    choice = input (">")

    if choice == "1":
        found_monty_python()
    elif choice == "2":
        outside_2()
    else:
        find_Monty_Python()

def find_Space_balls():
    print (name + " is looking for Space Balls help them out")
    print ("1. look under the couch")   
    print ("2. Go ask a freind ")

    choice = input (">")

    if choice == "1":
        found_space_balls()
    elif choice == "2":
        outside_3()
    else:
        find_Space_balls()

def find_star_wars():
    print (name + " is looking for star wars help them out")
    print ("1. look under the couch")   
    print ("2. Go ask a freind ")

    choice = input (">")

    if choice == "1":
        found_star_wars()
    elif choice == "2":
        outside_4()
    else:
        find_Lord_Rings()

def durian():
    print (name + " is looking for a durian were should they look ") 
    print ("1. look in the pantry")
    print ("2. look in the fridge")

    choice = input(">")

    if choice == "1":
        found_durian()
    elif choice =="2":
        print (" Thats not where it is try again!!!")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    else:
        durian()

def mc_donalds():
    print (name + " is looking for mc donalds were should hey look ") 
    print ("1. look in the fridge to see if you have left overs")
    print ("2. wait to see if it magically appears ")

    choice = input(">")

    if choice == "1":
        found_mcdonalds()
    elif choice =="2":
        print (" you sit there waitting for an eternity so long that you DIE!!! ")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    else:
        mc_donalds()

def burger_king():
    print (name + " is looking for burger king were should they look ") 
    print ("1. look in the fridge to see if you have left overs")
    print ("2. wait to see if it magically appears ")

    choice = input(">")

    if choice == "1":
        found_burger_king()
    elif choice =="2":
        print (" you sit there waitting for an eternity so long that you DIE!!! ")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    else:
        burger_king()

def Applebees():
    print (name + " is looking for Applebees were should they look ") 
    print ("1. look in the fridge to see if you have left overs")
    print ("2. wait to see if it magically appears ")

    choice = input(">")

    if choice == "1":
        found_Applebees()
    elif choice =="2":
        print (" you sit there waitting for an eternity so long that you DIE!!! ")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    else:
        Applebees()

def found_lord_ring():
    print (name + " is looking under the couch when they see this majestic movie called Lord Of The Rings what should they do now")
    print ("1. put D.V.D into D.V.D plyer and watch movie")
    print ("2. Break movie")

    choice = input (">")

    if choice == "1":
        watch_movie1()
    elif choice == "2":
        print("you get teleported into the movie were there is a dragon there that eats you alive")
        play = input ("do you want to play again?")
    
        if play == "yes":
                    start_adventure()
        else:
                    print ("Have a nice day")
    else:
        found_lord_ring()

def found_monty_python():
    print (name + " is looking under the couch when they see this majestic movie called Monty Python And The Holy Grail what should they do now")
    print ("1. put D.V.D into D.V.D plyer and watch movie")
    print ("2. Break movie")

    choice = input (">")

    if choice == "1":
        watch_movie2()
    elif choice == "2":
        print("you broke your favorite movie and you go into spiraling depression you lose")
        play = input ("do you want to play again?")
    
        if play == "yes":
                    start_adventure()
        else:
                    print ("Have a nice day")
        
    else:
        found_monty_python()

def found_space_balls():
    print (name + " is looking under the couch when they see this majestic movie called Space Balls what should they do now")
    print ("1. put D.V.D into D.V.D plyer and watch movie")
    print ("2. Break movie")

    choice = input (">")

    if choice == "1":
        watch_movie_4()
    elif choice == "2":
        print("you get teleported into a room were you are force to watch Space Balls the rest of your life")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    else:
        found_space_balls

def found_star_wars():
    print (name + " is looking under the couch when they see this majestic movie called Star Wars what should they do now")
    print ("1. put D.V.D into D.V.D plyer and watch movie")
    print ("2. Break movie")

    choice = input (">")

    if choice == "1":
        watch_movie3()
    elif choice == "2":
        print("You get teleported into space were the millennium falcon hits you and you DIE!!!!")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    else:
        found_star_wars

def outside():
    print(name +" is making there way outside when a dragon scopse down and grabs you at this moment you realise that you are in lord of the rings what should they do now? ")
    print ("1. some how summon a nuclear bomb")
    print ("2. see if you can fly")

    choice = input (">")

    if choice == "1":
        print("you get hit with somuch radiation you slowly fade away ")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    elif choice == "2":
        print("you fall to your death ")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    else:
        outside()

def outside_2():
    print(name +" you come across a white bunny what should they do? ")
    print ("1. run away")
    print ("2. go investigate")

    choice = input (">")

    if choice == "1":
        print(" the bunny kills you   ")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    elif choice == "2":
        print(" the bunny kills you  ")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    else:
        outside_2()

def outside_3():
    print(name +" you step outside and see a van driveing in space what do you do? ")
    print ("1. run away")
    print ("2. go investigate")

    choice = input (">")

    if choice == "1":
        print(" the van goes throw your house and you die")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    elif choice == "2":
        print(" you go into the van and you see what looks like people and they see you than push you into space ")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    else:
        outside_3()

def outside_4():
    print(name +" you step outside and it looks like you are in a ship you are given two dierections to go left or right? ")
    print ("1. left")
    print ("2. right")

    choice = input (">")

    if choice == "1":
        print(" you come face to face with darth vader and he force chokes you")
        time.sleep(3)
        pygame.mixer.music.load(music_file_5)
        pygame.mixer.music.play()
        play = input ("do you want to play again?")
        if play == "yes":
            pygame.mixer.music.stop()
            start_adventure()
        else:
            pygame.mixer.music.stop()
            print ("Have a nice day")
    elif choice == "2":
        print(" you some how get into a trashcompactor and get squeezed to death  ")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    else:
        outside_4()

def found_durian():
    print(name +" you hear someone stabbing your front door what do you do ")
    print ("1. go comfront the person at the front door")
    print ("2. go to the back door")
    print ("3. jump throw the side window")
    print ("4. go up to the attic")

    choice = input (">")

    if choice == "1":
        time.sleep(3)
        pygame.mixer.music.load(music_file_2)
        pygame.mixer.music.play()
        print(" her hear a guy say heres jonny and than things fade to black")
        play = input ("do you want to play again?")
        if play == "yes":
            pygame.mixer.music.stop()
            start_adventure()
        else:
            pygame.mixer.music.stop()
            print ("Have a nice day")
    elif choice == "2":
        time.sleep(3)
        pygame.mixer.music.load(music_file_4)
        pygame.mixer.music.play()
        print(" you see a small doll with a knife that is laughing and vision begain to fade")
        play = input ("do you want to play again?")
        if play == "yes":
            pygame.mixer.music.stop()
            start_adventure()
        else:
            pygame.mixer.music.stop()
            print ("Have a nice day")
    
    elif choice == "3":
        time.sleep(3)
        pygame.mixer.music.load(music_file_3)
        pygame.mixer.music.play()
        print(" and see a yellow bunny with a knfe in his hads and says i will always come back")
        play = input ("do you want to play again?")
        if play == "yes":
            pygame.mixer.music.stop()
            start_adventure()
        else:
            pygame.mixer.music.stop()
            print ("Have a nice day")

    elif choice == "4":
        time.sleep(3)
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        print(" you see a stand selling lava chicken you get intised by the catchy song ")
        play = input ("do you want to play again?")
        if play == "yes":
            pygame.mixer.music.stop()
            start_adventure()
        else:
            pygame.mixer.music.stop()
            print ("Have a nice day")
    else:
        found_durian()

def found_mcdonalds():
    print(name +" you here something buzzing around")
    print ("1. go comfront the buzzing sound")
    print ("2. run away")
    print ("3. do nothing")
    print ("4. pumal your face with Mc donalds")

    choice = input (">")

    if choice == "1":
        print(" you see a bee and it say hey and you pass out")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    elif choice == "2":
        print(" a hive drops on you and you die")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    
    elif choice == "3":
        print(" bee kiils you")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")

    elif choice == "4":
        print(" you ate to much Mc Donalds and you explode")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    else:
        found_mcdonalds()

def found_burger_king():
    print(name +" you here some strange sonds so how you going to call")
    print ("1. ghost busters")
    print ("2. child protective services ")
    print ("3. your insurance company")
    print ("4. seth")

    choice = input (">")

    if choice == "1":
        print(" the ghost busters see you as a ghost and put you in ghost trap")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    elif choice == "2":
        print(" they say you are insane so they call the cops because they think you are high and you get 500 years of jail")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    
    elif choice == "3":
        print(" they dont answer")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")

    elif choice == "4":
        print(" he dose not help you at all so you check your self and you fall throw lose floor bords and die ")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    else:
        found_burger_king()

def found_Applebees():
    print(name +" you hear loud sounds outside")
    print ("1. check it out")
    print ("2. do nothing ")
    print ("3. say thats a nice sound")
    print ("4. read book")

    choice = input (">")

    if choice == "1":
        print(" you see a van giveing out FREE candy and you check it out but insted of gitting FREE candy you get kidnapped and NEVER seen again")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    elif choice == "2":
        print(" van goes throw house and kills you")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    
    elif choice == "3":
        print(" nothing happends except free candy outside")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")

    elif choice == "4":
        print(" you are smart but you were sitting there too long that you die but when people find the body they see you only got to the first page ")
        play = input ("do you want to play again?")
        if play == "yes":
            start_adventure()
        else:
            print ("Have a nice day")
    else:
        found_Applebees()

def  watch_movie1():
    pygame.mixer.music.load(music_file_9)
    pygame.mixer.music.play()
    text_1 = " Unit Production Managers	Nikolas Korda\
Zane Weiner\
\
\
\
\
\
\
First Assistant Director	Carolynne Cunningham\
Second Assistant Director	Guy Campbell\
\
\
\
\
\
\
Executive In Charge Of Production	Carla Fry\
Executive In Charge Of Post Production	Jody Levin\
Executive In Charge Of Visual Effects	Lauren Ritchie\
\
\
\
\
\
\
\
\
Conceptual Designers	Alan Lee • John Howe\
\
\
\
\
\
\
Supervising Sound Editor/Co-Designer	Ethan Van Der Ryn\
Supervising Sound Director	Michael Hopkins\
Sound Editor	David Farmer\
\
\
\
\
Featuring\
Voice Of The Ring	Alan Howard\
Cast In Alphabetical Order\
Everard Proudfoot Noel Appleby\
\
Sauron Sala Baker\
\
Galadriel Cate Blanchett\
\
Pippin Billy Boyd\
\
Mrs Proudfoot Megan Edwards\
\
Gil-Galad Mark Ferguson\
\
Gandalf Ian McKellen\
\
Lurtz Lawrence Makoare\
\
Elendil Peter McKenzie\
\
Merry Dominic Monaghan\
\
Bounder Ian Mune\
\
Farmer Maggot Cameron Rhodes\
\
TBA\
\
Gate Keeper Martyn Sanderson\
\
Isildur Harry Sinclair\
\
TBA\
\
Gollum Andy Serkis\
\
Arden Liv Tyler\
\
Elrond Hugo Weaving\
\
Frodo	Elijah Wood\
Hero Orcs Goblins Uruks & Ringwrathhs\
\
TBA\
\
Cute Hobbit Children	Billy & Katie Jackson\
Doubles & Stand-ins\
\
TBA\
\
Riding Doubles\
\
TBA\
\
Extras Wranglers\
\
TBA\
\
Choreographer	Shona McCullagh\
\
\
Assistant Choreographer	Miriam Cuperman\
\
\
Cultural Fighting Styles	Tony Woolf\
\
\
Supervising Dialect Coach	Andrew Jack\
Dialect Coach	Roisin Carty\
\
\
Tolkien Language Translation	David Salo\
\
\
Stunt Coordinator	George Marshall Ruge\
\
\
Swordmaster	Bob Anderson\
\
\
Assistant Stunt Coordinator	Daniel W. Barringer\
Assistant Sword Master	Kirk Maxwell\
Stunt Rigger	Paul Shapcott\
Horse Stunt Coordinator	Casey O'Neill\
Coordinator	Alice Capper-Starr\
Stunt Performers\
\
TBA\
\
Set Decorator	Dan Hannah\
Art Directors\
\
TBA\
\
Assistant Art Directors	Jules Cook\
Ross McGarva\
Jacqui Allen\
Production Managers Second Units	Carol Kim\
Bridget Bourke\
First Assistant Directors Second Units	Simon Warnock\
David Norris\
Liz Tan\
Richard Barker\
Second Assistant Director	Marc Ashton\
Key Second Assistant Director Second Unit	Louise Harness\
Second Second Assistant Directors	Joanne Pearce\
Skot Thomas\
Second Assistant Director. Second Unit	Emma Cross\
Third Assistant Directors	Eric Houghton\
Chris Husson\
Richard Matthews\
Set PAs\
Star Olson • Katie Hutchinson • Robert Halcrow\
\
Production Coordinators\
Elaine Burt\
Niccola Sanderson Belcher • Aubrey Tradget\
\
Assistant Production Coordinators\
Emily Lascelles • Jeanne Stuart • Fran Davey • Brent Robb\
\
Assistant To Mr Peter Jackson	Jan Blenkin\
Assistant To Barrie M. Osborne	Janine Anery\
Producer's Assistant	Tanya Buchanan\
Travel & Accommodations Coordinators Matthews Dravitzki • Nicola BirchField • Liz Target\
\
It Support Duncan Nimmo • Helene Takacs\
\
PAs Runners\
\
TBA\
\
Wingnut Films Production Assistant	Caroline McKay\
Wingnut Films Runner	Carter Nixon\
Wingnut Films Accountant	Linda Klein-Nixon\
Script Supervisors Victoria Sullivan\
Oksana Sokol • Dianne Moffatt • Pat Robins\
\
Supervising Unit Location Manager	Richard Sharkey\
Supervising Location Manager	Robin Murphy"
    for letter in text_1:
        print(letter, end="", flush=True)
        time.sleep(0.001)
    print("\n")

    print("""             ___ . .  _                                                                                             
    "T$$$P"   |  |_| |_                                                                                             
     :$$$     |  | | |_                                                                                             
    :$$$                                                      "T$$$$$$$b.                                          
    :$$$     .g$$$$$p.   T$$$$b.    T$$$$$bp.                   BUG    "Tb      T$b      T$P   .g$P^^T$$  ,gP^^T$$ 
     $$$    d^"     "^b   $$  "Tb    $$    "Tb    .s^s. :sssp   $$$     :$; T$$P $^b.     $   dP"     `T :$P    `T
    :$$   dP         Tb  $$   :$;   $$      Tb  d'   `b $      $$$     :$;  $$  $ `Tp    $  d$           Tbp.   
    :$$  :$;         :$; $$   :$;   $$      :$; T.   .P $^^    $$$    .dP   $$  $   ^b.  $ :$;            "T$$p.  
     $$$  :$;         :$; $$...dP    $$      :$;  `^s^' .$.     $$$...dP"    $$  $    `Tp $ :$;     "T$$      "T$b 
    $$$   Tb.       ,dP  $$   Tb    $$      dP ""$""$" "$"$^^  $$$""T$b     $$  $      ^b$  T$       T$ ;      $$; 
     $$$    Tp._   _,gP   $$   `Tb.  $$    ,dP    $  $...$ $..  $$$   T$b    :$  $       `$   Tb.     :$ T.    ,dP 
    $$$;    "^$$$$$^"   d$$     `T.d$$$$$P^"     $  $   $ $"", $$$    T$b  d$$bd$b      d$b   "^TbsssP" 'T$bgd$P  
    $$$b.____.dP                                 $ .$. .$.$ss,d$$$b.   T$b.                                       
    .d$$$$$$$$$$P  bug                                                    `T$b.
    """)  

    play = input ("do you want to play again?")
    if play == "yes":
        pygame.mixer.music.stop()
        start_adventure()
    else:
        pygame.mixer.music.stop()
        print ("Have a nice day")

def watch_movie2():
    pygame.mixer.music.load(music_file_8)
    pygame.mixer.music.play()
    text_2 = "GRAHAM CHAPMAN PLAYED: KING ARTHUR. HICCOUGHING GUARD, THREE-HEADED KNIGHT\
\
JOHN CLEESE PLAYED: SECOND SOLDIER WITH A KEEN INTEREST IN BIRDS, LARGE MAN WITH DEAD BODY, BLACK KNIGHT, MR NEWT (A VILLAGE BLACKSMITH INTERESTED IN BURNING WITCHES), A QUITE EXTRAORDINARILY RUDE FRENCHMAN, TIM THE WIZARD, SIR LAUNCELOT\
\
TERRY GILLIAM PLAYED: PATSY (ARTHUR’S TRUSTY STEED), THE GREEN KNIGHT SOOTHSAYER, BRIDGEKEEPER, SIR GAWAIN (THE FIRST TO BE KILLED BY THE RABBIT)\
\
ERIC IDLE PLAYED: THE DEAD COLLECTOR, MR BINT (A VILLAGE NE’ER-DO -WELL VERY KEEN ON BURNING WITCHES), SIR ROBIN, THE GUARD WHO DOESN’T HICCOUGH BUT TRIES TO GET THINGS STRAIGHT, CONCORDE (SIR LAUNCELOT’S TRUSTY STEED), ROGER THE SHRUBBER (A SHRUBBER), BROTHER MAYNARD\
\
NEIL INNES PLAYED: THE FIRST SELF-DESTRUCTIVE MONK, ROBIN’S LEAST FAVORITE MINSTREL, THE PAGE CRUSHED BY A RABBIT, THE OWNER OF A DUCK\
\
TERRY JONES PLAYED: DENNIS’S MOTHER, SIR BEDEVERE, THREE-HEADED KNIGHT, PRINCE HERBERT\
\
MICHAEL PALIN PLAYED: 1ST SOLDIER WITH A KEEN INTEREST IN BIRDS, DENNIS, MR DUCK (A VILLAGE CARPENTER WHO IS ALMOST KEENER THAN ANYONE ELSE TO BURN WITCHES), THREE-HEADED KNIGHT, SIR GALAHAD, KING OF SWAMP CASTLE, BROTHER MAYNARD’S ROOMMATE\
\
CONNIE BOOTH PLAYED: THE WITCH\
\
CAROL CLEVELAND PLAYED: ZOOT AND DINGO\
\
BEE DUFFELL PLAYED: OLD CRONE TO WHOM KING ARTHUR SAID “NI!”\
\
JOHN YOUNG PLAYED: THE DEAD BODY THAT CLAIMS IT ISN’T, AND THE HISTORIAN WHO ISN’T A.J.P. TAYLOR AT ALL\
\
RITA DAVIES PLAYED: THE HISTORIAN WHO ISN’T A.J.P. TAYLOR (HONESTLY)’S WIFE\
\
SALLY KINGHORN PLAYED: EITHER WINSTON OR PIGLET\
\
AVRIL STEWART PLAYED: EITHER PIGLET OR WINSTON\
\
PYTHON (MONTY) PICTURES LTD\
Registered Address: 20 Fitzroy Square, London W1P6BB\
Registered Number 1138069 England\
August 5th, 1974."


    for letter in text_2:
        print(letter, end="", flush=True)
        time.sleep(0.001)

    print("\n")

    print("""             ┳┳┓         ┏┓   ┓       ┏┓   ┓  ┏┳┓┓     ┓┏  ┓    ┏┓    •┓
             ┃┃┃┏┓┏┓╋┓┏  ┃┃┓┏╋┣┓┏┓┏┓  ┣┫┏┓┏┫   ┃ ┣┓┏┓  ┣┫┏┓┃┓┏  ┃┓┏┓┏┓┓┃
             ┛ ┗┗┛┛┗┗┗┫  ┣┛┗┫┗┛┗┗┛┛┗  ┛┗┛┗┗┻   ┻ ┛┗┗   ┛┗┗┛┗┗┫  ┗┛┛ ┗┻┗┗
                      ┛     ┛                                ┛          """)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
   
    play = input ("do you want to play again?")
    if play == "yes":
        pygame.mixer.music.stop()
        start_adventure()
    else:
        pygame.mixer.music.stop()
        print ("Have a nice day")

def watch_movie3():
    pygame.mixer.music.load(music_file_7)
    pygame.mixer.music.play()
    text_3 = "Director\
:\
Richard Marquand\
Writer\
:\
Lawrence Kasdan, George Lucas\
Producer\
:\
Howard G. Kazanjian, Rick McCallum, Howard G. Kazanjian, George Lucas, Howard G Kazanjian\
Cinematographer\
:\
Alec Mills, Alan Hume\
Editor\
:\
Marcia Lucas, Duwayne Dunham, Sean Barton\
Executive Producer\
:\
George Lucas\
Cast\
:\
Mark Hamill, Anthony Daniels, Billy Dee Williams, Harrison Ford, Carrie Fisher\
First Assistant Director\
:\
David Tomblin\
Second Assistant Director\
:\
Russell Lodge, Christopher Newman, Roy Button, Eric Jewett, Michael E. Steele\
Co-Producer\
:\
Robert Watts, Jim Bloom\
Script Supervisor\
:\
Pamela Mann\
Stunts\
:\
Alf Joint, Ted Grossman, Bob Yerkes, Wendy Leech, Michael Cassidy, Frank Henson, Billy Horrigan, Peter Burroughs, Bob Anderson, Larry Holt, Paul Weston, Michael Cassidy, Malcolm Weaver, Peter Diamond, Marc Boyle, Colin Skeaping, Tracey Eddon, Dickey Beer\
Second Unit Director\
:\
George Lucas, Roger Christian\
Story by\
:\
George Lucas\
Rigging Gaffer\
:\
Tom Brown, Tom Brown\
Visual Effects Art Director\
:\
George Hull\
Utility Stunts\
:\
Martin Klebba\
Costume Design\
:\
Aggie Guerard Rodgers, Nilo Rodis-Jamero\
Production Designer\
:\
Fred Hole, James L. Schoppe, Norman Reynolds\
Production Executive\
:\
Robert Latham Brown\
Screenwriter\
:\
Lawrence Kasdan, George Lucas\
Makeup Artist\
:\
Nick Dudman, Graham Freeborn, Kay Freeborn, Richard Mills, Tom Smith, Peter Robb-King\
Visual Effects\
:\
Paul Huston\
Original Music Composer\
:\
John Williams, John Williams\
Stand In\
:\
Roy Everson, Roy Beck, Stephen Calcutt, Erica Simmons, Jack Dearlove\
Casting\
:\
Mary Selway\
Stunt Double\
:\
Julius LeFlore, Peter Brace, Kiran Shah, Margarita Farrell, Sandi Gross, Vic Armstrong, Tracey Eddon\
Creature Design\
:\
Chris Walas, Phil Tippett\
Set Decoration\
:\
Harry Lange, Michael Ford\
Hairdresser\
:\
Paul LeBlanc, Patricia McDermott, Mike Lockey\
Assistant Production Manager\
:\
Patricia Carr, Patricia Carr\
Visual Effects Camera\
:\
Robert Elswit\
Makeup Designer\
:\
Stuart Freeborn, Phil Tippett\
Draughtsman\
:\
Reg Bream\
Stunt Coordinator\
:\
Glenn Randall Jr.\
Unit Manager\
:\
Louis G. Friedman\
Musician\
:\
London Symphony Orchestra\
Production Supervisor\
:\
Douglas Twiddy\
Unit Production Manager\
:\
Miki Herman\
Sound Re-Recording Mixer\
:\
Gary Summers\
Sound Designer\
:\
Ben Burtt\
Propmaker\
:\
Bill Hargreaves\
Technical specifications\
Rating:\
PG\
Country:\
United States\
Language:\
English\
Duration:\
133 min\
Genres:\
Action, SciFi/Fantasy, Suspense/Thriller"
    for letter in text_3:
            print(letter, end="", flush=True)
            time.sleep(0.001)
    print("""                                                                                        
 @@@@@@   @@@@@@@   @@@@@@   @@@@@@@      @@@  @@@  @@@   @@@@@@   @@@@@@@    @@@@@@   
@@@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@@     @@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
!@@         @@!    @@!  @@@  @@!  @@@     @@!  @@!  @@!  @@!  @@@  @@!  @@@  !@@       
!@!         !@!    !@!  @!@  !@!  @!@     !@!  !@!  !@!  !@!  @!@  !@!  @!@  !@!       
!!@@!!      @!!    @!@!@!@!  @!@!!@!      @!!  !!@  @!@  @!@!@!@!  @!@!!@!   !!@@!!    
 !!@!!!     !!!    !!!@!!!!  !!@!@!       !@!  !!!  !@!  !!!@!!!!  !!@!@!     !!@!!!   
     !:!    !!:    !!:  !!!  !!: :!!      !!:  !!:  !!:  !!:  !!!  !!: :!!        !:!  
    !:!     :!:    :!:  !:!  :!:  !:!     :!:  :!:  :!:  :!:  !:!  :!:  !:!      !:!   
:::: ::      ::    ::   :::  ::   :::      :::: :: :::   ::   :::  ::   :::  :::: ::   
:: : :       :      :   : :   :   : :       :: :  : :     :   : :   :   : :  :: : :    

                                                                                        """)
    play = input ("do you want to play again?")
    if play == "yes":
        pygame.mixer.music.stop()
        start_adventure()
    else:
        pygame.mixer.music.stop()
        print ("Have a nice day")

def watch_movie_4():
    pygame.mixer.music.load(music_file_6)
    pygame.mixer.music.play()
    text_4 = """Director
Mel Brooks\
Writers\
Mel Brooks
written by &
Thomas Meehan
written by &
Ronny Graham
written by
Cast
(in credits order) verified as complete
Mel Brooks
Mel Brooks
President Skroob/Yogurt
John Candy at an event for The 60th Annual Academy Awards (1988)
John Candy
Barf
Rick Moranis in Splitting Heirs (1993)
Rick Moranis
Dark Helmet
Bill Pullman in Independence Day: Resurgence (2016)
Bill Pullman
Lone Starr
Daphne Zuniga
Daphne Zuniga
Princess Vespa
Dick Van Patten in Eight Is Enough (1977)
Dick Van Patten
King Roland
George Wyner in Wildcats (1986)
George Wyner
Colonel Sandurz
Michael Winslow
Michael Winslow
Radar Technician
Joan Rivers in The Apprentice (2004)
Joan Rivers
Dot Matrix(voice)
Lorene Yarnell Jansson
Lorene Yarnell Jansson
Dot Matrix(as Lorene Yarnell)
John Hurt
John Hurt
John Hurt
Sal Viscuso
Sal Viscuso
Radio Operator Sergeant Ricco
Ronny Graham in Spaceballs (1987)
Ronny Graham
Minister
Jim J. Bullock
Jim J. Bullock
Prince Valium(as JM J. Bullock)
Leslie Bevis in Murder, She Wrote (1984)
Leslie Bevis
Commanderette Zircon
Jim Jackman
Jim Jackman
Major Asshole
Mike Pniewski
Mike Pniewski
Laser Gunner(as Michael Pniewski)
Sandy Helberg in The Paragon of Comedy (1983)
Sandy Helberg
Dr. Schlotkin
Stephen Tobolowsky
Stephen Tobolowsky
Captain of the Guard
Jeff MacGregor in Show 123 (1989)
Jeff MacGregor
Snotty
Henry Kaiser
Magnetic Beam Operator
Denise Gallup
Charlene
Dian Gallup
Marlene
Gail Barle
Waitress
Dey Young
Dey Young
Waitress
Rhonda Shear
Rhonda Shear
Woman in Diner
Robert Prescott
Robert Prescott
Sand Cruiser Driver
Jack Riley at an event for The Aristocrats (2005)
Jack Riley
TV Newsman
Tom Dreesen
Tom Dreesen
Megamaid Guard
Dom DeLuise, Rudy De Luca, and Rick Lazzarini in Spaceballs (1987)
Rudy De Luca
Vinnie(as Rudy DeLuca)
Tony Griffin
Prison Guard
Rick Ducommun
Rick Ducommun
Prison Guard
Ken Olfson in One Day at a Time (1975)
Ken Olfson
Head Usher
Bryan O'Byrne in Bewitched (1964)
Bryan O'Byrne
Organist
Wayne Wilson
Trucker in Cap
Ira Miller
Short Order Cook
Earl Finn
Guard with Captain
Mitchell Bock
Video Operator
Tommy Swerdlow
Tommy Swerdlow
Troop Leader
Tim Russ in Crossroads (1986)
Tim Russ
Trooper
Ed Gale
Ed Gale
Dink
Antonio Hoyos
Dink
Felix Silla
Felix Silla
Dink
Arturo Gil
Arturo Gil
Dink
Tony Cox at an event for Who's Your Caddy? (2007)
Tony Cox
Dink
John Kennedy Hayden
Dink
Dee Booher
Bearded Lady(as Deanna Booher)
Johnny Silver
Johnny Silver
Caddy Arnold
Brenda Strong
Brenda Strong
Nurse Gretchen
Dom DeLuise
Dom DeLuise
Pizza the Hutt(voice)
Rest of cast listed alphabetically
Elaine Ballace
War Room Tech #1(uncredited)
Robert Buckingham
Robert Buckingham
Wedding Guest(uncredited)
Corey Burton in Atlantis: The Lost Empire (2001)
Corey Burton
Dink(voice) (uncredited)
John E. Coleman
Prison Guard(uncredited)
John Copage
Wedding Guest(uncredited)
Dan Cotter
Wedding Guest(uncredited)
Bob K. Cummings
Prison Guard(uncredited)
Robert Dulaine
Wedding Guest(uncredited)
Brent Dunsford
Wedding Guest(uncredited)
Rose Dursey
War Room Tech #2(uncredited)
Dane Farwell
Dane Farwell
Ape #1(uncredited)
Buddy Gates
Wedding Guest(uncredited)
Roy Goldman in M*A*S*H (1972)
Roy Goldman
Spaceball(uncredited)
Camille Hagen
Woman in Diner(uncredited)
Phil Hartman
Phil Hartman
Dink(voice) (uncredited)
Fritz Herzog
Prince Valium Family Member(uncredited)
Conrad Hurtt
Conrad Hurtt
Spaceball Guard(uncredited)
Richard Karron
Pizza the Hut(uncredited)
Rick Lazzarini
Rick Lazzarini
Ape #2(uncredited)
Tress MacNeille
Tress MacNeille
Dink(voice) (uncredited)
Terence Marsh
Terence Marsh
Spaceball Drum Beater(uncredited)
Jeri McBride
Wedding Guest(uncredited)
Steve McLean
Steve McLean
Movie Crew Member(uncredited)
Thomas Meehan
Thomas Meehan
King Roland's Aide(uncredited)
Jim Michael
Diner Patron(uncredited)
Sam Nickens
Wedding Guest(uncredited)
John Paragon
John Paragon
Dink(voice) (uncredited)
Rob Paulsen at an event for Jimmy Neutron: Boy Genius (2001)
Rob Paulsen
Spaceball with Comb/Dink(voice) (uncredited)
David Pfeiffer
Wedding Guest(uncredited)
Denney Pierce in The Invisible Man (2000)
Denney Pierce
Prison Guard(uncredited)
Julie Pitkanen
Self-Destruct Voice(uncredited)
Ben Pollock
Wedding Guest(uncredited)
Julie Salles
Wedding Guest(uncredited)
George Sasaki
Transporter Technician(uncredited)
Richard Dreyfuss and Dennis Scott in What About Bob? (1991)
Dennis Scott
Lone Starr Stunt Double(uncredited)
Reynaldo Silva
Wedding Guest(uncredited)
Marvin Smith
Wedding Guest(uncredited)
Walter Smith
Wedding Guest(uncredited)
Paul G. Stalone
Wedding Guest(uncredited)
Cary Stratton
Spaceball(uncredited)
Don Terwilliger
Transporter Technician(uncredited)
Oliver Theess
Oliver Theess
Wedding Guest(uncredited)
Dick Warlock and Anne Bruner in Halloween II (1981)
Dick Warlock
Vulcan Pinch Guard Mylar(uncredited)
Jesse Wayne
Jesse Wayne
Pizza Guy(uncredited)
Brian J. Williams
Brian J. Williams
Prison Guard(uncredited)
Sheb Wooley
Sheb Wooley
Screaming Guard(archive sound) (uncredited)
Dee Dee Young
Wedding Guest(uncredited)
Producers
Mel Brooks
produced by
Ezra Swerdlow
co-producer
Composer
John Morris
music by
Cinematographer
Nick McLean
director of photography
Editor
Conrad Buff IV
edited by
Casting
David Rubin
Bill Shepard
casting by
Production Designer
Terence Marsh
production designed by
Art Director
Harold Michelson
Set Decorator
John Franco Jr.
Costume Designer
Donfeld
costumes designed by
Makeup Department
Ken Diaz
makeup artist
Melanie Levitt
makeup artist (as Melanie Elaine Levitt)
Ben Nye III
makeup designer (as Ben Nye Jr.)
Rick Stratton
makeup artist
Dione Taylor
hair stylist
Max Alvarez
makeup special effects (uncredited)
Susan A. Cabral
makeup artist (uncredited)
Joe English
makeup special effects (uncredited)
Screaming Mad George
makeup special effects (uncredited)
John Goodwin
makeup special effects (uncredited)
Steve LaPorte
makeup artist (uncredited)
David Rau
makeup special effects (uncredited)
Elaina P. Schulman
hair stylist (uncredited)
Production Management
Robert Latham Brown
production manager
Second Unit Directors or Assistant Directors
Mitchell Bock
second assistant director
Carol D. Bonnefil
additional second assistant director
Dan Kolsrud
assistant director
Art Department
Camille Abbott
illustrator
Jerry Gadette
stand-by painter
Arthur Gelb
property illustrator
William Gideon
carpenter
Peter J. Kelly
set designer (as Peter Kelly)
Guy A. MacLaury
general foreman (as Guy Allan MacLaury)
William S. Maxwell III
leadman (as William Maxwell III)
Richard McKenzie
set designer
James J. Pickering
drapery man
Ken Reed
construction foreman
Jacques Valin
set designer
Dianne Wager
assistant art director (as Diane Wager)
Steve Willis
propmaker foreman
S. Bruce Wineinger
construction coordinator
José Ignacio Álvarez
carpenter (uncredited)
John Alvin
poster artist (uncredited)
Steve Havrilla
labor foreman (uncredited)
William Hutchinson
paint foreman (uncredited)
Wayne Kerner
sign writer (uncredited)
Mick McGinty
advance poster artwork (uncredited)
Greg Nestor
swing gang (uncredited)
Joseph Perugini
plasterer foreman (uncredited)
Benjamin Resella
scenic effects supervisor (uncredited)
Earl W. Shubin
swing gang (uncredited)
Christopher Windisch
carpenter (uncredited)
Sound Department
Sandina Bailo-Lape
sound effects editor
Michael John Bateman
supervising dialogue editor
Richard Beggs
rerecording mixer
David Franklin Bergad
assistant sound editor (as David Bergad)
Bob Bowman
assistant sound editor (as Robert Bowman)
Sue Breitrose
assistant sound editor
Scott Chandler
assistant sound editor
Don Coufal
production sound mixer
Ken Fischer
sound effects editor
Ernie Fosselius
sound effects editor
Laja Holland
assistant sound editor
Ronald Jacobs
sound effects editor
Tom Johnson
foley recordist
Glad Pickering
dialogue editor
Gary Rydstrom
sound designer / re-recording mixer (uncredited)
Paige Sartorius
assistant sound editor
George Simpson
dialogue editor
Ronald Sinclair
dialogue editor
David Slusser
assistant sound editor
Jim Stuebe
production sound mixer (as Jim Steube)
Gary Summers
rerecording mixer
Randy Thom
rerecording mixer / sound designer
Dennie Thorpe
foley artist
Jeff Wexler
production sound mixer
Pamela Jule Yuen
assistant sound editor (as Pamela J. Yuen)
Jim Borgardt
adr editor (uncredited)
Bill Rojas
70mm magnetic sound (uncredited)
Bill Voigtlander
adr editor (uncredited)
Special Effects
Peter Albiez
special effects supervisor
Trevor Cripps
special effects technician
Rick Lazzarini
barf ear animatronics
Mark Lesser
available light
Richard Ratliff
special effects
Damon Allison
special effects (uncredited)
Raymond C. Boyle
special effects (uncredited)
William Burdette Jr.
special effects (uncredited)
Albert Delgado
special effects (uncredited)
Cy Guerrier
special effects (uncredited)
Paul Haines
special effects (uncredited)
John J. Hawkins
special effects (uncredited)
Gary L. Karas
special effects (uncredited)
Bruce Knechtges
special effects (uncredited)
Thomas Lantz
special effects (uncredited)
Russell McElhannon
special effects (uncredited)
Raymond Oberg
special effects (uncredited)
Peter Olexiewicz
special effects (uncredited)
Lambert Powell
special effects (uncredited)
Tom Prossner
special effects sculptor (uncredited)
Raymond Robinson
special effects (uncredited)
Monty Shook
special effects (uncredited)
Michael Wilmot
special effects (uncredited)
Roger Winiger
special effects (uncredited)
Visual Effects
Richard Alexander
effects technician: Apogee Inc.
Percy Angress
special visual effects producer: Apogee Inc.
David Beasley
model maker: Apogee Inc.
Mat Beck
motion control camera operator: Apogee Inc.
Cosmas Paul Bolger Jr.
optical camera assistant: Apogee Inc.
Craig Boyajian
visual effects coordinator
Stephen David Brooks
motion control camera assistant: Apogee Inc. (as Stephen Brooks)
Rae Burkland
model department special design: Apogee Inc.
Glenn Campbell
motion control camera assistant: Apogee Inc.
Clint Colver
effects animation supervisor: Apogee Inc.
Stephen Dane
visual effects art director: Apogee Inc. (as Steven Dane)
Peter Donen
visual effects supervisor
Dennis Dorney
optical camera assistant: Apogee Inc.
Roger Dorney
optical supervisor: Apogee Inc.
Syd Dutton
matte painting effects (as Sid Dutton)
John Eaves
model maker: Apogee Inc.
Jonathan Erland
visual effects matte technician: Apogee Inc.
Cory Faucher
model maker: Apogee Inc.
Rick Gilligan
optical camera assistant: Apogee Inc.
Ron Goldstein
effects technician: Apogee Inc.
Mark Gredell
motion control camera assistant: Apogee Inc.
Peter Gruskoff
visual effects production assistant
Rhonda C. Gunner
video and graphic displays: Video Image
David R. Hardberger
motion control camera operator: Apogee Inc. (as David Hardberger)
Richard E. Hollander
video and graphic displays: Video Image
Robert Jason
chief set lighting technician: Apogee Inc. (as Bob Jason)
Paul D. Johnson
motion control programmer: Apogee Inc. (as Paul Johnson)
Grant McCune
chief model maker: Apogee Inc.
Susan McGuire
none
Gregory L. McMurry
video and graphic displays: Video Image (as Gregory L. McMurray)
Alvah J. Miller
motion control electronics engineer: Apogee Inc.
Debbi Nikkel
chief production auditor: Apogee Inc.
Tom Pahk
model maker: Apogee Inc.
Jerry Pooler
optical camera operator: Apogee Inc.
Ron Robinson
motion control camera assistant: Apogee Inc.
Christopher S. Ross
model maker: Apogee Inc. (as Chris Ross)
Jay Roth
model maker: Apogee Inc.
Suzie Schneider
model maker: Apogee Inc. (as Suzy Schneider)
Robert Shepherd
executive in charge of production: Apogee Inc.
John R. Shourt
animation illustrator: Apogee Inc. (as John Shourt)
William Shourt
effects technician: Apogee Inc. (as Bill Shourt)
Douglas Smith
motion control camera operator: Apogee Inc. (as Doug Smith)
David Sosalla
model maker: Apogee Inc.
Smokey Stover
model maker: Apogee Inc.
John E. Sullivan
motion control camera operator: Apogee Inc. (as John Sullivan)
Bill Taylor
matte painting effects
Ron Thornton
model department special design: Apogee Inc.
Don Trumbull
visual effects engineer: Apogee Inc.
Michael Van Himbergen
production coordinator: Apogee Inc.
John C. Wash
video and graphic displays: Video Image
Harry Weinmann
animation illustrator: Apogee Inc.
Albert Whitlock
matte painting supervisor
Joseph Yanuzzi
assistant editor: Apogee Inc. (as Joe Yanuzzi)
Charles Bailey
creature shop manager: ILM (uncredited)
David Cornelius
motion control technician (uncredited)
Joss Geiduschek
model maker: Apogee Inc. (uncredited)
David Johnson
dancing alien puppeteer: ILM (uncredited)
Sam Longoria
visual effects machinist: Apogee Inc. (uncredited)
Michael Douglas Middleton
visual effects still photographer (uncredited)
Mark Setrakian
dancing alien animatronics: ILM (uncredited)
Eben Stromquist
dancing alien supervisor: ILM (uncredited)
Joseph Thomas
animation cameraman (uncredited)
Lauren Vogt
dancing alien sculptor: ILM (uncredited)
Stunts
Dick Warlock
stunt coordinator (as Richard Warlock) / stunt actor (uncredited)
Bob K. Cummings
stunt actor (uncredited)
Dane Farwell
stunt double: Bill Pullman (uncredited)
Eddie Matthews
stunt actor (uncredited)
Denney Pierce
stunt actor (uncredited)
Dennis Scott
stunt actor (uncredited)
Michael Washlake
stunts (uncredited)
Jesse Wayne
stunt double: for Mel Brooks (uncredited)
Jack West
stunt double: Rick Moranis (uncredited)
Brian J. Williams
stunt actor (uncredited)
Camera and Electrical Department
Stephen E. Bridge
camera operator (as Steve Bridge)
Michael A. Chavez
first assistant camera
Lindsay P. Hill
video playback operator
Gerald A. King
second grip (as Jerry King)
George Llerena
second assistant camera
Steve McLean
first assistant camera
Michael D. O'Shea
camera operator
Víctor Pérez
assistant lighting technician (as Victor Perez)
Thomas P. Powell
rigging electrician
Peter Sorel
still photographer
Bruce D. Spellman
second grip (as Bruce Spellman)
Tom Stern
chief lighting technician
Bill Young
key grip (as William C. Young)
Paul Amorelli
electrician (uncredited)
Frank Detone Jr.
rigging grip (uncredited)
Jim Dunford
dolly grip (uncredited)
Patrick James Grosswendt
electrician (uncredited)
Michael Laws
electrician (uncredited)
Mitchell Lookabaugh
grip (uncredited)
Jack E. McLean Jr.
electrician (uncredited)
David L. Merrill
second dolly grip (uncredited)
Michael Douglas Middleton
still photographer: special art (uncredited)
Jim Porter
electrician (uncredited)
Bill Rustic
grip (uncredited)
Michael J. Spehar
electrician (uncredited)
Costume and Wardrobe Department
Bruce Ericksen
wardrobe supervisor: men
Charmaine Nash Simmons
wardrobe supervisor: women (as Charmaine N. Simmons)
Ed Burza
costumer: wedding sequence (uncredited)
Armand Coutu
costumer: wedding sequence (uncredited)
Sharon Iris Crall
costumer: wedding sequence (uncredited)
Lorraine Dawson
costumer: wedding sequence (uncredited)
Guilbert Dulfer
tailor (uncredited)
Joan Joseff
costume jeweller (uncredited)
Tina Joseff
costume jeweller (uncredited)
Perri Kimono
costume key person (uncredited)
Don Pike
costume key person (uncredited)
Steven Zimbelman
costume key person (uncredited)
Editorial Department
Debra Goldfield
assistant editor
Jay Ignaszewski
associate editor
Nicholas C. Smith
additional editor
Clarinda Wong
assistant editor
Location Management
Michael John Meehan
location manager (as Michael J. Meehan)
Music Department
Jack Hayes
orchestrator
Eugene Marks
music editor
Norman B. Schwartz
vocal effects supervisor
Armin Steiner
scoring mixer
Patricia Aiken
musician: violin (uncredited)
Dale Anderson
musician: drums, percussion (uncredited)
Don Ashworth
musician: woodwinds (uncredited)
Jim Atkinson
musician: french horn (uncredited)
Israel Baker
musician: violin (uncredited)
Rick Baptist
musician: trumpet (uncredited)
Myer Bello
musician: viola (uncredited)
Chuck Berghofer
musician: bass (uncredited)
Emily Bernstein
musician: woodwinds (uncredited)
Tom Boyd
musician: oboe soloist (uncredited)
Alfred Breuning
musician: violin (uncredited)
Tom Brown
music copyist (uncredited)
Darius Campo
musician: violin (uncredited)
Norman Carr
musician: violin (uncredited)
Fred Cooper
music copyist (uncredited)
Larry Corbett
musician: cello (uncredited)
Rose Corrigan
musician: woodwinds (uncredited)
Wayne Coster
music copyist (uncredited)
Harry Cykman
musician: violin (uncredited)
Roy D'Antonio
musician: woodwinds (uncredited)
Paulinho Da Costa
musician: percussion (uncredited)
Robert Daugherty
musician: bass (uncredited)
Waldemar DeAlmeida
musician: cello (uncredited)
Drew Dembowski
musician: bass (uncredited)
Bob DiVall
musician: trumpet (uncredited)
Assa Drori
musician: violin (uncredited)
David Duke
musician: french horn (uncredited)
George Duke
musician: keyboards (uncredited)
Earl Dumler
musician: woodwinds (uncredited)
Arni Egilsson
musician: bass (uncredited)
William Elton
musician: trombone (uncredited)
Henry Ferber
musician: violin (uncredited)
Ron Folsom
musician: violin (uncredited)
Gary Foster
musician: woodwinds (uncredited)
Catherine Gotthoffer
musician: harp (uncredited)
George Graham
musician: trumpet (uncredited)
Marilyn Graham
musician: violin (uncredited)
Gary Gray
musician: woodwinds (uncredited)
Danny Greco
musician: drums, percussion (uncredited)
Sol Gubin
musician: drums, percussion (uncredited)
Wendy Hall
music copyist (uncredited)
Diana Halprin
musician: violin (uncredited)
Gwenn Heller
musician: violin (uncredited)
John Hornschuch
musician: bass (uncredited)
Paul Jackson Jr.
musician: guitar (uncredited)
Ron Jannelli
musician: woodwinds (uncredited)
Patricia Johnson
musician: violin (uncredited)
Tommy Johnson
musician: tuba (uncredited)
Deborah S. Mitchell Jones
music copyist (uncredited)
Jeff Jones
music copyist (uncredited)
Jo Ann Kane
music copyist (uncredited)
Raymond Kelley
musician: cello (uncredited)
Randy Kerber
musician: keyboards, piano (uncredited)
Janet Ketchum
musician: woodwinds (uncredited)
Carol Kleister-Castillo
musician: viola (uncredited)
Bernard Kundell
musician: violin (uncredited)
C.T. Lake
music copyist (uncredited)
Michael Lloyd
music arranger (uncredited) / song producer (uncredited)
Nancy V. Loe
musician: woodwinds (uncredited)
Harry V. Lojewski
music copyist (uncredited) / musician: keyboards, piano (uncredited)
Warren Luening
musician: trumpet (uncredited)
Raymond Mace
music copyist (uncredited)
Yoko Matsuda
musician: violin (uncredited)
Malcolm McNab
musician: trumpet (uncredited)
Todd Miller
musician: drums, percussion (uncredited)
Kenneth W. Mitchell
music copyist (uncredited)
Angela Morley
orchestrator (uncredited)
Carole Mukagawa
musician: viola (uncredited)
Jennifer Munday
musician: violin (uncredited)
Brian O'Connor
musician: french horn (uncredited)
Don Palmer
musician: violin (uncredited)
Claudia Parducci
musician: violin (uncredited)
Richard Perissi
musician: french horn (uncredited)
Tony Plog
musician: trumpet (uncredited)
Ralph Pollock
musician: french horn (uncredited)
Debra M. Price
musician: violin (uncredited)
Kim Pringle
musician: viola (uncredited)
Rebecca Reese
musician: cello (uncredited)
Christopher Reutinger
musician: violin (uncredited)
Jay Rosen
musician: violin (uncredited)
Robin Ross
musician: viola (uncredited)
Meyer Rubin
musician: bass (uncredited)
Robert Sanov
musician: violin (uncredited)
Sheldon Sanov
musician: violin (uncredited)
David Schwartz
musician: bass (uncredited)
Frederick Seykora
musician: cello (uncredited)
David Shamban
musician: cello (uncredited)
Harry Shlutz
musician: cello (uncredited)
David Shostac
musician: woodwinds (uncredited)
Karen Smith
music copyist (uncredited)
Mike Snyder
musician: drums, percussion (uncredited)
Joe Soldo
musician: woodwinds (uncredited)
Tina Soule
musician: cello (uncredited)
Spiros Stamos
musician: violin (uncredited)
Sheridon Stokes
musician: woodwinds (uncredited)
Robert Stone
musician: bass (uncredited)
Lisa M. Sutton
musician: violin (uncredited)
Jeremy Thale
music copyist (uncredited)
James Thatcher
musician: french horn (uncredited)
Barbara Thomason
musician: viola (uncredited)
Richard Todd
musician: french horn (uncredited)
Robert Tricarico
musician: woodwinds (uncredited)
Cynthia Ann Turner
music copyist (uncredited)
Lloyd Ulyate
musician: trombone (uncredited)
Ian Underwood
musician: keyboards, piano (uncredited)
Gerald Vinci
musician: violin (uncredited)
Don Waldrop
musician: tuba (uncredited)
Freddie Washington
musician: bass (uncredited)
Chauncey Welsch
musician: trombone (uncredited)
John Winter
musician: woodwinds (uncredited)
John Wittenberg
musician: violin (uncredited)
Gary Woodward
musician: woodwinds (uncredited)
Margaret Wooten
musician: violin (uncredited)
David Young
musician: bass (uncredited)
Bob Zimmitti
musician: drums, percussion (uncredited)
Mihail Zinovyev
musician: viola (uncredited)
Script and Continuity Department
Julie Pitkanen
script supervisor
Transportation Department
Chet Brooks
transportation captain
Jim Chesney
transportation coordinator
Chester Haffey
transportation
Frank Ancone
driver (uncredited)
Rodney Lee Bennett
driver (uncredited)
Donald P. Desmond
driver (uncredited)
David Diaz
driver (uncredited)
Craig Fehrman
driver (uncredited)
David Freeman
driver (uncredited)
Frank Hernandez
driver (uncredited)
William Hogue
driver (uncredited)
Ray Osburn
driver (uncredited)
Richard Reedy
driver (uncredited)
Christopher Rigby
driver (uncredited)
Richard Tashjian
driver (uncredited)
Color Department
Brian Borne
colorist (uncredited)
Craft Services
Ramon Pahoyo
craft service
Dale Ashman
craft service: special effects (uncredited)
Robert W. Ramage
craft service: special effects (uncredited)
Production Department
James Caverly
production assistant
Joanne Wetzel Caverly
production assistant (as JoAnne Wetzel Caverly)
Mary Courtney
production coordinator
Charles J.D. Schlissel
production assistant (as Charles Schlissel)
Production Finance and Accounting
Alison Harstedt
accountant
Laurie Stuebe
accountant (as Laurie Steube)
Property Department
Bill King
assistant property master
Dennis J. Parrish
property master (as Dennis Parrish)
Publicity
Saul Kahan
publicist
Susan Lee Smith
publicist (uncredited)
Voice Actors - Dubbing

Italian (2)
Pino Ammendola
Pizza Hot
Massimo Giuliani
Barf
Additional Crew
Nyna Cravens
assistant: Mr. Candy
Karen D'Arc
assistant: Mr. Meehan & Mr. Graham
Ann Fisher
assistant: Mr. Meehan & Mr. Graham
Anthony Goldschmidt
title designer
Daren Hicks
assistant: Ezra Swerdlow
K. Lenna Katich
production controller (as K. Lenna Kunkel)
Alan Ladd Jr.
presenter
Louis Sapin
French adaptation: dubbed version
Leah Zappy
assistant: Mr. Brooks
Roy Goldman
stand-in: Mel Brooks (uncredited)
Lillian Michelson
researcher (uncredited)
Julie Salles
stand-in: Daphne Zuniga (uncredited)
Jeff Viola
stand-in (uncredited)
Robert 'Bobby Z' Zajonc
helicopter pilot (uncredited)
Thanks
Bob Greenberg
the producer wishes to give special thanks to
Gerald B. Greenberg
the producer wishes to give special thanks to (as Jerry Greenberg)"""

    for letter in text_4:
            print(letter, end="", flush=True)
            time.sleep(0.001)

    print("""                                                                                           
 @@@@@@ @@@@@@@   @@@@@@   @@@@@@@ @@@@@@@@    @@@@@@@   @@@@@@  @@@      @@@       @@@@@@ 
!@@     @@!  @@@ @@!  @@@ !@@      @@!         @@!  @@@ @@!  @@@ @@!      @@!      !@@     
 !@@!!  @!@@!@!  @!@!@!@! !@!      @!!!:!      @!@!@!@  @!@!@!@! @!!      @!!       !@@!!  
    !:! !!:      !!:  !!! :!!      !!:         !!:  !!! !!:  !!! !!:      !!:          !:! 
::.: :   :        :   : :  :: :: : : :: ::     :: : ::   :   : : : ::.: : : ::.: : ::.: :  
                                                                                           """)
    play = input ("do you want to play again?")
    if play == "yes":
        pygame.mixer.music.stop()
        start_adventure()
    else:
        pygame.mixer.music.stop()
        print ("Have a nice day")

start_adventure()
