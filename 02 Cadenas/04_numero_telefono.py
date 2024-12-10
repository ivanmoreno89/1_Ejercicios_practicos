# Los teléfonos de una empresa tienen el siguiente formato
# prefijo-número-extension donde el prefijo es el código del
# país +34, y la extensión tiene dos dígitos (por ejemplo
# +34-913724710-56). Escribir un programa que pregunte por
# un número de teléfono con este formato y muestre por pantalla
# el número de teléfono sin el prefijo y la extensión.
 
""" Numero telefonico

Entradas:
numero_telefono (str): número de telefono ingresado por el usuario

Salidas:
(str): Print con código de país, número de telefono y extensión por separado """

numero_telefono = str(input("Digite el número de telefono: "))

print(f"El código del país es {numero_telefono[0:3]}")
print(f"El número de teléfono es {numero_telefono[4:13]}")
print(f"La extensión es: {numero_telefono[14:]}")

# print('El número de teléfono es ', tel[4:-3])