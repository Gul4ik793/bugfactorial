A = input("введите строку с вхождением h как минимум два раза: ")
B = A.partition("h")
k = B[0]
c = B[2]
m = len(B[2])
for i in range(0,m):
    if "h" in c:
        c = c.partition("h")
        c = c[2]
print(k+c)


