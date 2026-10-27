def calcular_imc(peso, estatura):
    return peso / estatura ** 2


def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"


# Conectar las dos funciones=============================================
imc = calcular_imc(84, 1.81)
categoria = clasificar_imc(imc)
print(f"Tu IMC es {imc:.2f} y estás en: {categoria}")
#========================================================================

print()
casos = [(50, 1.80), (70, 1.75), (84, 1.81), (100, 1.70)]
for peso, estatura in casos:
    imc = calcular_imc(peso, estatura)
    print(f"{peso} kg, {estatura} m -> IMC {imc:.2f} -> {clasificar_imc(imc)}")
