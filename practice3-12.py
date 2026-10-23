N = int(input("Ingresa la altura de la pirámide: "))

for i in range(1, N + 1):
    espacios = N - i
    asteriscos = (2 * i) -1
    linea = (" " * espacios) + ("*" * asteriscos)
    print(linea)

