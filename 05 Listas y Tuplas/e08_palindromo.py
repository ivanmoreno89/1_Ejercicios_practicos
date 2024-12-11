# Escribir un programa que pida al usuario una palabra
# y muestre por pantalla si es un palíndromo.

""" Palindromo

Entradas:
palabra (str): Palabra ingresada por el usuario
palindromo (str): Palabra invertida

Salidas:
(str): Print con confirmando si la palabra es o no un palindromo """

#variables
palabra = list(str(input("Escriba una palabra:\n")))
palindromo = list(reversed(palabra))

#bucle 
if palabra == palindromo:
    print(f"La palabra {palabra} es un Palindromo")
else:
    print(f"La palabra {palabra} no es un Palindromo")
