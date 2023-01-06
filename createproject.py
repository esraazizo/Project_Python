from datetime import date, datetime

def create():
    while True:
        title=input("please Enter title without spaces  : ")
        if (title.isalpha()):
            print(" Title is added successfully ^_^ ")
            break
        else:
            print("please Enter valid title!")
            continue
#----------------------------------------------------------------------------------------------------------        
    while True:
        details=input("please Enter details : ")
        print(" Details is added successfully ^_^ ")
        break
#-----------------------------------------------------------------------------
    while True:
        total=input("please Enter total target  : ")
        if (total.isdigit()):
            print(" Total is added successfully ^_^ ")
            break
        else:
            print("please Enter valid total!")
            continue
       
#-----------------------------------------------------------------------------
    while True:

        start_year = int(input('Enter a year (start) : '))
        start_month = int(input('Enter a month(start) : '))
        start_day = int(input('Enter a day(start) : '))
        d1 = date(start_year, start_month, start_day)
        print(d1)

        end_year = int(input('Enter a year(end) : '))
        end_month = int(input('Enter a month(end): '))
        end_day = int(input('Enter a day(end): '))
        d2 = date(end_year, end_month, end_day)
        print(d2)

        if d1 < d2 :
            print("date added successfully ")
            break 
        else:
            print("Error ! plesase Enter valid date")
            continue


    user_info=(f"{title}:{details}:{total}:{d1}:{d2} \n")

    try:
        fileobj=open("projectinfo.txt","a")
    except Exception as e:
        print(e)
    else:
        fileobj.write(user_info)
        fileobj.close()

    from projectmenu import projectmenu

    projectmenu()


#create()
