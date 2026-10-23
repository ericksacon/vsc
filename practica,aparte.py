import os
def limpiar_pantalla() :
    os.system( "cls" if os.name == "nt" else "clear")


print("Introdusca su tarjeta")
print()
print("Bienvenido")

Clave = "3423"
intentos = 0

while intentos < 3:
    nip = input("Ingrese su nip ")
    limpiar_pantalla()
    if nip == Clave:
        print("Acceso concedido")
        break
    else:
        intentos += 1
    if intentos == 1:
        print(f"Acceso denegado, te quedan {3 - intentos} intentos")
    elif intentos == 2:
        print(f"Acceso denegado, te queda {3 - intentos} intento")
    elif intentos == 3:
        print("ya no te quedan intentos")


saldo = 560

while True:
 
  print("Que accion quieres realizar")
  print("======opciones======")
  print("Presiona 1 para consultar saldo")
  print("Presiona 2 para retirar dinero")
  print("Presiona 3 para epositar saldo")
  print("Prsiona 4 salir")
  print("")

  opcion = int(input("Que acción quieres realizar? "))
  if opcion == 1:
      limpiar_pantalla()
      print(f"Tu saldo es de ${saldo}")
      input("Presiona enter para continuar... ")
  elif opcion == 2:
      limpiar_pantalla()
      retiro = float(input("Cantidad a retirar "))
      if retiro < saldo and retiro > 0:
        print(f"Has retirado ${retiro} con éxito")
        input("Presiona enter para continuar... ")
        saldo = saldo - retiro
      else:
          print("Retiro invalido, porfavor, revisa tu saldo")
  elif opcion == 3:
      limpiar_pantalla()
      deposito = float(input("Cantidad a depositar "))
      print(f"Has depositado ${deposito} con éxito")
      input("Presiona enter para continuar.. . ")
      saldo = saldo + deposito
  elif opcion == 4:
      print("Retirando tarjeta...")
      break
 
  