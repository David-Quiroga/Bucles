# Mostrar series de Fibonacci hasta 10 términos

# Definimos una funcion que tenga los primeros valores de fibonacci
def fibo(n):
    a = 1
    b = 1
# Si n es equivalente a 1, este nos imprimira el 0
    if n == 1:
        print("0")
#Si es equivalente a 2, nos imprima el 0 y el 1
    elif n == 2:
        print("0", "1")
# Sino que impra el 0 y los valores que se le dieron a la "a" y a "b"
    else:
        print("0")
        print(a)
        print(a)
#Con este for hacemos que nos genere un rango y que nos reste los 3 ultimos numeros de la secuencia
        for i in range(n - 3):
# Aqui haremos la suceccion de fibonacci, que el total de todo
# Sea igual a la suma de a y b; Que b = a y que a = al total
            total = a + b
            b = a
            a = total
#Ahora hacemos print de la sentencia que pusimos anterior mente
            print(total)
# Por ultimo asignamos la cantidad de numeros que queremos que salgan (en este caso 10)
fibo(10)
    
