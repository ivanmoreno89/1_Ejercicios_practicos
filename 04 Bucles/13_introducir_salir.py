# Escribir un programa que muestre el eco de todo
# lo que el usuario introduzca hasta que el usuario
# escriba "salir" que terminará.

""" Eco

Entradas:
frase (str): Información ingresada por el usuario

Salidas:
(str): print hasta que el usuario escriba 'salir' """

frase = ""
while frase.lower() != "salir":
    frase = input("Escriba una frase:\n")
print("Ha salido exitosamente")

# while True:
#     frase = input("Introduce algo: ")
#     if frase == "salir":
#         break
#     print(frase)
