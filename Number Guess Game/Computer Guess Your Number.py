import random

def play():
    low,high=1,100
    feedback=''
    tries=0
    print("lets start the game! ill start guessing now".title())
    while feedback != 'C':
        if low != high:
            guess=random.randint(low,high)
        else:
            guess=low
        tries+=1
        print(f"Is it {guess}?")
        #input H for high, L for low, C for correct
        feedback=input()
        if feedback != 'C':
            print("Oops, Ill try again!")
            if feedback=='H':
                high=guess-1
            else:
                low=guess+1
    print(f"Yay I won! It only took {tries} tries!")

play()
