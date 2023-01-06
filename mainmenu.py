from registeration import registeration
from login import login
def mainmenu():
    while True: 
        x = input(" Enter 1 for register or 2 for login or 3 to exit : ")
        if x == "1":
            registeration()
            from projectmenu import projectmenu
            projectmenu()
            break
        elif x == "2":
            login()
            from projectmenu import projectmenu
            projectmenu()
            break
        elif x == "3":
            exit()
        else:
            print("inavlid number!")
            continue



#mainmenu()



