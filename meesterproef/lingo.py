from src.data.lingowords import *
from src.data.art import *
from src.classes.lingo_game import lingo_game
from src.classes.team import Team
from src.classes.player import Player


print(lingo_title)

while True:
    
    play = input("Woudld you like to start a game of lingo? (Y/N):  ")

    if (play.lower() == 'y'):
        print("let's play!!")
        
        team_1_name = input("select the name of the first team:  ")
        team_1_player_1 = Player(input(f"select the first player of {team_1_name}:  "))
        team_1_player_2 = Player(input(f"select the second player of {team_1_name}:  "))
        
        team_2_name = input("select the name of the second team:  ")
        team_2_player_1 = Player(input(f"select the first player of {team_2_name}:  "))
        team_2_player_2 = Player(input(f"select the second player of {team_2_name}:  "))
        
        team_1 = Team(team_1_name, team_1_player_1, team_1_player_2)
        team_2 = Team(team_2_name, team_2_player_1, team_2_player_2)
        
        lingo_round = lingo_game(team_1, team_2)
        
        lingo_round.start_game()
        
    elif (play.lower() == 'n'):
        print("thanks for playing!! 👋")
        break
        
    else:
        print("try entering a valid option!")



