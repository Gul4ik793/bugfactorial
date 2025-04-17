A = int( input("Ввведите первое целое число: "))
B = int( input("Ввведите второе целое число: "))
if A <= B:
    for A in range(A, B + 1):
        print(A, end=" ")
else:
     for A in range(A, B-1,-1):
        print(A, end=" ")
