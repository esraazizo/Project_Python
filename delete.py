def delete():
    while True:
         title = input("Enter the title you want to delete : ")
         with open("projectinfo.txt","r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if title not in line:
                    f.write(line)
            f.truncate()
            print(f"Project {title} is deleted successfully ^_^ ")
            break

            
    from projectmenu import projectmenu

    projectmenu()



#delete()