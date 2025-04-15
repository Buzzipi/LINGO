class Team:
    def __init__(self, team_name, member1, member2):
        self.team_name = team_name
        self.member1 = member1
        self.member2 = member2
        self.amountOfGuessedWords = 0
        
    def ShowTeamMembers(self):
        print(f"first team member: {self.member1.name}")
        print(f"second team member: {self.member2.name}")
        
    def ShowTeamName(self):
        print(f"team name: {self.team_name}")