from time import sleep
from hangmanFunctions import *
from json import load
from threading import Event
from threading import Thread

# countadown with threading
def countdown(tm, event): 
    
    global timer # declare global var for time in seconds
    timer = tm
    for sec in range(tm): # loop n times based on the argument
        timer -= 1 # countdown
        sleep(1)
        print("\t\t\t{}:{}".format(timer//60, timer%60) if timer%60 > 9 else "\t\t\t{}:0{}".format(timer//60, timer%60), end='\r') # print minutes and seconds
        if event.is_set(): # if event is set, kill the thread
            break
    print("\n\033[31mYou ran out of time!\033[0m ...click on any letter to exit") # print message when loop ends
    
    

def hangman(drawings, num):

    print(*drawings[3]) # print title

    players = {input("Name player {}: ".format(i + 1)) :0 for i in range(num)} if num == 2 else {"None":0} # ask names and initialize score when 2 players

    info = level() # choose level and generate word
    num_lev = info[1] # number of level (1, 2 or 3)
    tm = info[2] # game time
    word = info[0].upper() # word to be guessed
    drawing = drawings[num_lev-1] # chosen drawing according to level
    tries = len(drawing) - 1 # chosen level
    failed_letts = [] # store failed letters
    word_fill = list(len(word) * "_") # blank spaces (_ _)

    clr() # clear screen
    print("\033[103mYou have {} tries\033[0m".format(tries))
    print(color(num_lev, drawing[0])) # print first drawing
    print(" ".join(word_fill)) # print blank spaces
    turn = 1 # set turn to player 1
    
    event = Event() # create and event
    countdown_thread = Thread(target=countdown, args=(tm, event)) # create thread
    countdown_thread.start() # initialize thread (countdown starts)
    
    while word_fill != list(word) and timer > 0: # code block will run unless the word is found and there is still time
        char = ""
        while not char.isalpha() or len(char) != 1: # the program only accepts alphabetic characters of length one
            char = input("\n{} enter a letter: \n".format(list(players.keys())[turn-1])).upper() if num == 2 else input("\nEnter a letter: \n").upper() # letter 
            clr()

        if timer == 0: # check time
            event.set() # stop the clock
            countdown_thread.join() # kill thread
            textDisplay(num, word, players) # display text
            return

        elif char in word and char not in failed_letts: # when a letter is found
            inds = [i for i in range(len(word)) if word[i] == char] # indices where the letter is found
            players[list(players.keys())[turn-1]] += len(inds)  # sums the number of guessed letters to player x
            for ind in inds: # replace every blank space with the letter
                word_fill.pop(ind)
                word_fill.insert(ind, char)

        elif char in failed_letts: # when letter was already inputted
            print("Try a new letter!")
            sleep(2)

        else:
            failed_letts.append(char) # when letter is not in the word

            if tries == len(failed_letts): # check if number of tries is met
                event.set() # stop the clock
                countdown_thread.join()
                clr() 
                print(color(num_lev, drawing[len(failed_letts)])) # print last drawing
                print("\033[31m\nGame Over!\033[0m")
                textDisplay(num, word, players)

                return 
            
        clr()
        print("\033[103mYou have {} tries left\033[0m".format(tries-len(failed_letts))) if tries-len(failed_letts) > 1 else print("\033[103mYou have 1 try left\033[0m")
        print(color(num_lev, drawing[len(failed_letts)])) # print current drawing based on failed letters
        print(" ".join(word_fill)) # print word with guessed letters and blank spaces
        print("\033[31m\nFailed letters:\033[0m", " ".join(failed_letts)) # print failed letters
        if num == 2:
            turn = 1 if turn == 2 else 2 # assign the turn to the next player

    else: # word found
        event.set() # stop clock
        countdown_thread.join() # kill thread
        clr()
        print("\033[32mYou won!\033[0m")
        textDisplay(num, word, players)
    
    return 



if __name__ == "__main__":
    answer = "yes"   
    with open("drawings.json") as file:
        drawings = load(file) 
        
    while answer.lower() == "yes":
        num = int(input("\033[92mFor 1 or 2 players?\033[0m\n"))
        clr()
        hangman(drawings, num)
        answer = input("\033[94mDo you want to play again? (Yes/No): \033[0m")
        clr()
