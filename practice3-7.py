import random
def numero_random():
    return random.randint(1, 100)

num_random = numero_random()

print("======Adivina el número======")

while True:
    num = int(input("Escoje un número " ))
    if num < num_random:
        print("Más alto")
    elif num > num_random:
        print("Mas bajo")
    else:
        print("Has adivinado el número exitosamente")
        break

