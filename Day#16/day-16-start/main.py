import another_module
# import turtle
# We can simplify as
from turtle import Turtle, Screen

from prettytable import PrettyTable
table = PrettyTable()
print(table)
table.add_column("city Name",['Chitral', 'Peshwar', 'islamabad'])
table.add_column("Zip Code",['41', '51', '46'])
print(table)
print(another_module.another_variable)
# import turtle module and inside the class Turtle crate the object of the class call timmy
# timmy = turtle.Turtle()
# now create another object
timmy = Turtle()
# Give object address
print(timmy)

timmy.shape('turtle')
timmy.color('DarkBlue')
timmy.forward(100)

# Attributes
## car attributes , speed , feul
### accessing attributes car.speed : object:attributes
my_screen = Screen()
# height of the canvas
print(my_screen.canvheight)

#Car object: Does move(), stop() methods
## car.stop() : object.method()

my_screen.exitonclick()




