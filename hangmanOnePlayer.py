import time
from hangmanFunctions import *
import json



def hangMan(drawings):

    print(*drawings[3]) # print title

    info = level() # choose level and generate word
    num_lev = info[1]
    word = info[0].upper() # word to be guessed
    drawing = drawings[info[1]-1] # chosen drawing according to level
    tries = len(drawing) - 1 # chosen level
    failed_letts = [] # store failed letters
    word_fill = list(len(word) * "_") # blank spaces (_ _)

    clr() # clear screen

    print(color(num_lev, drawing[0])) # print first drawing
    print(" ".join(word_fill)) # print blank spaces
    while word_fill != list(word) and len(failed_letts) <= tries:
        char = input("\nEnter a letter: \n").upper() # letter 
        #print(timer())
        
        if char in word and char not in failed_letts: # when a letter is found
            inds = [i for i in range(len(word)) if word[i] == char] # indices where the letter is found
            for ind in inds: # replace every blank space with the letter
                word_fill.pop(ind)
                word_fill.insert(ind, char)
        elif char in failed_letts: # when letter was already inputted
            print("Try a new letter!")
            time.sleep(2)
        else:
            failed_letts.append(char) # when letter is not in the word
            if tries == len(failed_letts): # check if number of tries is met
                clr() 
                print(color(num_lev, drawing[len(failed_letts)])) # print last drawing
                print("\033[31m\nGame Over!\033[0m")
                print("\nThe word was: \033[33m{}\033[0m\n".format(word))
                
                return "End"
        clr() 
        print(color(num_lev, drawing[len(failed_letts)])) # print current drawing based on failed letters
        print(" ".join(word_fill)) # print word with guessed letters and blank spaces
        print("\033[31m\nFailed letters:\033[0m", " ".join(failed_letts)) # print failed letters
        
    print("\033[32mYou won!\033[0m")   
    
    return "End"


answer = "yes"   
with open("drawings.json") as file:
    drawings = json.load(file) 
while answer.lower() == "yes":  
    hangMan(drawings)
    answer = input("\033[94mDo you want to play again? (Yes/No): \033[0m")

print("End")