from createproject import create
from view import view
from edit import edit
from delete import delete
from search import search
from mainmenu import mainmenu


def projectmenu():
    while True:

        choice = input("""
                      1: Create 
                      2: View 
                      3: Edit 
                      4: Delete 
                      5: Search 
                      6: MainMenu
                      
                      Please enter your choice: """)

        if choice == "1":
            create()
            break
        elif choice == "2" :
            view()
            break
        elif choice== "3" :
            edit()
            break
        elif choice== "4":
            delete()
            projectmenu()
            break
        elif choice== "5":
            search()
            break
        elif choice== "6" :
            mainmenu()
            break

        else:
            print("You must select number")
            print("Please try again")
            projectmenu()

        
projectmenu()