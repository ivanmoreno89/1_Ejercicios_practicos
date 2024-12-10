# Escribir un programa que pregunte el correo electrónico del
# usuario en la consola y muestre por pantalla otro correo
# electrónico con el mismo nombre (la parte delante de la
# arroba @) pero con dominio ceu.es.

""" Cambiar dominio de email

Entradas:
email (str): email ingresado por el usuario

Salidas:
(str): print con email y nuevo dominio """

email = input("Introduce tu correo electrónico: ")
print(email[:email.find('@')] + '@ceu.es')