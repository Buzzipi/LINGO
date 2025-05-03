import random
from collections import Counter

class Basket:
    
    def CreateBaskets(self, team1, team2):
        basket = list(range(1, 56))

        colored_balls = ["green_ball", "green_ball", "green_ball", "red_ball", "red_ball", "red_ball"]

        for num in basket:
            if num % 2 != 0:
                team1.basket.append(str(num))

        for num in basket:
            if num % 2 == 0:
                team2.basket.append(str(num))

        for colored_ball in colored_balls:
            team1.basket.append(colored_ball)
            team2.basket.append(colored_ball)
    
    def TakeBallFromBasket(self, team):
        random_ball = random.choice(team.basket)
        team.ballsInPossession.append(random_ball)
        team.basket.remove(random_ball)
        return random_ball
    
    def BasketRound(self, team):
        first_ball = self.TakeBallFromBasket(team)
        print(f"team: {team.team_name} got a '{first_ball}' ball!")
        
        if first_ball == "red_ball":
            return # if the if statement is met, the function stops here
        else:
            second_ball = self.TakeBallFromBasket(team)
            print(f"team: {team.team_name} got a '{second_ball}' ball!")
    
    def CheckPossibleWinnersBalls(self, team1, team2):
        duplicate_items_team_1 = dict(Counter(team1.ballsInPossession))
        duplicate_items_team_2 = dict(Counter(team2.ballsInPossession))
        
        try:
            if(duplicate_items_team_1["red_ball"] >=3):
                print(f"🎉team '{team2.team_name}' wins because team '{team1.team_name}' got 3 red balls!🎉") 
                return True
            if(duplicate_items_team_2["red_ball"] >=3):
                print(f"🎉team '{team1.team_name}' wins because team '{team2.team_name}' got 3 red balls!🎉") 
                return True
            if(duplicate_items_team_1["green_ball"] >=3):
                print(f"🎉team '{team1.team_name}' wins because they got 3 green balls!🎉") 
                return True
            if(duplicate_items_team_2["green_ball"] >=3):
                print(f"🎉team '{team2.team_name}' wins because they got 3 green balls!🎉") 
                return True
        except KeyError:
            return False
        
            

        
        
        
