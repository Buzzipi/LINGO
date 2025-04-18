from src.data.art import *
import time


class animations:
    @staticmethod
    def intro():
        for line in text_banner_lingo:
            time.sleep(0.2)
            print(line)
    
        print() 

        time.sleep(2)
        print(lingo_title)
        time.sleep(2)
        
        print()
    
    @staticmethod
    def outro():
        print()
        print()
        for line in outro_banner:
            time.sleep(0.2)
            print(line)
        
