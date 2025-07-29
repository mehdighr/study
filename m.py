all_data = {}

def add_num():
    name = input("please add your name :")
    tel_num = input("please add your tel num :")
    all_data[name] = tel_num
    print("now your notebook is this")
    show_num()


def show_num():
    if all_data == {}:
        print("it is empty")
    else:    
        for x,y in all_data.items():
            print(x, y)

def del_num():
    del_name = input("what name you are need to delete it: ")
    if del_name in all_data:
        del all_data[del_name]
        print("delete is complete")
    else:
        print("num not found")

def find_num():
    num_find = input("enter num for find it: ")
    if num_find in all_data.values():
        print("it is here")
    else:
        print("it is not here")

while True:
    menu = """
    1. add num
    2. show num
    3. find num
    4. del num
    5. exit
    """ 
    print(menu)
    my_choise = input("enter your choise: ")
    if my_choise == "1":
        add_num()
    elif my_choise == "2":
        show_num()
    elif my_choise == "3":
        find_num()
    elif my_choise == "4":
        del_num()
    elif my_choise == "5":
        break
    else:
        print("please add true choise")
