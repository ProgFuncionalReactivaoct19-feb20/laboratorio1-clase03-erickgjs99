"""
    autor: @erickgjs99
    file: ejercicios_1.py
    Dado el siguiente conjunto de promedios de estudiantes; determinar 
    los estudiantes que pasan de ciclo. Todos los estudiantes que pasan de ciclo
    son aquellos que tienen un promedio de 16.5 o mayor.
"""
prom = open("promedios.txt")
#Leer archivo
prom.read()
#funcion lambda para verificar los promedios
valid = filter(lambda x: x >= 16.5, prom)

print(list(valid))

prom.close()

