# Escribir un programa que pregunte al usuario los números
# ganadores de la lotería primitiva, los almacene en una
# lista y los muestre por pantalla ordenados de menor a mayor.


""" [Resumen]

Entradas:
Variable_01 (Tipo): [Descripción]
Variable_02 (Tipo): [Descripción]

Salidas:
(Tipo): Resultado esperado """

# Variables
loteria_ganadora = []

# Ciclo para ingreso de números ganadores
for numero_ganador in range(6):
    numero_ganador = int(input("Ingrese los números ganadores de la lotería (del 0 al 99):\n"))
    loteria_ganadora.append(numero_ganador)

print(loteria_ganadora)
print(sorted(loteria_ganadora))

print(f"Los números ganadores de la lotería son: {sorted(loteria_ganadora)}")

# for n in range(6):
#     loteria_ganadora.append(int(input("Ingrese los números ganadores de la lotería (del 0 al 99):\n")))

# loteria_ganadora.sort()
# print(f"los números ganadores de la lotería son: {loteria_ganadora}")
