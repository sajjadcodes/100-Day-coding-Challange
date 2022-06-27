#https://reeborg.ca/docs/en/
#http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fselect_collection_en.json&name=Alone&url=%2Fworlds%2Ftutorial_en%2Falone.json
def jump():
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
for i in range(1,12,3):
    move()
    jump()