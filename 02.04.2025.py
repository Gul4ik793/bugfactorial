x = 1
N = int( input("Ввведите объем куба: "))
print ("сторона куба: ", (N**(1/3)))
y = int(N ** (1/3))
if N ** (1/3)!=int(N ** (1/3)):
    print("Куб неидеальный")
else:
    for i in range(x, y + 1, 1):
        if int((x) ** 3)==N:
            print("Куб идеальный")
        else:
            x = x + 1
