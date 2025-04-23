import random

class Bingo:
    
    def CreateBingoCard(self, team):
        basket = team.basket.copy()
        
        for item in basket:
            try:
                if "green_ball" in basket:
                    basket.remove("green_ball")
                if "red_ball" in basket:
                    basket.remove("red_ball")
            except ValueError:
                continue
            
        for _ in range(4):
            row = []
            for _ in range(4):
                random_num = random.choice(basket)
                row.append(random_num)
                basket.remove(random_num)
            team.bingo_card.append(row)
    
    def CheckForMatchingNums(self, team):
        #check for matching nums in nums_in_possession and putting an X on them
        print(team.bingo_card)
        for row in team.bingo_card:
            for number in row:
                for nums in team.ballsInPossession:
                    if nums == number:
                        index = row.index(nums) # index is used to find the index of a given value in a list
                        row[index] = "x"
    
    def ShowBingoCard(self, team):
        #bingo card with X's for nums that the user has in possession
        
        self.CheckForMatchingNums(team)
        
        print()
        print("[BINGO CARD]")
        for list in team.bingo_card:
            aligned_list = []
            for num in list:
                aligned_list.append(str(num).center(4))
            print(' '.join(aligned_list))
    
    def CheckForBingo(self, team):
        #bingo if the user has 4 X's diagonally or horizontally next to each other

        #checks for horizontal bingo's
        for row in team.bingo_card:
            print(f"ur in the horizontal_col bingo check")
            print(row)
            if all(num == "x" for num in row): #if statement is not being met
                print("horizontal is true")
                return True

        #checks for vertical bingo's
        for vertical_col in range(4):   
            print(f"ur in the vertical_col bingo check")
            if all(team.bingo_card[row][vertical_col] == "x" for row in range(4)):
                print("vertical is true")
                return True



        #checks for diagonal bingo's
            
        #left-to-right
        if all(team.bingo_card[i][i] == "x" for i in range(4)):
            return True

        #right-to-left
        if all(team.bingo_card[i][3-i] == "x" for i in range(4)):
            return True
        
    