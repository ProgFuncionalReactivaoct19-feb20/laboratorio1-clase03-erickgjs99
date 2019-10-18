"""
    autor: @erickgjs99
    file: ejercicios_5.py
    Dadas las siguientes edad:

    [10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]
    Se ha generado una lista denomindad black_edades, formada así:
    [10, 14, 30, 32, 40, 16]
    Generar el listado de edades que no estén dentro de las black_edades.
"""
edades = [10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]
black_edades = [10, 14, 30, 32, 40, 16]
#funciones lambda para las edades
valid_age = lambda x: x[x]
valid_black_age = lambda x: x[x]
#funcion lambda para ver si no estan repetidas
list_age = (lambda x: valid_age(x) != valid_black_age(x))
#impresion de los resultados
print(list(map(list_age(valid_age(edades), valid_black_age(black_edades)))))


