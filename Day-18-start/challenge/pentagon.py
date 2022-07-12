from turtle import Turtle, Screen

pen = Turtle()

num_sides = 5

for _ in range(num_sides):
    angle = 360 / num_sides
    pen.forward(100)
    pen.right(angle)
    
screen = Screen()
screen.exitonclick()