def realizar_division(dividendo, divisor):
    if divisor == 0:
        print("La división entre cero no está definida.")
        return None
    else:
        resultado = dividendo / divisor
        return resultado

# Ejemplo de uso
dividendo = 10
divisor = 0
resultado_division = realizar_division(dividendo, divisor)

if resultado_division is not None:
    print(f"El resultado de la división {dividendo} / {divisor} es: {resultado_division}")
