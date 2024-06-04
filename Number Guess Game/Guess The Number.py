import random

def play():
    print("Game Begins! You have to guess a number between 1 and 100")
    random_num=random.randint(1,100)
    guess = None
    tries=0
    while guess != random_num:
        guess=int(input("Enter your Guess: "))
        tries+=1
        if guess > random_num:
            print("Sorry, Wrong Guess. Too High.")
        elif guess < random_num:
            print("Sorry,Wrong Guess. Too Low.")
    print(f"Congrats! You guessed the number {guess} correctly \
and it only took {tries} tries")

play()
