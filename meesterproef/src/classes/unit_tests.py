from src.data.lingowords import *
from src.data.art import *
from src.classes.lingo_game import *
from src.classes.team import *
from src.classes.player import *
from src.classes.animations import *
from src.classes.miscellaneous import *

class unit_tests:
    def __init__(self, team_1, team_2):
        self.team_1 = team_1
        self.team_2 = team_2
        self.run_all_tests()
        
    
    # __ indicating a private method
    def __create_baskets_test(self):
        
        miscellaneous_features.print_spacing(2)
        
        print("--BASKET-CREATION-TEST--")
        print("test to check if baskets are being properly generated for both teams")
        
        miscellaneous_features.print_spacing(1)
        print("expected result: both team baskets lists filled with balls")
        miscellaneous_features.print_spacing(1)
        
        basket_object = Basket()
        
        basket_object.CreateBaskets(self.team_1, self.team_2)
        
        # checks if both lists are filled in or not, if they're emtpy, false is returned
        if self.team_1.basket and self.team_2.basket:
            print(f"✅ result: team 1 basket: {self.team_1.basket} || team_2 basket: {self.team_2.basket}")
        else:
            print(f"❌  result: team 1 basket: {self.team_1.basket} || team_2 basket: {self.team_2.basket}")
        
        miscellaneous_features.print_spacing(3)
    
    
    def __create_bingo_cards_test(self):
        
        miscellaneous_features.print_spacing(3)
        
        print("--BINGO-CARD-CREATION-TEST--")
        print("test to check if bingo cards are being correctly generated for both teams")
        
        miscellaneous_features.print_spacing(1)
        print("expected result: both teams bingo card lists filled with numbers")
        miscellaneous_features.print_spacing(1)
        
        bingo_object = Bingo()
        
        bingo_object.CreateBingoCard(self.team_1)
        bingo_object.CreateBingoCard(self.team_2)
        
        if self.team_1.bingo_card and self.team_2.bingo_card:
            print(f"✅ result: team 1 bingo card: {self.team_1.bingo_card} || team_2 bingo card: {self.team_2.bingo_card}")
        else:
            print(f"❌  result: team 1 bingo card: {self.team_1.bingo_card} || team_2 bingo card: {self.team_2.bingo_card}")
        
        miscellaneous_features.print_spacing(3)
        
        
    def __test_mastermind_logic(self):
        miscellaneous_features.print_spacing(3)
        print("--MASTERMIND-LOGIC-TEST--")
        print("a quick demo test to see if the mastermind logic is behaving properly")
        print("if you see any of the following, please report it too the dev!!")
        miscellaneous_features.print_spacing(1)
        print("- the 5 guessing attempts not working properly")
        print("- the random word length not lining up with the stripped out word length")
        print("- not saying you guessed the word correctly even tho you did")
        print("if you encounter any other strange bugs that are not listed, please report them too!")
        print("any feedback is also gladly appreciated :)")
        miscellaneous_features.print_spacing(1)
        
        game_test = Mastermind()
        
        game_test.mastermind_game(self.team_1)
        
        
        miscellaneous_features.print_spacing(3)
        
        
        
        
        
    def run_all_tests(self):
       unit_tests.__create_baskets_test(self)
       unit_tests.__create_bingo_cards_test(self)
       unit_tests.__test_mastermind_logic(self)