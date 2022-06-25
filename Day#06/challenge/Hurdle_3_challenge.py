#URL_https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
#wall_in_front()
#front_is_clear()
#at_goal()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
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
    
    

while not at_goal():
    if front_is_clear():
      move()
    elif wall_in_front():
      jump()
      