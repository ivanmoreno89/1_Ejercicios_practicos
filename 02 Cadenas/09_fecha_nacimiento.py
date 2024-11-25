# Escribir un programa que pregunte al usuario la fecha de su
# nacimiento en formato dd/mm/aaaa y muestra por pantalla
# el día, el mes y el año. Adaptar el programa anterior para
# que también funcione cuando el día o el mes se introduzcan
# con un solo carácter.

fecha = str(input("Ingrese su fecha de nacimiento: "))
dia = fecha[:fecha.find("/")]
mes_año = fecha[fecha.find("/")+1:]
mes = mes_año[:mes_año.find("/")]
año = mes_año[mes_año.find("/")+1:]

print(f"El día de nacimiento fue el {dia}")
print(f"El mes de nacimiento fue el {mes}")
print(f"El año de nacimiento fue el {año}")

"""print('El número de teléfono es ', fecha[4:-3])
print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')"""
