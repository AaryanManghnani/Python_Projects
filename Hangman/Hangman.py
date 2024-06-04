import random
from string import ascii_uppercase

handle=open(r"C:\Users\aarya\OneDrive\Desktop\Python Projects\hangman_words.txt")

string=handle.read()
string=string.replace('","' , " ")
string=string.replace('"',"")

words=string.split()

def valid_word(words):
    word=random.choice(words)
    while '-' in word:
        word=random.choice(words)
    return word.upper()

def hangman():
    word=valid_word(words)
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
        print("Game Over. The word was",word)
    else:
        print("Good Game")
        
hangman()

    






