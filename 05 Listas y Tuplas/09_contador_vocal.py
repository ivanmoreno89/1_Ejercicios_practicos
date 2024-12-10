# Escribir un programa que pida al usuario una
# palabra y muestre por pantalla el número de
# veces que contiene cada vocal.


""" Contador de vocales en palabra

Entradas:
palabra (str): Palabra ingresada
vocales (str, lista): Vocales para conteo

Salidas:
(str): Mensaje indicando la cantidad por cada vocal """

# variables de entrada
palabra = str(input("Ingrese una palabra:\n"))
vocales = ["a", "e", "i", "o", "u"]

for vocal in vocales:
    n = 0
    for letra in palabra:
        if vocal == letra:
            n += 1
    # Resultado
    print(f"La letra {vocal} en la palabra {palabra} se encuentra {n} veces")