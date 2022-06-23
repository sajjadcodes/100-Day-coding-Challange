import random

names_string = input("Give me everyday's names, separated by a comma")

names = names_string.split(",")

print(names)

index = len(names)
print(index)
rand_number = random.randint(0,index-1)

print(names[rand_number] + " is going to buy the meal today!")