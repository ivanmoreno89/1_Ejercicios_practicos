# Escribir un programa que pregunte al usuario por el número
# de horas trabajadas y el coste por hora. Después debe mostrar
# por pantalla la paga que le corresponde.

horas = int(input("Ingrese las horas completas trabajadas: "))
coste_hora = int(input("Ingrese el coste por hora: "))
coste_total = (horas * coste_hora)
print("El coste total de las horas trabajadas es: ", str(coste_total))