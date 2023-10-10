import turtle
import random
  
# creating turtle pen
tim = turtle.Turtle()
  
# taking input for the side of the square

  
# taking the input for the color
list=["red","green","purple","black","orange"]

col=random.choice(list)
# set the fillcolor
for color in ["red","green","purple","black","orange","yellow"]:
    tim.fillcolor(color)
  
# start the filling color
tim.begin_fill()
  
# drawing the square of side s
for _ in range(4):
  tim.forward(200)
  tim.right(90)
  
# ending the filling of the color
tim.end_fill()