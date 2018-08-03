start = '''
One sunny day, you walk into the kitchen where your father is casually sipping coffee.
You tell him good morning and he greets you back.
He then asks you if you could buy some milk for him.
Mission: Buy milk.
'''
print(start)

print("Will you buy milk for your father? Type 'yes' or 'no'.")
answer1 = input()
while not (answer1 == "yes" or answer1 == "no"):
    print("Invalid response! Type 'yes' or 'no'.")
    answer1 = input()



if answer1 == "yes":
    print("You: Okay Dad, I'll see you later.")
    park = '''
    You walk on over to the park, where the path forks into two directions.
    You can either take a shortcut or go the regular way.
    '''
    print(park)

    print("Type 'shortcut' or 'regular'.")
    answer2=input()
    while not (answer2 == "shortcut" or answer2 == "regular"):
        print("Invalid response! Type 'shortcut' or 'regular'.")
        answer2 = input()
          
    if answer2 == "shortcut":
        print("Oh no! There's a creek in the path! Will you cross or turn back?")
        print("Type 'cross' or 'turn back'.")

        answer3 = input()
        
        if answer3 == "cross":
            print("You made it to the store! What type of milk would you like to buy?")
            print("Type 'dairy' or 'soy'")
            answer4 = input()
            if answer4 == "dairy" or "soy":
                print("Mission Complete! Good Job!")
        elif answer3 == "turn back":
            print("You decided to turn back and take the regular path.")
    if answer2 == "regular":
        regular1 = '''
    As you are walking down the street, you see a spaceship crash...
    There are aliens and injured civillians everythwere!
    Do you choose to run and get your milk, or help the injured...?
    '''

    print(regular1)
    print("Type 'run' or 'help'")
    
    answer5 = input()
    if answer5 == "help":
        print("The grateful civillians reward you for your courage with milk!")
        print("Mission Complete!")

    elif answer5 == "run":
        run = '''
        Your frantic running caught the aliens' attention.
        They chase you in hot pursuit and eventually surround you!
        Should you try to fight free from their wrath or attempt to befriend these creatures?
        '''

        print(run)
        print("Type 'fight' or 'befriend'.")

        answer6 = input()
        if answer6 == "befriend":
            print("The aliens worship you and have invited you to travel the universe with them! Safe travels!")
            print("You've completed the perfect ending!")
        elif answer6 == "fight":
            fight= '''
        Prepare for a battle to the death!
        Because the aliens believe in a fair fight, they've allowed you to choose your weapon!
        Brave civilian, they offer you a sword or a gun.
        Choose your weapon wisely.
        '''

        print(fight)
        print("Type 'sword' or 'gun'.")

        answer7 = input()
        if answer7 == "sword":
            print("Congratulations, you've won the fight and saved the city from the aliens!")
            print("Now hurry to the store and get that milk, champion!")
        elif answer7 == "gun":
            print("Shame on you! This is a dirty weapon!")
            print("Unfortunately the gun backfired and exploded in your face! RIP soldier. Better luck next time...")

        regular = '''
    As you are walking down the street, you see a spaceship crash...
    There are aliens and injured civillians everythwere!
    Do you choose to run and get your milk, or help the injured...?
    '''

    print(regular)
    print("Type 'run' or 'help'")
    
    answer5 = input()
    if answer5 == "help":
        print("The grateful civillians reward you for your courage with milk!")
        print("Mission Complete!")

    elif answer5 == "run":
        run = '''
        Your frantic running caught the aliens' attention.
        They chase you in hot pursuit and eventually surround you!
        Should you try to fight free from their wrath or attempt to befriend these creatures?
        '''

        print(run)
        print("Type 'fight' or 'befriend'.")

        answer6 = input()
        if answer6 == "befriend":
            print("The aliens worship you and have invited you to travel the universe with them! Safe travels!")
            print("You've completed the perfect ending!")
        elif answer6 == "fight":
            fight= '''
        Prepare for a battle to the death!
        Because the aliens believe in a fair fight, they've allowed you to choose your weapon!
        Brave civilian, they offer you a sword or a gun.
        Choose your weapon wisely.
        '''

        print(fight)
        print("Type 'sword' or 'gun'.")

        answer7 = input()
        if answer7 == "sword":
            print("Congratulations, you've won the fight and saved the city from the aliens!")
            print("Now hurry to the store and get that milk, champion!")
        elif answer7 == "gun":
            print("Shame on you! This is a dirty weapon!")
            print("Unfortunately the gun backfired and exploded in your face! RIP soldier. Better luck next time...")
    
    
        
    
elif answer1 == "no":
    print("Dad: You're grounded!")
    print("Mission failed!")

    
