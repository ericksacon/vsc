num = int(input("De que número quieres calculár su factorial "))

mult = num

for i in range(1, num ):
    mult *= i
print(f"{num}! = {mult}")