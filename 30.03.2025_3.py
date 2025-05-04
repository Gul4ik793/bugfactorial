import random
possible_action = ["1", "2", "3"]

def computer_action1():
    return  random.choice(possible_action)

def Gul4ik_action1():
    action = input ("введите ваше числовое значение  из перечисленного: (камень[1], ,бумага[2], ножницы[3]): ")
    if action in ["1", "2", "3"]:
        return int(action)
        actions = {1: "Камень", 2: "Бумага", 3: "Ножницы"}
        print (f"вы выбрали: { actions[action]}")
    else:
        print("введите правильный номер:")
        return Gul4ik_action1()



def G_action(Gul4ik_action1, computer_action1):
    actions = {1: "Камень", 2: "Бумага", 3: "Ножницы"}
    print (f"компьютер выбрал: { actions[computer_action1]}")
    print (f"вы выбрали: { actions[action]}")
    if Gul4ik_action1 == computer_action1:
        print ("Ничья: ")
    elif(Gul4ik_action == 1 and computer_action == 2)or\
         (Gul4ik_action == 2 and computer_action == 3) or\
         (Gul4ik_action == 3 and computer_action == 1):
        return ("Ты победил ")
    else:
        return ("Ты проиграл ")
    
    while True:
        Gul4ik_action = Gul4ik_action1()
        computer_action = computer_action1()
        result = G_action(Gul4ik_action1, computer_action1)
       
        print(result)
        input("Завершить игру?: д/н: ")
        if isEnd == "д":
            break
   
    

 
