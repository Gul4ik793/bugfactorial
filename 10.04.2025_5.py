A = list(input("Ввведите список чисел ").split())
n = len(A)
for i in range (0, n):
      A[i] = int(A[i])
for i in range (0, n, 2):
      print (A[i], end=" ")

      
