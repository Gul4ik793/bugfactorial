A = int( input("Ввведите первое целое число: "))
B = int( input("Ввведите второе целое число: "))
if A <= B:
    while A <= B:
        print(A, end=" ")
        A += 1
else:
     while A >= B:
         print(A, end=" ")
         A -= 1
         
