# Escribir un programa que almacene los vectores
# (1,2,3) y (-1,0,2) en dos listas y muestre por
# pantalla su producto escalar.


""" Producto Escalar

Entradas:
vector1 (list): vector 1
vector2 (list): vector 2
vector3 (list): multiplicación entre vectores 1 y 2
escalar (int): escalar del vector 3s

Salidas:
(str): print con resultado de la escalar de los vectores 1 y 2 """

vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]
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
