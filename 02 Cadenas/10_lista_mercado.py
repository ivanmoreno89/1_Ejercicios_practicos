# Escribir un programa que pregunte por consola por los productos
# de una cesta de la compra, separados por comas, y muestre por
# pantalla cada uno de los productos en una línea distinta.

mercado = input("Escriba la lista de mercado separada solo por comas: ")

productos = (mercado.split(", "))

for producto in productos:
    print(producto)


# print("\n".join(mercado.split(", ")))