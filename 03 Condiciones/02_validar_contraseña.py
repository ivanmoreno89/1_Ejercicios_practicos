# Escribir un programa que almacene la cadena de caracteres contraseña
# en una variable, pregunte al usuario por la contraseña e imprima por
# pantalla si la contraseña introducida por el usuario coincide con la
# guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

password = "contraseña"
user_password = str(input("Ingrese su contraseña: "))
if password == user_password.lower():
    print("La contraseña introducida coincide con la almacenada")
else:
    print("Error: La contraseña introducida no coincide con la almacenada")