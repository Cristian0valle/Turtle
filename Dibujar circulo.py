import turtle

wn = turtle.Screen()  # Configurar la ventana
wn.bgcolor("black")
wn.title("Círculo Centrado")
wn.setup(width=1.0, height=1.0)

t = turtle.Turtle()
t.speed(0)
t.color("red")

radius = min(wn.window_width() // 2, wn.window_height() // 2) - 50 # Calcular el radio del círculo

t.penup()
t.goto(0, -radius)
t.pendown()

for i in range(360):
    t.forward(radius * 2 * 3.1415 / 360)
    t.left(1)

wn.exitonclick()