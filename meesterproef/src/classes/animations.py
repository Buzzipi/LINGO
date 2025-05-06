from src.data.art import *
import time
import os


class animations:
    @staticmethod
    def intro():
        os.system('cls')
        
        time.sleep(2)
        print(lingo_title)
        time.sleep(2)
        
        for line in text_banner_lingo:
            time.sleep(0.2)
            print(line)
    
        print() 
        
        print()
        time.sleep(2)
        os.system('cls')
    
    @staticmethod
    def outro():
        print()
        print()
        for line in outro_banner:
            time.sleep(0.2)
            print(line)
    
    @staticmethod
    def main_menu():
        print()
        print()
        print("----[:MAIN MENU:]----")
        print("- play:  (type: P)")
        print("- quit:  (type: Q)")
        print()
        print()
        
        
