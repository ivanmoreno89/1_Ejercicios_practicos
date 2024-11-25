# Escribir un programa que pregunte el nombre el un producto,
# su precio y un número de unidades y muestre por pantalla
# una cadena con el nombre del producto seguido de su precio
# unitario con 6 dígitos enteros y 2 decimales, el número
# de unidades con tres dígitos y el coste total con 8 dígitos
# enteros y 2 decimales.

# producto = "Teléfono Acme"  # input("Escriba el nombre del producto: ")
# precio = 630.25             # input("Escriba el precio del producto: ")
# unidades = 200              # input("Escriba la cantidad de unidades del producto: ")

producto = input("Escriba el nombre del producto: ")
precio = float(input("Escriba el precio del producto: "))
unidades = float(input("Escriba la cantidad de unidades del producto: "))

print(f"El producto {producto} tiene un costo unitario de {precio:.2f} euros. Las {unidades:.0f} unidades del producto tienen un costo de {precio*unidades:.2f} euros")

# print('{producto}: {unidades:3d}
# unidades x {precio:9.2f}€ = {total:11.2f}€'
# .format(producto = producto,
# unidades = unidades,
# precio = precio,
# total = unidades * precio))