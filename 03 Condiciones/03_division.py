# Escribir un programa que pida al usuario dos números
# y muestre por pantalla su división. Si el divisor es
# cero el programa debe mostrar un error.

numero1 = int(input("Escriba un primer valor: "))
numero2 = int(input("Escriba un segundo valor: "))

if numero2 != 0:
    print(f"El resultado de la division es {float(numero1)/(numero2)}")
else:
    print("Error. El divisor no puede ser 0")