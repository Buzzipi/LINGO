import random
from collections import Counter
from src.data.lingowords import *

class Mastermind:
    def random_selected_word(self, words_list):
        randomly_selected_word = random.choice(words_list)
        return randomly_selected_word
    
    def prepare_word(self, word_lines, random_word):
        word_lines.append(random_word[0])
        
        copied_list = random_word.copy()
        amount_of_letters_in_word = copied_list[1:] # skips the 0 index and only returns all the values after index 0
        

        for letter in amount_of_letters_in_word:
            # print(letter)
            if letter != '' or ' ':
                word_lines.append("_")
            else:
                word_lines.append("")
    
    def word_guessing_logic(self, random_word, word_lines, random_word_duplicate_letters, team):
        turn = 0
        
        break_loop = False
        
        while True:
            
            if break_loop == True:
                break
            
            if turn == 5:
                print_random_word = ''.join(random_word)
                print()
                print("you're sadly out of guessing attempts :(")
                print(f"the word was: \033[96m{print_random_word}\033[0m")
                print()
                team.amountOfFailedGuessedWords += 1
                break
                
            for _ in range(5):
                turn += 1
                
                if turn < 5:
                    print()
                    print(f"\033[93mturn: {turn}\033[0m")
                    print()
                elif turn == 5:
                    print()
                    print(f"\033[91mturn: {turn}\033[0m")
                    print()
                    
                guessed_word = '  '.join(word_lines)
                print(guessed_word)
                user_guess = input(f"{team.team_name}'s turn too guess the word:  ").lower()
                user_guess_list = list(user_guess)
                user_guess_duplicate_keys = {word: 0 for word in user_guess_list}
                
                index = 0
                
                if len(user_guess_list) > len(random_word):
                    print("this word is too long!")
                    continue
                if len(user_guess_list) < len(random_word):
                    print("this word is too short!")
                    continue
                
                
                for letter in user_guess_list:
                    
                    word_lines[index] = letter
                    user_guess_duplicate_keys[letter] += 1
                    
                    #if letter not in random word, letter turns gray
                    if(letter not in random_word):
                        word_lines[index] = letter
                        index += 1
                        continue
                    
                    # word turns yellow if it's in the random word 
                    if(letter in random_word): 
                        word_lines[index] = f"\033[93m\033[1m{letter}\033[0m\033[0m"
                        
                        #check for duplicate letters in word
                        try:
                            if user_guess_duplicate_keys[letter] > random_word_duplicate_letters[letter]:
                                word_lines[index] = letter
                                index += 1
                                continue
                        except KeyError:
                            continue
                        
                        # word turns green if it is in the random word, and on the same index 
                        if letter == random_word[index]:
                            word_lines[index] = f"\033[92m\033[1m{letter}\033[0m\033[0m"
                        index += 1
                        continue
                        
                        
                    index += 1
                
                if user_guess_list == random_word:
                    print(f"\033[92m{team.team_name} guessed the word!\033[0m")
                    break_loop = True
                    team.amountOfGuessedWords += 1
                    team.amountOfFailedGuessedWords = 0
                    break
          
    def mastermind_game(self, team):
        random_word = list(self.random_selected_word(words))
        random_word_duplicate_letters = dict(Counter(random_word))
        
        
        word_lines = []
        
        self.prepare_word(word_lines, random_word)
    
        self.word_guessing_logic(random_word, word_lines, random_word_duplicate_letters, team)