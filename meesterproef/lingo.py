from src.data.lingowords import *
from src.data.art import *
from src.classes.lingo_game import *
from src.classes.team import *
from src.classes.player import *
from src.classes.animations import *
from src.classes.enums import *
import os
import time



animations.intro()



while True:

    animations.main_menu()
    
    user_input = input(":  ").lower()
    
    

    if (user_input.lower() == 'p'):
        os.system('cls') #clears the console
        
        team_1_name = input("select the name of the first team:  ")
        team_1_player_1 = Player(input(f"select the first player of {team_1_name}:  "))
        team_1_player_2 = Player(input(f"select the second player of {team_1_name}:  "))
        print()
        team_2_name = input("select the name of the second team:  ")
        team_2_player_1 = Player(input(f"select the first player of {team_2_name}:  "))
        team_2_player_2 = Player(input(f"select the second player of {team_2_name}:  "))
        
        team_1 = Team(team_1_name, team_1_player_1, team_1_player_2)
        team_2 = Team(team_2_name, team_2_player_1, team_2_player_2)
        
        lingo_round = lingo_game(team_1, team_2)
        
        lingo_round.start_game()
        
    elif (user_input.lower() == 'q'):
        os.system('cls')
        animations.outro()
        break  
    else:
        print()
        print("\033[93mtry entering a valid option!\033[0m")
        print()


