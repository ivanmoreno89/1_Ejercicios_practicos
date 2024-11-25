# Escribir un programa que pida al usuario una palabra
# y luego muestre por pantalla una a una las letras de
# la palabra introducida empezando por la última.


""" [Resumen]

Entradas:
Variable_01 (Tipo): [Descripción]
Variable_02 (Tipo): [Descripción]

Salidas:
(Tipo): Resultado esperado """

palabra = input("Introduzca una palabra:\n")
palabra_invertida = reversed(palabra)
for n in palabra_invertida:
    print(n, sep="\n")