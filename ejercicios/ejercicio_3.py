"""
    autor: @erickgjs99
    file: ejercicios_3.py
"""

# funcion para separar la oracion
def words(cad):
    sep = " "
    lista = cad.split(sep)
    # funcion lambda para sacar la lista
    verif = filter(lambda x: len(x) % 2 == 0 or len(x) % 3 == 0, lista)
    print(list(verif))

words("No hay medicina que cure lo que no cura la felicidad")
