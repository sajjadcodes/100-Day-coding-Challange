if 3 > 2:
    a_variable = 10
#it will not treated as a block level. it will the
#level of if exist if whtin a funcion it will be scope to the function
# Else it will treat the Global variable

game_level = 3

enemies = ["Skeleton", 'Zombie', 'Alien']

if game_level < 5:
    new_enemy = enemies[0]

#all though new_enemy is created inside the if block. but it is accessible outside the block
print(new_enemy)

# Within function
def create_enemy():
    nemeies_list = ["Skeleton","zombie", "Alien"]
    if game_leve < 3:
        your_enemy = nemeies_list[0]
    print(your_enemy)
    

#will not accessbile outside the function. Because,it is not within a function. So it has scope inside the function
#print(your_enemy)