__author__ = 'maxim'
print("#######################################################\r\n")
print("For python files we'll using pyCharm Community Edition")
print("By the way, we need to create our Virtual Environment, it is only available in pyCharm new versions\r\n")
print("#######################################################")
pass

#choice prompt. Check if input == int
def choice():
    choice = input("> ")
    if choice.isdigit() == True:
        return int(choice)
    else:
        return 0

def intro():
    print("""Ты находишься в мрачном гнусном помещении с прелым воздухом и мокрыми стенами.
Из отражения в зеркале на тебя смотрит скелет в старом пиджаке с бабочкой".
Что ты будешь делать?\n""")
    q1()

def q1():
    print("1. Достать руки из сундука")
    print("2. Планировать плап побега.")
    x = choice()
    if x == 1:
        print("У тебя уже есть руки, бака!\n")
        q1()
    elif x == 2:
        print("2")
    else:
        return q1()

intro()
