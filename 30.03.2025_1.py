import random

possible_action = ["камень", "бумага", "ножницы"]
computer_action = random.choice(possible_action)

while True:
    Gul4ik_action = input("введите ваше значение  из перечисленного: камень, бумага, ножницы: " )

    print (" компьютер выбрал: ", computer_action)
    print (" вы выбрали: ", Gul4ik_action)

    if Gul4ik_action == computer_action:
        print ("Ничья: ")
    elif Gul4ik_action == "камень":
        if computer_action == "ножницы":
            print ("Ты победил: ")
        else:
            print ("Ты проиграл: ")
    elif Gul4ik_action == "бумага":
        if computer_action == "камень":
            print ("Ты победил: ")
        else:
            print ("Ты проиграл: ")
    elif Gul4ik_action == "ножницы":
        if computer_action == "бумага":
            print ("Ты победил: ")
        else:
            print ("Ты проиграл: ")
    isEnd = input(" Завершить игру?: д/н: ")
    if isEnd == "д":
        break

 
