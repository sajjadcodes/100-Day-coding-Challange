import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock,paper,scissors]

choice = int(input("What do you Choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

rand_shape = random.choice(game)

if game[choice] == rand_shape:
    print(game[choice])
    print(rand_shape)
    print("Game Draw")

elif game[choice] == game[0] and rand_shape== game[2]:
    print(game[choice])
    print(rand_shape)
    print("You Won.!")

elif game[choice] == game[2] and rand_shape == game[1]:
    print(game[choice])
    print(rand_shape)
    print("You Again Won")
else:
    print(game[choice])
    print(rand_shape)
    print("You loss")
