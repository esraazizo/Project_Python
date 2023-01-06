
def view():
    try:
        f = open("projectinfo.txt","r")
    except Exception as e :
        print(e)
    else:
        v = f.read()
        print("---- Information about all projects ----")
        print("Title  : Details : Total target : Start Date : End Date ")
        print(v)



#view()