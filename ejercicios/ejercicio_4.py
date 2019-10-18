"""
    autor: @erickgjs99
    file: ejercicios_4.py
"""
notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]
# FUNcion lambda para evaluar quien tine bueno o regular en notas cualitativas
verif = filter(lambda x: x[3] == "Bueno" or x[3] == "Regular", notas)
#impresion de los resultados
print(list(verif))