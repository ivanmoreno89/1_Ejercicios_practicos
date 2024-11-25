# Escribir un programa para una empresa que tiene salas
# de juegos para todas las edades y quiere calcular
# de forma automática el precio que debe cobrar a sus
# clientes por entrar. El programa debe preguntar al
# usuario la edad del cliente y mostrar el precio de
# la entrada. Si el cliente es menor de 4 años puede
# entrar gratis, si tiene entre 4 y 18 años debe pagar
# 5€ y si es mayor de 18 años, 10€.

""" Dada la edad del cliente, mostrar el valor a pagar

Variables:
edad (int): Edad del cliente.
precio (int): Precio de la entrada según el cliente.

Resultado:
(str): Mensaje con la edad y cobro a realizar """

# Validación de la edad
edad = int(input("Escriba la edad del cliente: "))
precio = 0

# Condicional del precio de acuerdo con la edad
if edad < 4:
    precio = 0
elif edad < 18:
    precio = 5
elif edad >= 18:
    precio = 10
else:
    print("Validar información")

# Mensaje con el cobro al cliente según su edad
print(f"Para los clientes con {edad} años, el valor de la entrada es de {precio}€")
