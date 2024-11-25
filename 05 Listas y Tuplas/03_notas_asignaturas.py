# Escribir un programa que almacene las asignaturas de
# un curso (por ejemplo Matemáticas, Física, Química,
# Historia y Lengua) en una lista, pregunte al usuario
# la nota que ha sacado en cada asignatura, y después
# las muestre por pantalla con el mensaje En <asignatura>
# has sacado <nota> donde <asignatura> es cada una des
# las asignaturas de la lista y <nota> cada una de las
# correspondientes notas introducidas por el usuario.

""" [Resumen]

Entradas:
Variable_01 (Tipo): [Descripción]
Variable_02 (Tipo): [Descripción]

Salidas:
(Tipo): Resultado esperado """

asignaturas = ["Matematicas", "Física", "Química", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    nota = input(f"Digité la nota obtenida en la asignatura {asignatura}:\n")
    notas.append(nota)
for n in range(len(asignaturas)):
    print(f"En {asignaturas[n]} has obtenido {notas[n]}")