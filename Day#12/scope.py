enemies = 1

def increase_enemies():
    enemies =2
    print(f"enemies inside function: {enemies}")

increase_enemies()

print(f"enemies outside function: {enemies}")

# Local Scope
# when you create variable inside the function.It is accessible only inside
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# not accessible; error NameError
#print(potion_strength)

# Global Scope
# Define top level of the file. Means it is not within a function
# Global variable access everywhere. No matter how deep the function level is.
play_health  = 10

def drink_potion_1():
    potion_strength = 2
    print(play_health)
drink_potion_1()

#Namespace: 