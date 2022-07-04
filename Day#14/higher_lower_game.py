from art import logo, vs

import random

data = [
 {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    }
    ]


print(logo)

account_a = random.choice(data)
account_b = random.choice(data)


print(account_a)
print("--------------------------------------------")
print(account_b)
print(f"Compare A: {account_a['name']}, {account_a['description']}, from {account_a['country']}.")
print(f"Compare B: {account_b['name']}, {account_b['description']}, from {account_b['country']}.")
choice = input("Who has more followers? Type 'A' or 'B': ").lower()

if choice == 'a':
    print("user selected A")

if choice == 'b':
    print("User Selected B")

#print(ran_a[0]['follower_count'])
#if ran_a[0]['follower_count'] > ran_b[0]['follower_count']:
 #   print(ran_a[0]['name'])
#else:
 #   print(ran_b[0]['name'])