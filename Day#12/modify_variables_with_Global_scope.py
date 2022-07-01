#How to modify variables with Global Scope
#side-note: It is terrible ideas to call local and Global variable with same name
# Its also not good practice to modify global scope. Return options is better  
enemies = "Skeleton"

def incease_enemies():
    enemies = "Zombie"
    print(f"enemies inside function:{enemies}")

incease_enemies()

print(f"enemeis outside function: {enemies}")


enemies_1 = 1

def incease_enemies_1():
    global enemies_1
    enemies_1 += 2
    print(f"enemies inside function:{enemies_1}")

incease_enemies_1()

print(f"enemeis outside function: {enemies_1}")