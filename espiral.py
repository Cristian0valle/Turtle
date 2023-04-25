import turtle

# Configurar la ventana de dibujo
wn = turtle.Screen()
wn.bgcolor("black") # Fondo negro
wn.title("Animación de Espiral")
wn.setup(width=800, height=600) # Tamaño de la ventana             wn==ventana

# Configurar la tortuga
t = turtle.Turtle()
t.speed(0) # Velocidad máxima de la tortuga
t.color("cyan") # Color de la tortuga

# Animación de la espiral
for i in range(360): # Repetir 360 veces
    t.forward(i) # Avanzar la tortuga
    t.left(59) # Girar a la izquierda

# Cerrar la ventana al hacer clic
wn.exitonclick()