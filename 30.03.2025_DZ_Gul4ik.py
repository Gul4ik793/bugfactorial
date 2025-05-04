import random
possible_action =[1, 2, 3]
computer = random.choice(possible_action)
getactions = dict({1: "Камень", 2: "Ножницы", 3: "Бумага"})

def Gul4ik_action():
    print("Выберите: 1. Камень  2. Ножницы   3. Бумага ")
    action = input("Введите номер вашего выбора: ")
    if action in ["1", "2", "3"]:
        action = int(action)
        print("Вы выбрали: ", action,":", getactions[action])
        print ("Компьютер выбрал: ",computer,":", getactions[computer] )
        return action
    else:
        print("             Введите номер вашего выбора корректно:")
        return Gul4ik_action()
    
def result_action():
    if Gul4ik == computer:
        print ("             Ничья: ")
    elif(Gul4ik == 1 and computer == 2)or(Gul4ik == 2 and computer == 3) or(Gul4ik == 3 and computer == 1):
        return ("            Ты победил ")
    else:
        return ("            Ты проиграл ")
     
while True:
    Gul4ik = Gul4ik_action()
    result = result_action()
    print(result)
    isEnd = input(" Завершить игру?: д/н: ")
    if isEnd == "д":
        print("Игра окончена!")
        break
    else:
        print("Игра продолжается: ")



   
   
