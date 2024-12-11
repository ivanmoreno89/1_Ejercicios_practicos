# Escribir un programa que almacene las asignaturas de
# un curso (por ejemplo Matemáticas, Física, Química,
# Historia y Lengua) en una lista, pregunte al usuario
# la nota que ha sacado en cada asignatura y elimine de
# la lista las asignaturas aprobadas. Al final el programa
# debe mostrar por pantalla las asignaturas que el usuario
# tiene que repetir.

""" Ingresar notas a asignaturas y mostrar cuáles se deben repetir

Entradas:
asignaturas (Lista, srt):           Asignaturas cursadas
notas_asignaturas (Lista, int):     Notas obtenidas por cada materia
asignaturas_repetir (Lista, srt):   Asignaturas que se deben repetir
asignatura (srt):                   Contador para asignatura en lista Asignaturas
nota (int):                         Nota obtenida por asignatura 

Salidas:
(SRT): Mensaje con lista de asignaturas a repetir """

# Variables
asignaturas = ["Matematicas", "Física", "Química", "Historia", "Lengua"]
notas_asignaturas = []
asignaturas_repetir = []

# Ciclo para ingreso de notas
for asignatura in asignaturas:
    nota = int(input(f"Digite la nota obtenida en la asignatura {asignatura}:\n"))
    
    # ciclo para validar nota
    if nota < 5:
        notas_asignaturas.append(nota)
        asignaturas_repetir.append(asignatura)

# Mensaje de salida
print(f"Las siguientes son las asignaturas que debe repetir: {asignaturas_repetir}")

# Otras opciones -->

# for n in range(len(asignaturas)-1, -1, -1):
#     notas_asignaturas = float(input(f"Digite la nota obtenida en la asignatura {asignaturas[n]}:\n"))
#     if notas_asignaturas >= 5:
#         asignaturas.pop(n)
# print("Tienes que repetir " + str(asignaturas))

# asignaturas_aprobadas = []
# for asignatura in asignaturas:
#     notas_asignaturas = float(input(f"Digite la nota obtenida en la asignatura {asignatura}:\n"))
#     if notas_asignaturas >= 5:
#         asignaturas_aprobadas.append(asignatura)
# for asignatura in asignaturas_aprobadas:
#     asignaturas.remove(asignatura)
# print("Tienes que repetir " + str(asignaturas))
