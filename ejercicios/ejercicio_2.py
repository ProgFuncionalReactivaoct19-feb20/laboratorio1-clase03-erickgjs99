"""
    autor: @erickgjs99
    file: ejercicios_2.py
"""

notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]
# funciones lambda para sumar todas las tuplas
sum1 = lambda x: x[0]
sum2 = lambda x: x[1]
sum3 = lambda x: x[2]
# funcion lambda para sumar los numeros dentro de las tuplas 
total_Sum = lambda x: sum1(x)+sum2(x)+sum3(x)
# impresion de los resultados
print(list(map(total_Sum, notas)))