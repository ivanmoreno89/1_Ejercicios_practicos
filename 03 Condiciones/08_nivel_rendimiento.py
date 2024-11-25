# En una determinada empresa, sus empleados son evaluados
# al final de cada año. Los puntos que pueden obtener en
# la evaluación comienzan en 0.0 y pueden ir aumentando,
# traduciéndose en mejores beneficios. Los puntos que pueden
# conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más,
# pero no valores intermedios entre las cifras mencionadas.
# A continuación se muestra una tabla con los niveles
# correspondientes a cada puntuación. La cantidad de dinero
# conseguida en cada nivel es de 2.400€ multiplicada
# por la puntuación del nivel.

# Nivel             Puntuación
# Inaceptable           0.0
# Aceptable             0.4
# Meritorio         0.6 o más

# Escribir un programa que lea la puntuación del usuario
# e indique su nivel de rendimiento, así como la cantidad
# de dinero que recibirá el usuario.

""" Dada una puntuación, devolver el nivel y la cantidad de dinero conseguida

Variables:
puntuacion (float): valoración que recibe el trabajador de acuerdo con la tabla.

Resultado:
(str): Mensaje con nivel obtenido y la cifra en euros multiplicada por la puntuación """

# El usuario ingresa el valor de la puntuación que obtuvo
puntuacion = float(input("Escriba la puntuación obtenida en el periodo evaluado: "))

# Condicional para determinar el 
if puntuacion == 0.0:
    print(f"Su nivel fue INACEPTABLE y por ende la cantidad de dinero recibida será de {puntuacion*2400}€")
elif puntuacion == 0.4:
    print(f"Su nivel fue ACEPTABLE y por ende la cantidad de dinero recibida será de {puntuacion*2400}€")
elif puntuacion >= 0.6:
    print(f"Su nivel fue MERITORIO y por ende la cantidad de dinero recibida será de {puntuacion*2400}€")
else:
    print("Error en la información ingresada")
