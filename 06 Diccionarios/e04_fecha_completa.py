# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y
# muestre por pantalla la misma fecha en formato dd de <mes> de aaaa
# donde <mes> es el nombre del mes.

""" Fecha completa

Entradas:
calendar (dict): Calendario
variable2 (type): [Descripción]
variable3 (type): [Descripción]

Salidas:
(type): [Descripción] """

calendar = {'01': 'enero',
              '02': 'febrero',
              '03': 'marzo',
              '04': 'abril',
              '05': 'mayo',
              '06': 'junio',
              '07': 'julio',
              '08': 'agosto',
              '09': 'septiembre',
              '10': 'octubre',
              '11': 'noviembre',
              '12': 'diciembre'
              }

fecha = input('Ingrese la fecha separada por /:\n')
day = fecha[:fecha.find("/")]
month_year = fecha[fecha.find("/")+1:]
month = month_year[:month_year.find("/")]
year = month_year[month_year.find("/")+1:]

if month in calendar:
    print(f'La fecha es {day} de {calendar[month]} de {year}')
else:
    print('Error al procesar la fecha')
