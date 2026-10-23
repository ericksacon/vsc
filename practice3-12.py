N = int(input("Ingresa la altura de la pirámide: "))

for i in range(1, N + 1):
    espacios = N - i
    asteriscos = ((N + i )* 1) - 1
    linea = (" " * espacios) + ("*" * asteriscos)
    print(linea)

#Tienes que terminar de hacerlo