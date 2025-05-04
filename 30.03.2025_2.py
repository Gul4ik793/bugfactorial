import random
possible_action = di["камень", "бумага", "ножницы"]

def Gul4ik_action ():
    return input ("введите ваше значение  из перечисленного: (камень[0], бумага[1], ножницы[2]: ")

def computer_action ():
    return  random.choice(possible_action)

def action():
    if Gul4ik_action == computer_action:
        print ("Ничья: ")
    elif Gul4ik_action == "камень":
        if computer_action == "ножницы":
            print ("Ты победил ")
        else:
            print ("Ты проиграл ")
    elif Gul4ik_action == "бумага":
        if computer_action == "камень":
            print ("Ты победил ")
        else:
            print ("Ты проиграл ")
    elif Gul4ik_action == "ножницы":
        if computer_action == "бумага":
            print ("Ты победил ")
        else:
            print ("Ты проиграл ")
def isEnd():
    input("Завершить игру?: д/н: ")
    if isEnd == "д":
        break
    
while True:
    def calc(a, b):
        print (action)
    
    

 
