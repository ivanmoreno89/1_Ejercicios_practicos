# Escribir un programa que pregunte por consola el precio
# de un producto en euros con dos decimales y muestre por
# pantalla el número de euros y el número de céntimos del
# precio introducido.

precio = float(input("Ingresar el precio del producto: "))
entero = int(precio)
decimal = precio - int(precio)
print(f"La parte entera del precio es {entero} y la parte decimal es {decimal}")
# print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')
