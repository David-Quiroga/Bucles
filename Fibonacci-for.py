# Mostrar series de Fibonacci hasta 10 términos

def fibo(n):
    a = 1 
    b = 1
    if n == 1:
        print("0")
    elif n == 2:
        print("0", "1")
    else:
        print("0")
        print(a)
        print(a)
        for i in range(n - 3):
            total = a + b
            b = a
            a = total
            print(total)

fibo(10)
    
