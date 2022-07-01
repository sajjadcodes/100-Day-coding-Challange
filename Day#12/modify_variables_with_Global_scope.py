#How to modify variables with Global Scope
#side-note: It is terrible ideas to call local and Global variable with same name

enemies = "Skeleton"

def incease_enemies():
    enemies = "Zombie"
    print(f"enemies inside function:{enemies}")

incease_enemies()

print(f"enemeis outside function: {enemies}")