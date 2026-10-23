num_notas = int(input("Cuántas notas quieres ingresar? "))
notas = 0

for i in range(num_notas):
    nota_ingre = float(input("Nota a ingresar: "))
    notas += nota_ingre
print(f"El promedio de las notas es de {notas / num_notas:.2f}")    





