import random

class Team:
    def __init__(self, team_name, member1, member2):
        self.team_name = team_name
        self.member1 = member1
        self.member2 = member2
        self.amountOfGuessedWords = 0
        self.amountOfFailedGuessedWords = 0
        self.basket = []
        self.ballsInPossession = []
        self.bingo_card = []
        
    def ShowTeamMembers(self):
        print(f"first team member: {self.member1.name}")
        print(f"second team member: {self.member2.name}")
        
    def ShowTeamName(self):
        print(f"team name: {self.team_name}")
        
    def RandomBallFromBasket(self):
        random_ball = random.choice(self.basket)
        
        print(f"you got a {random_ball} ball!")
        
        self.ballsInPossession.append(random_ball)