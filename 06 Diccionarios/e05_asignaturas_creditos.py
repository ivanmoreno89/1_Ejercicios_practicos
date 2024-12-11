# Escribir un programa que almacene el diccionario con los créditos de las
# asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y
# después muestre por pantalla los créditos de cada asignatura en el formato
# <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de
# las asignaturas del curso, y <créditos> son sus créditos. Al final debe
# mostrar también el número total de créditos del curso.

""" Asignaturas con créditos

Entradas:
asignaturas (dict): Asignaturas con créditos
creditos (int): Sumatoria de todos los créditos

Salidas:
(str): información de créditos por asignatura y créditos totales """

asignaturas = {
    'Matemáticas': 6,
    'Física': 4,
    'Química': 5
    }

for asignatura in asignaturas:
    print(f'La asignatura {asignatura} tiene {asignaturas[asignatura]} créditos')


creditos = sum(asignaturas.values())
print(f'La suma de todos los créditos es {creditos}')

# curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
# total_creditos = 0
# for asignatura, creditos in curso.items():
#     print(asignatura, 'tiene', creditos, 'créditos')
#     total_creditos += creditos
# print('Número total de créditos del curso: ', total_creditos)
