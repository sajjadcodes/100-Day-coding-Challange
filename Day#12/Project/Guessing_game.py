from random import randint
from art import logo

EASY_NUMBER = 10
HARD_NUMBER = 5
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard'")
if choice == "hard":
    print("hard")
if choice == "easy":
    print("Easy")

# while choice > 0:
#     print(f"You have {choice} attempts remaining to guess the number")
