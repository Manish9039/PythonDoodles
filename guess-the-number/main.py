import random
from art import logo

print(logo)
print("Welcome to the Number Riddle: Guess the mystery number!")
print("I'm thinking of a number between 1 and 100.")
list_of_no = []
for i in range(1, 101):
    list_of_no.append(i)

mystery_no = random.choice(list_of_no)


# print(mystery_no)

# lines 16 - 18 can be replaced by randint(1, 100)

def checker(attempt):
    while attempt != 0:
        user_guess = int(input("Make a guess: "))
        attempt -= 1
        if user_guess == mystery_no:
            attempt = 0
            print(f"You got it.The answer was {mystery_no}")
        elif user_guess > mystery_no:
            print("Too high.")
            if attempt == 0:
                print("You've run out of guesses, you lose.")
            else:
                print("Guess again")
                print(f"You have {attempt} attempts remaining to guess the number.")
        elif user_guess < mystery_no:
            print("Too low.")
            if attempt == 0:
                print("You've run out of guesses, you lose.")
            else:
                print("Guess again")
                print(f"You have {attempt} attempts remaining to guess the number.")


difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    print("You have 10 attempts remaining to guess the number.")
    checker(10)
elif difficulty == "hard":
    print("You have 5 attempts remaining to guess the number.")
    checker(5)