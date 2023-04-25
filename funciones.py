def Nombres(param1, param2):
    """Esto sirve para mostrar los nombres
    """
    print(param1)
    print(param2)

Nombres("cristian", "ovalle")
   
def imprimir(texto, veces = 1): #Veces seria un valor por defecto, por lo que siempre comenzaria en 1
    print(veces * texto) 

imprimir("Eva")

def varios(p1, p2, *otros): 
    """Esta funcion tiene un numero variable de argumentos, gracias a el signo * antes del nombre del argumento
     el cual se puede seguir incrementando o si no estara vacio por defecto   """    
    for val in otros:
        print(val)
varios(1,2)
varios(1,2,3)
varios(1,2,3,4)
