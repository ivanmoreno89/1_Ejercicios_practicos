# Escribir un programa que almacene las asignaturas
# de un curso (por ejemplo Matemáticas, Física, Química,
# Historia y Lengua) en una lista y la muestre por
# pantalla el mensaje Yo estudio <asignatura>, donde
# <asignatura> es cada una de las asignaturas de la lista.

""" [Resumen]

Entradas:
Variable_01 (Tipo): [Descripción]
Variable_02 (Tipo): [Descripción]

Salidas:
(Tipo): Resultado esperado """

asignaturas = ["Matematicas", "Física", "Química", "Historia", "Lengua"]
for asignatura in asignaturas:
    print(F"Yo estudio {asignatura}", sep="\n")