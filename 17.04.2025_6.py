A = "AaBbCcDd"
B = ""
C = ""
m = len(A)
for i in range(0,m):
    if A[i].isupper()==True:
        n = A[i]
        B = B + n
    else:
        k = A[i]
        C = C + k
print(B)
print(C)


