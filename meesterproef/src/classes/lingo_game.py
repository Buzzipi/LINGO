from src.data.lingowords import *
import random
from collections import Counter

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
        random_word_duplicate_letters = dict(Counter(random_word))
        
        word_lines = []
        
        word_lines.append(random_word[0])
        
        copied_list = random_word.copy()
        amount_of_letters_in_word = copied_list[1:] # skips the 0 index and only returns all the values after index 0
        

        for letter in amount_of_letters_in_word:
            print(letter)
            if letter != '' or ' ':
                word_lines.append("_")
            else:
                word_lines.append("")
        
        turn = 0
        
        break_loop = False
        
        while True:
            
            if break_loop == True:
                break
            
            if turn == 5:
                print(random_word)
                break
                
            for _ in range(5):
                turn += 1
                print(turn)
                guessed_word = '  '.join(word_lines)
                print(guessed_word)
                user_guess = list(input("guess the word:  "))
                user_guess_duplicate_keys = {word: 0 for word in user_guess}
                
                index = 0
                
                if len(user_guess) > len(random_word):
                    print("this word is too long!")
                    continue
                if len(user_guess) < len(random_word):
                    print("this word is too short!")
                    continue
                
                
                for letter in user_guess:
                    
                    word_lines[index] = letter
                    user_guess_duplicate_keys[letter] += 1
                    
                    if(letter not in random_word):
                        word_lines[index] = letter
                    if(letter in random_word):    
                        word_lines[index] = f"\033[93m{letter}\033[0m"
                    if letter == random_word[index]:
                        if letter in word_lines:
                            continue
                        else: 
                            word_lines[index] = f"\033[92m{letter}\033[0m"
                    try:
                        if user_guess_duplicate_keys[letter] > random_word_duplicate_letters[letter]:
                            word_lines[index] = letter
                    except KeyError:
                        continue
                        
                        
                    index += 1
                
                print(user_guess_duplicate_keys)
                
                if user_guess == random_word:
                    print("you guessed the word!")
                    break_loop = True
                    break
                
            
    
        
    