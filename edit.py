def edit():
    old=input("Enter data you want to edit it :") 
    new=input("Enter new data want to add it :")
    with open("projectinfo.txt","r") as f:
        newline=[]
        for word in f.readlines():        
            newline.append(word.replace(old,new)) 
            
    print("data updated successfully")


    with open("projectinfo.txt","w") as f:
        for line in newline:
            f.writelines(line)
            
  
        f.close()

    from projectmenu import projectmenu

    projectmenu()

#edit()