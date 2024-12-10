# Los alumnos de un curso se han dividido en dos grupos A y B
# de acuerdo al sexo y el nombre. El grupo A esta formado por
# las mujeres con un nombre anterior a la M y los hombres con
# un nombre posterior a la N y el grupo B por el resto.
# Escribir un programa que pregunte al usuario su nombre y
# genero y muestre por pantalla el grupo que le corresponde.

""" Grupo de nombres

Entradas:
nombre (str): Nombre ingresado por el usuario
genero (str): genero ingresado por el usuario

Salidas:
(str): Print indicando si pertenece al grupo a o b. También indica error. """

nombre = input("Cuál es tu nombre?: ")
genero = input("Cuál es tu genero?: ")

if (genero.lower() == "femenino" and nombre[0].upper() < "M") or (genero.lower() == "masculino" and nombre[0].upper() < "N"):
    print("perteneces al grupo A")
elif (genero.lower() == "femenino" and nombre[0].upper() > "M") or (genero.lower() == "masculino" and nombre[0].upper() > "N"):
    print("Perteneces al grupo B")
else:
    print("Error en la información ingresada")
