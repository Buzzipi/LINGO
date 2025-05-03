from src.data.lingowords import *
from src.classes.mastermind import *
import random
from src.classes.basket import *
from src.classes.bingo import *
import os
import time

class lingo_game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        
    # word guessing logic
    def Mastermind(self, team): # class instance (object)
        MM = Mastermind()
        MM.mastermind_game(team)
    
    # basket logic
    def CreatingBaskets(self, team1, team2):
        basket = Basket()
        basket.CreateBaskets(team1, team2)
    
    def PickingBallsFromBasket(self, team):
        basket = Basket()
        basket.BasketRound(team)
    
    def winnerByBalls(self, team1, team2):
        basket = Basket()
        value = basket.CheckPossibleWinnersBalls(team1, team2)  
        return value
        
    # bingo logic
    def CreateBingoCards(self, team1, team2):
        bingo = Bingo()
        bingo.CreateBingoCard(team1)
        bingo.CreateBingoCard(team2)
    
    def ShowBingoCard(self, team):
        bingo = Bingo()
        bingo.ShowBingoCard(team)
    
    def CheckBingo(self, team):
        bingo = Bingo()
        value = bingo.CheckForBingo(team)
        return value
        
        
    
    def start_game(self):
        os.system('cls')
        print()
        
        self.CreatingBaskets(self.team1, self.team2)
        self.CreateBingoCards(self.team1, self.team2)
        
        while True:
            
            
            current_score_team_1 = self.team1.amountOfGuessedWords
            current_score_team_2 = self.team2.amountOfGuessedWords
            
            
            if (self.team1.amountOfFailedGuessedWords >= 3):
                os.system('cls')
                print(f"🎉{self.team2.team_name} has won the game, because {self.team1.team_name} failed to guess a word 3 times in a row!!🎉")
                break
            
            if (self.team2.amountOfFailedGuessedWords >= 3):
                os.system('cls')
                print(f"🎉{self.team1.team_name} has won the game, because {self.team2.team_name} failed to guess a word 3 times in a row!!🎉")
                break
            
            os.system('cls')
            
            # team 1's turn
            self.Mastermind(self.team1)
            if (self.team1.amountOfGuessedWords >= 10):
                os.system('cls')
                print(f"🎉{self.team1.team_name} guessed 10 words correctly!!, they are the lingo winners!🎉")
                break
            
            if (self.team1.amountOfGuessedWords > current_score_team_1):
                self.PickingBallsFromBasket(self.team1)
            
            time.sleep(3)
            
            
            
            os.system('cls')
            
            
            # team 2's turn
            self.Mastermind(self.team2)
            if (self.team2.amountOfGuessedWords >= 10):
                os.system('cls')
                print(f"🎉{self.team2.team_name} guessed 10 words correctly!!, they are the lingo winners!🎉")
                break
            
            if (self.team2.amountOfGuessedWords > current_score_team_2):
                self.PickingBallsFromBasket(self.team2)
            
            time.sleep(3)
            
            
            
            
            winner_with_balls = self.winnerByBalls(self.team1, self.team2)
            
            if(winner_with_balls == True):
                break
            
            BingoWinnerTeam1 = self.CheckBingo(self.team1)
            BingoWinnerTeam2 = self.CheckBingo(self.team2)
            
            if BingoWinnerTeam1 == True:
                os.system('cls')
                print(f"🎉{self.team1.team_name} got BINGO!!🎉")
                break
            if BingoWinnerTeam2 == True:
                os.system('cls')
                print(f"🎉{self.team2.team_name} got BINGO!!🎉")
                break
                
            
        
        print()
        print()
        print(f"{self.team1.team_name} balls in possession: {self.team1.ballsInPossession}")
        print(f"{self.team2.team_name} balls in possession: {self.team2.ballsInPossession}")
        print()
        print()
        print(f"{self.team1.team_name}'s bingo card:")
        print()
        self.ShowBingoCard(self.team1)
        print()
        print()
        print("-----------------------------------------------")
        print(f"{self.team2.team_name}'s bingo card:")
        print()
        self.ShowBingoCard(self.team2)
        print()
                
       
        
                
            
    
        
    