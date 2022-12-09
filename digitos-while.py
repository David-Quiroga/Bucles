# Dado un número, cuente el número total de dígitos de un número
# * Por ejemplo, el número es 75869, por lo que la salida debería ser 5

numero = int(input("Ingrese una cantidad de numeros positivos: "))

contador = int(1);
control = int(10);

while control <= numero:
    contador = contador + 1;
    control = control * 10;
print ("La cantidad de digitos en " +str(numero)+" es de: " +str(contador));
    