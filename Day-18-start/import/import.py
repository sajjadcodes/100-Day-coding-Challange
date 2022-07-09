from turtle import  Turtle, Screen

tim = Turtle()
tim.fillcolor('red')
tim.dot(2)

tim.forward(100)
tim.penup()
tim.forward(100)
tim.pendown()
tim.right(90)
tim.forward(100)
screen = Screen()
screen.exitonclick()
