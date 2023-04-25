from calendar import THURSDAY
import turtle

turtle.title("6")
turtle.setworldcoordinates(-200, -2000, 2000, 2000)

def draw_flower(x, y, tilt,radius):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.seth(tilt-45)
    turtle.circle(radius, 90)
    turtle.left(90)
    turtle.circle(radius, 90)

for tilt in range(0, 260, 30):
    draw_flower(0,0,tilt,1000)