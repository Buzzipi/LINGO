from src.data.lingowords import *
from src.data.art import *


print(lingo_title)

while True:
    
    play = input("Woudld you like to start a game of lingo? (Y/N):  ")

    if (play.lower() == 'y'):
        print("let's play!!")
        break
        
    elif (play.lower() == 'n'):
        print("oh ok :/")
        break
        
    else:
        print("try entering a valid option!")



