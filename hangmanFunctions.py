from  wonderwords import RandomWord
import time
import os


def clr():
    return os.system('cls')

def timer():
    for sec in range(180, -1, -1):
        time.sleep(1)
        if sec%60 > 9:
            t = str(sec//60) +":" + str(sec%60)
        else:
            t = str(sec//60) +":0" + str(sec%60)[0]
        print(t, end='\r')

    return "You ran out of time!"


def level() -> str:
    r = RandomWord()

    choice = None
    while choice not in [1, 2, 3]:
        choice = int(input("Choose \033[32m1\033[0m, \033[33m2\033[0m or \033[91m3\033[0m as level:\n\n\033[32m1. Easy\n\033[33m2. Intermediate\n\033[91m3. Hard\n\033[0m"))
        clr()
    match choice:
        case 1:
            info = [r.word(word_min_length=8, word_max_length=19), 1]
        case 2:
            info = [r.word(word_min_length=5, word_max_length=8), 2]
        case 3:
            info = [r.word(word_max_length=5), 3]

    return info

def color(num:int, picture:str):
    choice = num
    match choice:
        case 1:
            c = "\033[96m{}\033[0m".format(picture)
            return c
        case 2:
            c = "\033[93m{}\033[0m".format(picture)
            return c
        case 3:
            c = "\033[35m{}\033[0m".format(picture)
            return c
