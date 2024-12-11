# Escribir un programa que pregunte por consola el precio
# de un producto en euros con dos decimales y muestre por
# pantalla el número de euros y el número de céntimos del
# precio introducido.

""" entero decimal

Entradas:
precio (float): precio ingresado por el usuario
entero (int): entero extraido del precio
decimal (float): decimal resultado de la resta entre 'precio' y 'entero'

Salidas:
(str): print con información de entero y decimal por separado """

precio = float(input("Ingresar el precio del producto: "))
entero = int(precio)
decimal = precio - int(precio)
print(f"La parte entera del precio es {entero} y la parte decimal es {decimal}")
# print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')
