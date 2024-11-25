# Escribir un programa que almacene los vectores
# (1,2,3) y (-1,0,2) en dos listas y muestre por
# pantalla su producto escalar.


""" [Resumen]

Entradas:
Variable_01 (Tipo): [Descripción]
Variable_02 (Tipo): [Descripción]

Salidas:
(Tipo): Resultado esperado """

vector1 = (1, 2, 3)
vector2 = (-1, 0, 2)
vector3 = []
escalar = 0

for n in range(len(vector1)):
    vector3.append(vector1[n] * vector2[n])

for valor in vector3:
    escalar += valor

print(f"El producto escalar entre {vector1} y {vector2} es {escalar}")

# for n in range(len(vector1)):
#     escalar += vector1[n]*vector2[n]

# print(f"El producto escalar entre {vector1} y {vector2} es {escalar}")
