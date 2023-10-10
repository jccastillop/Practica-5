import math

# a. Ingresar n datos a una lista
def ingresar_datos():
    n = int(input("Ingrese la cantidad de datos: "))
    datos = []
    for i in range(n):
        dato = float(input(f"Ingrese el dato {i + 1}: "))
        datos.append(dato)
    return datos

# b. Ordenar una lista de menor a mayor
def ordenar_lista(lista):
    return sorted(lista)

# c. Calcular la sumatoria de los datos de una lista
def sumatoria_lista(lista):
    suma = 0
    for dato in lista:
        suma += dato
    return suma

# d. Calcular la media de los datos
def calcular_media(lista):
    return sumatoria_lista(lista) / len(lista)

# e. Calcular la mediana
def calcular_mediana(lista):
    lista_ordenada = ordenar_lista(lista)
    n = len(lista_ordenada)
    if n % 2 == 0:
        medio1 = lista_ordenada[n // 2 - 1]
        medio2 = lista_ordenada[n // 2]
        return (medio1 + medio2) / 2
    else:
        return lista_ordenada[n // 2]

# f. Calcular la moda
def calcular_moda(lista):
    frecuencias = {}
    for dato in lista:
        if dato in frecuencias:
            frecuencias[dato] += 1
        else:
            frecuencias[dato] = 1
    moda = [k for k, v in frecuencias.items() if v == max(frecuencias.values())]
    return moda

# g. Calcular la desviación típica o estándar para datos sin agrupar
def calcular_desviacion_estandar(lista):
    media = calcular_media(lista)
    sumatoria_cuadrados = sum((dato - media) ** 2 for dato in lista)
    varianza = sumatoria_cuadrados / len(lista)
    desviacion_estandar = math.sqrt(varianza)
    return desviacion_estandar

# Ejemplo de uso
datos = ingresar_datos()
print("Lista ingresada:", datos)
print("Lista ordenada:", ordenar_lista(datos))
print("Sumatoria de la lista:", sumatoria_lista(datos))
print("Media de la lista:", calcular_media(datos))
print("Mediana de la lista:", calcular_mediana(datos))
print("Moda de la lista:", calcular_moda(datos))
print("Desviación estándar de la lista:", calcular_desviacion_estandar(datos))
