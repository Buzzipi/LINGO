from src.classes.unit_tests import *


team_1_name = input("select the name of the first team:  ")
team_1_player_1 = Player(input(f"select the first player of {team_1_name}:  "))
team_1_player_2 = Player(input(f"select the second player of {team_1_name}:  "))

team_2_name = input("select the name of the first team:  ")
team_2_player_1 = Player(input(f"select the first player of {team_2_name}:  "))
team_2_player_2 = Player(input(f"select the second player of {team_2_name}:  "))

team_1 = Team(team_1_name, team_1_player_1, team_1_player_2)
team_2 = Team(team_2_name, team_2_player_1, team_2_player_2)

test = unit_tests(team_1, team_2)
    