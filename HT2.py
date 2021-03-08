## EJERCICIO No. 1
print("EJERCICIO No. 1")
print("=================")
numr = int(input("Ingrese un número entero para la altura del triangulo: "))
for i in range(numr):
    for j in range(i+1):
        print("*", end="")
    print("")

## EJERCICIO No. 2
print("")
print("EJERCICIO NO. 2")
print("=================")
numr = int(input("Ingrese un número entero positivo: "))
for i in range(numr, -1, -1):
    print(i, end=", ")

## EJERCICIO 3
print("")
print("EJERCICIO No. 3")
print("=================")
numr = int(input("Introduce un numero para ver si es primo: "))
for i in range(1, numr):
    if numr % i == 0:
        break
if (i + 1)  == numr:
    print(str(numr) + " es un numero primo")
else: 
    print(str(numr) + " no es un numero primo")
    print("Gracias:")