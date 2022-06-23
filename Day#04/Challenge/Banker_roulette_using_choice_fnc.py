import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

person_to_pay = random.choice(names)

print(person_to_pay + " is going to pay bill today.!")