
from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_cards = []
user_cards = []
blackjack = []
def blackjack(arr,ace,ten):
    if ace in arr and ten in arr:
        return True
    else:
        return False
    
def play_card():
    print(logo)
    your_card = []
    opponent_card = []
    your_card = random.choices(cards)
    your_card = random.choices(cards)
    opponent_card = random.choices(cards)
    opponent_card = random.choices(cards)
    
    print(your_card)
    print(opponent_card)
    
    for card in range(len(your_card)):
        user_cards.append(your_card[card])
        if card == '11':
            blackjack.append(card)
        if card == '10':
            blackjack.append(card)
            
            
   
    for card in range(len(opponent_card)):
        computer_cards.append(opponent_card[card])
        
    user_score = 0
    user_score = sum(user_cards)
    computer_score = 0
    computer_score = sum(computer_cards)
    
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_score}") 


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

arr= [10,3,2,4]
ace =11
ten = 10
print(blackjack(arr,ace,ten))
#while play == 'y':
 # play_card()
  #play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    




