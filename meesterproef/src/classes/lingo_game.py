from src.data.lingowords import *
from src.classes.mastermind import *
import random
from collections import Counter
from src.classes.basket import *

class lingo_game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
    
    def Mastermind(self, team): # class instance (object)
        MM = Mastermind()
        MM.mastermind_game(team)
    
    def CreatingBaskets(self, team1, team2):
        basket = Basket()
        basket.CreateBaskets(team1, team2)
        
    
    def start_game(self):
        print()
        print("LETS BEGIN!")
        
        self.CreatingBaskets(self.team1, self.team2)
        
        while True:
            
            
            current_score_team_1 = self.team1.amountOfGuessedWords
            current_score_team_2 = self.team2.amountOfGuessedWords
            
            
            if (self.team1.amountOfFailedGuessedWords >= 3):
                print(f"🎉{self.team2.team_name} has won the game, because {self.team1.team_name} failed to guess a word 3 times in a row!!🎉")
                break
            
            if (self.team2.amountOfFailedGuessedWords >= 3):
                print(f"🎉{self.team1.team_name} has won the game, because {self.team2.team_name} failed to guess a word 3 times in a row!!🎉")
                break
            
            
            # team 1's turn
            self.Mastermind(self.team1)
            if (self.team1.amountOfGuessedWords >= 10):
                print(f"🎉{self.team1.team_name} guessed 10 words correctly!!, they are the lingo winners!🎉")
                break
            
            if (self.team1.amountOfGuessedWords > current_score_team_1):
                self.team1.RandomBallFromBasket()
            
            
            # team 2's turn
            self.Mastermind(self.team2)
            if (self.team2.amountOfGuessedWords >= 10):
                print(f"🎉{self.team2.team_name} guessed 10 words correctly!!, they are the lingo winners!🎉")
                break
            
            if (self.team2.amountOfGuessedWords > current_score_team_2):
                self.team2.RandomBallFromBasket()
        
        print()
        print()
        print(f"{self.team1.team_name} ball possession: {self.team1.ballsInPossession}")
        print(f"{self.team2.team_name} ball possession: {self.team2.ballsInPossession}")
        print()
        print()
                
       
        
                
            
    
        
    