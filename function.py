# --- Define your functions below! ---
from random import*
def intro():
    print("(Hi, I'm Sushi the ChatBot, but you can call me yours ;))!")

def askName():
    print("(Nice to meet you! Let's be friends!)")

def choose():
       print("What would you like to do?\n")
       choices = ("Ask for a fact - Get to know Sushi better.\n"
                  "Tell a joke - Sushi will tell you a joke.\n")
       print(choices)
       choice = input("(Choose from 'fact' or 'joke')")
       process_input2(choice)
    
def process_input2(user_input):
    if user_input == "fact":
        knowBetter()
        choose()
    elif user_input == "joke":
        funny()
        choose()
    else:
        print("**Not a valid input.**")
        choose()
        

def knowBetter():
    topic= ["My favorite color is purple!","I love golden retrievers!", "I'm from a Girls Who Code laptop!", "My favorite subject is computer science~", "I LOVE coding!"]
    random=randint(0,len(topic)-1)
    ask=topic[random]
    print(ask)

def funny():
    jokes=["Are you milk tea? Because we'd get oolong!", "Are you coffee? Cause I love you a latte~","What did one ocean say to the other? Nothing. They just waved!","What do you call a fake noodle? An impasta!","Why is Peter Pan always flying? Because he neverlands! I love this joke because it never grows old!"]
    rando=randint(0,len(jokes)-1)
    laugh=jokes[rando]
    print(laugh)

def repeat(other):
    responses = ["fact","joke"]
    while not other in responses:
        print("Please input 'fact' or 'joke'")
        other = input("What would you like to do?")
    choose()
        
    
def process_input(user_input):
    feelings = ["good", "great", "ok"]
    if user_input in feelings:
        print("(That's good!)")
        choose()
        
    else:
        print("(I hope your day gets better!)")
        
        


# --- Put your main program below! ---
def main():
    intro()
    while True:
        name = input("(What's your name?)")
        askName()
        question = input("(How was your day?)")
        process_input(question)     
        other = input("What would you like to do?")
        repeat(other)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
