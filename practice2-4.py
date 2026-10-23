num1=float(input("Primer valor "))
num2=float(input("Segundo valor "))
num3=float(input("Tercer valor "))

if num1 > num2 and num1 > num3:
    print(f"El número {num1} es el mayor")
elif num2 > num1 and num2 > num3:
    print(f"El número {num2} es el mayor")
elif num3 > num2 and num3 > num1:
    print(f"El número {num3} es el mayor")
else:
    print("Los números son iguales")

##Para que el and reconozca ambas condiciones, debo "repetir la condición" Ej:
##if num1 > num2 and num3:Está mal porque no se está tomando en cuenta el num3
##if num1 > num2 and num1 > num3: así está bién ya que ahora si se están tomando en cuenta todas las condiciones