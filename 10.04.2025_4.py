n = int( input("Ввведите основание треугольника, число>=3: "))
m = int (n/2)
if n >= 3:
    for i in range(0, n, 2):
        for j in range(0, m):
            print(end=" ")
        m = m - 1
        for j in range(0, i+1):
            print("*", end="")
        print()
else:
    print("введено неверное число")
