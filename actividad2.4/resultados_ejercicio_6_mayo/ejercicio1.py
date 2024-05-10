pares = 0
impares = 0

while True:
    try:
        num = int(input("Ingrese un numero: "))
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    except ValueError:
        print("Error: Ingrese solo números.")
        break

# Mostrar resultados
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)