# **Hangman Game...**

### _Done by:  The Bug Hunting Pythons._  :bug:🦗:bug:

<p align="center">
  <img src="https://user-images.githubusercontent.com/124607045/236589667-741812cd-a5f3-4fd6-b797-b63bd8582732.png" alt="Sublime's custom image"/>
</p>

* **Team members:**  Jana Rubiano Hurtado, Samuel Villamizar & Ana Maria De Felipe Briñez.

---

Welcome to this repository in which we would like to show you the development of the hangman game through Python programming code.

First of all, we will present the index of what you can find in this repository.

**Index:**
* Explanation of the development of the hangman game code.
   * Pseudocode of the basic code structure.
   * Each function explanation. 
* Steps to install the game.
* How to use the code.
* References. 

---

##  _Explanation of the development of the hangman game code._  :woman_technologist::woman_technologist::man_technologist:

In the first place, the basic structure of the code was planned by means of a pseudocode. 

 `Pseudocode of the basic code structure. `

```mermaid
flowchart TD
    A[Begin.] -->B(Print: Welcome to the hangman game.) -->C(Show game levels.)
    --> D("Level 1: Easy.
    Level 2: Intermediate.
    Level 3: Hard.")
    --> E(Allow the user to choose a level.)
    E --> F(Level: Easy.) --> I(" • X attempts
    • 2 ↔ 5 letters in the word.
    ") -->L
    E --> G(Level: Intermediate.) --> J(" •  X attempts
    • 6 ↔ 8 letters in the word.
    ") -->L
    E --> H(Level: Hard.) --> K(" •  X attempts
   •  9 ↔ 19 letters in the word.
    ") 
    --> L(" • Generate a random word using a Python library that corresponds to the game difficulty.
     •  Print a hangman design corresponding to the game difficulty.
     •  Print underscores representing the length of the random word.
    ") 
    --> W(Allow the user to enter a letter.)
    --> R{Does the entered letter belong to the generated word?}
    R -->n(No) --> q("• Add the word to the list.
    • Print part of the hangman design.
    • Print the failed letters.
    • Indicate a lost attempt.
    ") -->u{Has the user lost all its attempts?}
    u -->o(Yes) -->S("Game over. 
    Show the correct word. 
    ") --> P
    u--> t(No) --> W
    
    R -->Y(Yes) --> T(" • Add the word to the list.
    • Print the updated underscores with the letter.
    • Compare the list with the string of the generated word.
    ") -->U{Is the word completed?} 
    U -->O(Yes) --> k(Print: Congratulations)
    --> P(Ask the user if he/she wants to play again)
    P --> b(No) --> w[End]
    P--> a(Yes) -->C
    U --> i(No) -->W
   
```
---
Secondly, we will begin to explain the operation of each function of the code.

To enable the functionality of the game code, three main libraries were imported.

1. **Time:** This library is used to manage a timer in the code. It allows for the creation of a countdown that controls the user's playing time.
2. **RandomWord:** This library can be installed using the command prompt (cmd) and enables the generation of random words with varying lengths and categories.
3. **Os:** This library allows access to the operating system, enabling interaction with various system functionalities.

 `libraries`
 
```Python
from  wonderwords import RandomWord
import time
import os
```

---
##  _Steps to install the game._ :open_file_folder::memo:

---
##  _How to use the code._ :tada:

---
##  _References._ :mag_right:
