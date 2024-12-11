# Escribir un programa que pregunte el nombre del usuario en
# la consola y después de que el usuario lo introduzca muestre
# por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el
# nombre de usuario en mayúsculas y <n> es el número de letras
# que tienen el nombre.

""" Contador de letras

Entradas:
nobmre (str): Nombre ingresado por el usuario

Salidas:
(str): print contando las letras del nombre """

nombre = input("Ingrese su nombre: ")
# print(len(nombre))

print(str(nombre) + " tiene " + str(len(nombre)) + " letras")
print(f"{nombre} tiene {len(nombre)} letras")