# Escribir un programa que almacene las asignaturas
# de un curso (por ejemplo Matemáticas, Física, Química,
# Historia y Lengua) en una lista y la muestre por
# pantalla el mensaje Yo estudio <asignatura>, donde
# <asignatura> es cada una de las asignaturas de la lista.

""" Asignaturas en curso

Entradas:
asignaturas (list): lista de asignaturas

Salidas:
(str): print indicando las asignaturas que se estudian """

asignaturas = ["Matematicas", "Física", "Química", "Historia", "Lengua"]
for asignatura in asignaturas:
    print(F"Yo estudio {asignatura}", sep="\n")