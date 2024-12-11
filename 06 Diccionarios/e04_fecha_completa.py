# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y
# muestre por pantalla la misma fecha en formato dd de <mes> de aaaa
# donde <mes> es el nombre del mes.

""" Fecha completa

Entradas:
calendar (dict): Calendario
fecha (str): Fecha ingresada por el usuario
day (str): día extraido de 'fecha'
month_year (str): mes y año extraido de 'fecha'
month (str): mes extraido de 'month_year'
year (str): año extraido de 'month_year'

Salidas:
(str): print con información de fecha completa """

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

fecha = input('Ingrese la fecha en formato dd/mm/aaaa:\n')
day = fecha[:fecha.find("/")]
month_year = fecha[fecha.find("/")+1:]
month = month_year[:month_year.find("/")]
year = month_year[month_year.find("/")+1:]

if month in calendar:
    print(f'La fecha es {day} de {calendar[month]} de {year}')
else:
    print('Error al procesar la fecha')

# meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
# fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
# fecha = fecha.split('/')
# print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])
