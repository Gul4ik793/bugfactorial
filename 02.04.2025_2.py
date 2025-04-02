N = int( input("Сколько чисел будем складывать?: "))
print ("будем складывать: ", N , "чисел")
y=0
for i in range(1, N+1, 1):
    x = input("введите число или stop: ") 
    if x=="stop":
        break
    else:
        x=int(x)
        y=y+x
print ("сумма чисел: ", y)
    
    
