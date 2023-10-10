def calcular_raiz_n(numero, n):
    if numero < 0 and n % 2 == 0:
        return None
    
    resultado = numero ** (1/n)
    return resultado

numero = 27
exponente = 3
raiz_resultado = calcular_raiz_n(numero, exponente)
if raiz_resultado is not None:
    print(f"La raíz {exponente} de {numero} es: {raiz_resultado}")
else:
    print("No se puede calcular la raíz n de un número negativo con un exponente par.")
