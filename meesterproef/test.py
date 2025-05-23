import random

list_of_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]

nums_in_possession = ["3", "5", "1"]

test_bingo_card = [["3", "32", "3", "0"],
                   ["3", "3", "3", "11"],
                   ["13", "1", "1", "11"],
                   ["1", "21", "36", "1"]]

bingo_card = []

    
#create bingo card 
for i in range(4):
    row = []
    for i in range(4):
        random_num = random.choice(list_of_num)
        row.append(random_num)
    bingo_card.append(row)


#check for matching nums in nums_in_possession and putting an X on them
for row in test_bingo_card:
    for number in row:
        for nums in nums_in_possession:
            if nums == number:
                index = row.index(nums) # index is used to find the index of a given value in a list
                row[index] = "x"

#bingo card with X's for nums that the user has in possession
print()
print("[BINGO CARD]")
for list in test_bingo_card:
    aligned_list = []
    for num in list:
        aligned_list.append(num.center(4))
    print(' '.join(aligned_list))


#bingo if the user has 4 X's diagonally or horizontally next to each other


#checks for horizontal bingo's
for row in test_bingo_card:
    if all(num == "x" for num in row):
        print("Bingo")

#checks for vertical bingo's
for vertical_col in range(4):   
    if all(test_bingo_card[row][vertical_col] == "x" for row in range(4)):
        print("Bingo")



#checks for diagonal bingo's
    
#left-to-right
if all(test_bingo_card[i][i] == "x" for i in range(4)):
    print("bingo")

#right-to-left
if all(test_bingo_card[i][3-i] == "x" for i in range(4)):
    print("Bingo")
        
        

    
    



