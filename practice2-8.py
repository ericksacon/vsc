año = int(input("Dame un año "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Tú año es viciesto")
else:
    print("Tu año no es viciesto") 
