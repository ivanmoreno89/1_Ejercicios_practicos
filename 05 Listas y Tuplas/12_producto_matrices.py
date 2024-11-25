# Escribir un programa que almacene las matrices
# A = [[1, 2, 3], [4, 5, 6]]
# B = [[-1, 0, 1], [0, 1, 1]]
# en una lista y muestre por pantalla su producto.
# Nota: Para representar matrices mediante listas
# usar listas anidadas, representando cada vector
# fila en una lista.

""" [Resumen]

Entradas:
Variable_01 (Tipo): [Descripción]
Variable_02 (Tipo): [Descripción]

Salidas:
(Tipo): Resultado esperado """

# Variables de entrada
matriz_a = [[1, 2, 3],
            [4, 5, 6]]
matriz_b = [[-1, 0],
            [0, 1],
            [1, 1]]
matriz_c = [[0, 0],
            [0, 0]]

for i in range(len(matriz_a)):
    for j in range(len(matriz_b[0])):
        for k in range(len(matriz_b)):
            matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j]
for i in range(len(matriz_c)):
    matriz_c[i] = tuple(matriz_c[i])
matriz_c = tuple(matriz_c)
for i in range(len(matriz_c)):
    print(matriz_c[i])
