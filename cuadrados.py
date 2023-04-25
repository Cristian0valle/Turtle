import turtle

# Configurar la ventana de dibujo
wn = turtle.Screen()
wn.bgcolor("black") # Fondo negro
wn.title("Animación de Figura Geométrica")
wn.setup(width=800, height=600) # Tamaño de la ventana

# Configurar la tortuga
t = turtle.Turtle()
t.speed(0) # Velocidad máxima de la tortuga
t.color("cyan") # Color de la tortuga

# Animación de la figura geométrica
for i in range(360): # Repetir 360 veces
    t.forward(200) # Avanzar la tortuga
    t.left(59) # Girar a la izquierda
    for j in range(4): # Repetir 4 veces
        t.forward(100) # Avanzar la tortuga
        t.right(90) # Girar a la derecha

    t.right(5) # Girar a la derecha

    # Cambiar el color de la tortuga
    if i % 2 == 0:
        t.color("magenta")
    else:
        t.color("cyan")

# Cerrar la ventana al hacer clic
wn.exitonclick()