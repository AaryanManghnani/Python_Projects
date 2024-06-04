import random
import re

import random
from string import ascii_uppercase

handle=open(r"C:\Users\aarya\OneDrive\Desktop\Python Projects\hangman_words.txt")

string=handle.read()
word_list=re.findall('\w+',string) #finds all word characters

def valid_word(word_list):
    word=random.choice(word_list)
    while '-' in word:
        word=random.choice(word_list)
    return word.upper()

def hangman():
    global word_list
    word=valid_word(word_list)
    word_letters=set(word)       
    alpha = set(ascii_uppercase)   
    used_letters=set()         
    print('Lets Start!')
    print('_ '*len(word))
    lives=6

    while len(word_letters)>0 and lives>0:
        print('Lives left: ',lives)
        print('Already Guessed Words: ', ','.join(used_letters))
        user_letter=input('Guess a letter: ').upper()
        if user_letter in alpha - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
               word_letters.remove(user_letter)
            else:
                lives-=1
                print("Wrong Guess")

        elif user_letter in used_letters:
            print('You already guessed that word. Try something else.')
    
        else:
            print('Invalid Character. Try something else.')
        word_list=[letter if letter in used_letters else '_'for letter in word]
        print(' '.join(word_list))

    if(lives==0):
        print("Game Over. The word was ",word)
    else:
        print("Good Game")
        
hangman()
