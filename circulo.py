import turtle


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Animación de Flor")
wn.setup(width=800, height=600) # Tamaño de la ventana


t = turtle.Turtle()
t.speed(0)
t.color("cyan")

# Animación de la flor
for i in range(72): 
    for j in range(4): 
        t.forward(100) 
        t.left(90) 
    t.right(5) 

    
    if i % 2 == 0:     		# Cambiar el color de la tortuga
        t.color("magenta")
    else:
        t.color("cyan")


wn.exitonclick()