num1 = float(input("Primer termino "))
num2 = float(input("Segundo termino "))

suma = num1 + num2
resta = num1 - num2
multipli = num1 * num2


print("=======Opciones=======")
print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")

opción = input("Elige la operación a realizar ")

if opción == "1":
    print(f"El resultado de la suma es {suma}")
elif opción == "2":
    print(f"El resultado de la resta es de {resta}")
elif opción == "3":
    print(f"El resultado de la multiplicación es {multipli}")
elif opción == "4":
    if num2 == 0:
        print("El divisor debe ser mayor a 0")
    else:
        print(f"El resultado de la operación es {num1 / num2}")
else:
    print("Operación no válida")     