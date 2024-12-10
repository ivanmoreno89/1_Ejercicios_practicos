# Escribir un programa que pida al usuario que introduzca una
# frase en la consola y muestre por pantalla la frase invertida.

""" Contador de letras

Entradas:
frase (str): frase ingresada por el usuario

Salidas:
(str): print de frase invertida y contador de letra"""

frase = input("Introduce una frase: ")
print(frase[::-1])

print(frase.count("e"))