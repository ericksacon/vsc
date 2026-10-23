nom = input("Cuál es tu nombre? ")

eda = int(input("Cuál es tu edad? "))

if eda >0 and eda <= 2:
    print(f"{nom}, es un bebé ")
elif eda >=3 and eda <= 12:
    print(f"{nom}, es un niño")
elif eda >= 13 and eda <= 17:
    print(f"{nom}, es un adolescente")
elif eda >=18 and eda <= 64:
    print(f"{nom}, es mayor de edad")
elif eda >= 65 and eda <= 140:
    print(f"{nom}, es un adulto mayor")
else:
    print("Edad no válida")