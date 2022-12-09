# Imprima el siguiente patrón con el ciclo for:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# Se indica el numero max. de asteriscos
n = 5

# Se usa un for in range para generar un rango y que este inicie
# desde con 1 asterisco
# Se suma uno para que nos incluya el extremo
for  i in range(1, n + 1):
#    Con este for, se indica hasta lo que indique la i
    for j in range(i):
        # Imprimimos el * y con el end hacemos que termine y que nos genero un espacio luego de un * 
        print("* ", end="")
        # Aqui generamos un salto de linea
    print()
    # Con este for se disminuye el numero de asteriscos
for i in range(n -1, 0, -1):
    # Hacemos que se genere los mismos asteriscos
    for j in range(i):
        print("* ", end="")
    print()