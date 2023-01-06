def login():
    try:
        fileobj=open("info.txt","r")
    except Exception as e :
        print(e)
    else:
        users=fileobj.readlines()
#-----------------------------------------------------------------
    user_mail=input("please enter your Email : ")
    password=input("please enter your password : ")
#----------------------------------------------------------------
    found=''
    for i in users:
        user_info=i.split(":")
        if user_info[1]==user_mail and user_info[2]==password:
            print("logged in successfully")
            found='yes'
            break
    if found=='yes':
        pass
    else:
        print("user not found")

            

#login()