from src.data.lingowords import *
import random

class lingo_game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
    
    def random_selected_word(self, words_list):
        randomly_selected_word = random.choice(words_list)
        return randomly_selected_word
    
    def start_game(self):
        print()
        print("LETS BEGIN!")
        random_word = list(self.random_selected_word(words))
        
        word_lines = []
        
        for _ in range(len(random_word)):
            word_lines.append("_")
            
        while True:
            print(random_word)
            for i in range(5):
                print(word_lines) 
                user_guess = list(input("guess the word:  "))
                
                index = 0
                for letter in user_guess:
                    if(letter in random_word):
                        word_lines[index] = letter
                        
                if(user_guess in random_word):
                    for i in range(len(random_word)):
                        if random_word[i] == user_guess:
                            word_lines[i] == user_guess
                            break
                
                
            
    
        
    