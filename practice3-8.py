print("Bienvenido")
print()
print("Por favor registrese")

user = input("Ingrese su nomre de usuario ")

while True:
    print()
    clave = input("Ingrese su contraseña ")
    if len(clave) < 8:
        print("Su contraseña debe contener al menos 8 caracteres")
    else:
        print("Registro completado exitosamente")
        break

    #Estate atento a la sangria (indentación) de los comandos