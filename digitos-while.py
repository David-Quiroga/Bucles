# Dado un número, cuente el número total de dígitos de un número
# * Por ejemplo, el número es 75869, por lo que la salida debería ser 5

# Con input le pedimos al usuaro que ingrese los numeros y con el int le transformamos a entero
# Y lo guardamos a la variable numero
numero = int(input("Ingrese una cantidad de numeros positivos: "))

# A contador y control lo inicializamos como entero
contador = int(1);
control = int(10);
# Mientras control sea menor a numero, el contaodr se sumara por 1 
# y el control se multiplica por 10
while control <= numero:
    contador = contador + 1;
    control = control * 10;
# Con el print mostramos en consola el resultado y concatenamos el numero y contador
print ("La cantidad de digitos en " +str(numero)+" es de: " +str(contador));
    