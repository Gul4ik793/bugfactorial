A = list(input("Ввведите список чисел ").split())
n = len(A)
k = 0
d = 0
for i in range (0, n):
      A[i] = int(A[i])
for j in range(0, n):
      if k <= A[j]:
            k=A[j]
            d=j
      else:
            print(end="")
print("наибольшее число -", k, "его индекс =", d)



      
