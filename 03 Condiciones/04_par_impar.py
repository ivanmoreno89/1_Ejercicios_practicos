# Escribir un programa que pida al usuario un número
# entero y muestre por pantalla si es par o impar.

entero = int(input("Ingrese un número entero: "))

if entero%2 == 0:
    print(f"El número {entero} es par")
else:
    print(f"El número {entero} es impar")
