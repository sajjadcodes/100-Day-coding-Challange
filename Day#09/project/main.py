from art import logo

print(logo)

stop = "yes"
bidder_list = {}
while stop == 'yes':
    print('yes')
    name = input('What is your name? ')
    price = int(input("What is your bid: $"))
    bidder_list[name] = price
    stop = input("Are there any other bidders? Types 'yes'or 'no' ").lower()
    
   

def find_highest_amount(bidder_list):
    highest_bid = 0
    winner = ""
    for bidder in bidder_list:
        bid_amount = bidder_list[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f"the winner is {winner} with highest {highest_bid}")


find_highest_amount(bidder_list)