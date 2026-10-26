def num_mayor(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

print(num_mayor(4, 9, 44))
print(num_mayor(8, 3, 9))
print(num_mayor(3, 1, 100))