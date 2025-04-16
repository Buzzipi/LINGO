from src.data.lingowords import *
from src.classes.mastermind import *
import random
from collections import Counter

class lingo_game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
    
    def Mastermind(self, team): # class instance (object)
        MM = Mastermind()
        MM.mastermind_game(team)
    
    def start_game(self):
        print()
        print("LETS BEGIN!")
        while True:
            
            if (self.team1.amountOfFailedGuessedWords >= 3):
                print(f"🎉{self.team2.team_name} has won the game, because {self.team1.team_name} failed to guess a word 3 times in a row!!🎉")
                break
            
            if (self.team2.amountOfFailedGuessedWords >= 3):
                print(f"🎉{self.team1.team_name} has won the game, because {self.team2.team_name} failed to guess a word 3 times in a row!!🎉")
                break
            
            self.Mastermind(self.team1)
            if (self.team1.amountOfGuessedWords >= 10):
                print(f"🎉{self.team1.team_name} guessed 10 words correctly!!, they are the lingo winners!🎉")
                break
            
            self.Mastermind(self.team2)
            if (self.team2.amountOfGuessedWords >= 10):
                print(f"🎉{self.team2.team_name} guessed 10 words correctly!!, they are the lingo winners!🎉")
                break
       
        
                
            
    
        
    