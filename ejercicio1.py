def calcular_suma(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

numeros_suma = (3, 5, 7, 9)
resultado = calcular_suma(*numeros_suma)
print(f"La suma de los números {numeros_suma} es: {resultado}")
