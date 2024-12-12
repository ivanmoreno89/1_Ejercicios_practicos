# Escribir un programa que pregunte al usuario la fecha de su
# nacimiento en formato dd/mm/aaaa y muestra por pantalla
# el día, el mes y el año. Adaptar el programa anterior para
# que también funcione cuando el día o el mes se introduzcan
# con un solo carácter.

""" Fecha de nacimiento

Entradas:
fecha (str): Fecha de nacimiento ingresada por el usuario separada por '/'
dia (str): día extraido de 'fecha'
mes_anio (str): mes y año extraidos de 'fecha'
mes (str): mes extraido de 'mes_año'
año (str): año extraido de 'mes_año'

Salidas:
(str): print con información de nacimiento por día, mes y año """

fecha = str(input("Ingrese su fecha de nacimiento: "))
dia = fecha[:fecha.find("/")]
mes_anio = fecha[fecha.find("/")+1:]
mes = mes_anio[:mes_anio.find("/")]
anio = mes_anio[mes_anio.find("/")+1:]

print(f"El día de nacimiento fue el {dia}")
print(f"El mes de nacimiento fue el {mes}")
print(f"El año de nacimiento fue el {anio}")

# print('El número de teléfono es ', fecha[4:-3])
# print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')
