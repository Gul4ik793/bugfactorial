A = list(input("Ввведите список чисел ").split())
n = len(A)
k = 0
d = 0
for i in range (0, n):
      A[i] = int(A[i])
for m in range (0, n):
      for j in range(0, n):
            if A[m] == A[j] and m!=j:
                        k += 1
      if k == 0:
            d = A[j]
      else:
            k = 0
            print(end="")
      print(d)

