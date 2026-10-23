peso = float(input("Ingresa tu peso (kg) "))
estatura = float(input("Ingresa tu estatura (m) "))
ind_ma_corporal = peso / estatura**2

if ind_ma_corporal < 18.5:
    print("Tu peso es demasiado bajo")
elif ind_ma_corporal < 25:
    print("Tu peso está en un rango normal")
elif ind_ma_corporal < 30:
    print("Tienes sobrepeso")
else:
    print("Tienes obesidad")