
bank = ["bumfuzzle", "cattywumpus", "collywobbles", "whippersnapper", "gubbins", "widdershins", "normal", "elephant", "michelle", "natalie", "amber", "claire", "tapioca"]

print("Let's play hangman! :)")

from random import*
#choosing word
random = randint(1, len(bank))
word = bank[random]
x = len(word)
list = []
for i in range(x):
    list.append('_')
print(list)



#Intro - Choose a letter
##guesses = 0
##while guesses <= 7:
guess = input("Guess a letter: ")

for i in range(len(word)):
    if guess == word[i]:
        list[i] = guess
    print(list)
