n = int( input("Ввведите натуральное число<=9: "))
if n <= 9:
    for i in range(1, n + 1):
        for i in range(1, i + 1):
            print(i, end="")
        else:
            print(" ")
else:
    print("введено неверное число")
