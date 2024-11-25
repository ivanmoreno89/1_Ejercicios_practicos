# Escribir un programa que pregunte el nombre del usuario en la
# consola y un número entero e imprima por pantalla en líneas
# distintas el nombre del usuario tantas veces como el número
# introducido.

nombre = input("Ingrese su nombre: ")
numero_entero = int(input("Escriba un valor entero de 1 a 10: "))

# i = 1
# while i <= numero_entero:
#     print(nombre)
#     i += 1

print((nombre + "\n") * int(numero_entero))