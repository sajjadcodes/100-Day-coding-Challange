from art import logo
import random

def card_play():
    yes = ''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    your_cards = []
    computer_cards = []
    yours_total = 0
    computer_total = 0
    yes = input("want to play a game of Blackjack? Type 'y' or 'n'").lower()
    if yes == 'y' and (yours_total < 21 and computer_total < 21):
        your_cards.append(random.choice(cards))
        your_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        print(your_cards)
        for item in range(len(your_cards)):
            yours_total +=your_cards[item]
            
        for item in range(len(computer_cards)):
            computer_total += computer_cards[item]
        print(f"Your cards: {your_cards}, current score: {yours_total}")
        print(f"Computer's first card: {computer_total}")

        yes = input("type 'y' to get another card, type 'n' to pass:")
    else:
        print("our final hand: {your_cards}, final score: {yours_total}")
        print("Computer's final hand: {computer_cards}, final score: {computer_total}")
if yours_total > computer_total and yours_total <= 21:
    print("You win")
elif yours_total < computer_total and computer_total <= 21:
    print("You lose")
elif computer_total == yours_total:
    print("Draw")
else:
    print("Bust")

card_play()
#def card_play(play):
 #   while play == True:
  #      print(logo)
        

#if blackjack == 'y':
 #   play == True
  #  card_play(play)
#else:
 #   play == False



#blackjack = input("Type 'y' to get another card, type 'n' to pass:")
#if blackjack == 'yes':
 #   play = True
#  card_play(play)
#else:
#   play = False
    
    