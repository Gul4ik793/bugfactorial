import random
possible_action =[0, 1, 2]

etalon = [["@","@","@"],
          ["@","@","@"],
          ["@","@","@"]]
gamingFirld = [["?","?","?"],
               ["?","?","?"],
               ["?","?","?"]]

def mines_etalon():
    for a in range(0, 3):
        b = random.choice(possible_action)
        etalon[a][b] = "*"
    return etalon

def mine():
    #Координаты закрытой клетки
    koorkl = True
    while koorkl:
        x, y = input("Введите координаты через пробел").split()
        x = int(x)
        y = int(y)
        if x < 0 or x >= 2 or y < 0 or y >= 2:
            print("Координаты выходят за поле")
        koorkl = False
    return (x, y)

    
result = mines_etalon()

koorkl1 = True
while koorkl1:
    a, b = mine()
    print("Ваши координаты мины: ", a,b)
    if result[a][b] == "*":
        gamingFirld[a][b] = "*"
        print("Вы проиграли")
        koorkl1 = False
    else:
        gamingFirld[a][b] = "@"
    print(gamingFirld)


print("Игра окончена")




