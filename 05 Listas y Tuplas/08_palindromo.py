# Escribir un programa que pida al usuario una palabra
# y muestre por pantalla si es un palíndromo.

""" [Resumen]

Entradas:
Variable_01 (Tipo): [Descripción]
Variable_02 (Tipo): [Descripción]

Salidas:
(Tipo): Resultado esperado """

#variables
palabra = list(str(input("Escriba una palabra:\n")))
palindromo = list(reversed(palabra))

#bucle 
if palabra == palindromo:
    print(f"La palabra {palabra} es un Palindromo")
else:
    print(f"La palabra {palabra} no es un Palindromo")
