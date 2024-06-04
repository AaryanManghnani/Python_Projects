import random

def play():
    print("lets start the game".title())
    result = None
    while result != 1 :
        user=input("Pick R for Rock, P for Paper, S for Scissors ")
        comp=random.choice(['R','P','S'])
        show(comp)
        if user==comp:
            print("Tie. Go again!")
            result = 0
        if(user=='R' and comp=='S')or(user=='S' and comp=='P')\
                     or(user=='P' and comp=='R'):
            print("You Won!")
            again=input("Press X to play again!")
            if again == 'X':
                result = 0
            else:
                result =1
        elif(user=='S' and comp=='R')or(user=='P' and comp=='S')\
                       or(user=='R' and comp=='P'):
            print("You Lose!")
            again=input("Press X to play again!")
            if again == 'X':
                result = 0
            else:
                result =1
    print("Thanks for Playing")       
            
def show(comp):
    if comp == 'R':
        print("Computer picked Rock")
    elif comp == 'P':
        print("Computer picked Paper")
    else:
        print("Computer picked Scissors")

play()
