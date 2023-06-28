from  wonderwords import RandomWord
import os


# clear screen
def clr(): 
    return os.system('cls')


# choose level and word
def level() -> str:
    r = RandomWord()

    choice = None
    while choice not in [1, 2, 3]:
        choice = int(input("Choose \033[32m1\033[0m, \033[33m2\033[0m or \033[91m3\033[0m as level:\n\n\033[32m1. Easy\n\033[33m2. Intermediate\n\033[91m3. Hard\n\033[0m"))
        clr()
    match choice:
        case 1:
            return [r.word(word_min_length=8, word_max_length=14), 1, 91]
        case 2:
           return [r.word(word_min_length=5, word_max_length=8), 2, 61]
        case 3:
            return [r.word(word_max_length=5), 3, 41]

# color the drawings
def color(num:int, picture:str):
    match num:
        case 1:
            return "\033[96m{}\033[0m".format(picture)
        case 2:
            return "\033[93m{}\033[0m".format(picture)
        case 3:
            return "\033[35m{}\033[0m".format(picture)

# display frequent text           
def textDisplay(num:int, word:str, players:dict):
    print("\nThe word was: \033[33m{}\033[0m\n".format(word))
    print("{}'s Score: \033[33m{}\033[0m      {}'s Score: \033[33m{}\033[0m".format(list(players.keys())[0], list(players.values())[0],list(players.keys())[1], list(players.values())[1])) if num == 2 else None