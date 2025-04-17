A = input("введите строку: ")
n = len(A)
print(A[2])
print(A[n-2])
print(A[:5])
print(A[:n-2])
print(A[0:n+1:2])
print(A[1:n+1:2])
A1 = A[n+1:0:-1]
A1 = A1+A[0]
print(A1)
print(A1[0:n:2])
print(n)




