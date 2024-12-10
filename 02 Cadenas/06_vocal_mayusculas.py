# Escribir un programa que pida al usuario que introduzca una
# frase en la consola y una vocal, y después muestre por pantalla
# la misma frase pero con la vocal introducida en mayúscula.

""" Vocal a mayusculas

Entradas:
frase (str): frase ingresada por el usuario
vocal (str): vocal ingresada por el usuario

Salidas:
(str): print con vocal ingresada en mayuscula """

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula:  ")
print(frase.replace(vocal, vocal.upper()))