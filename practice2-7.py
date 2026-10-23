usuario = input("Ingresa tu usuario ")
clave = input("Ingresa tu contraseña ")

if usuario == "admin" and clave == "1234":
    print("Acceso consedido ")
    print(f"Bienvenido {usuario}")
else:
    print("Acceso denegado")