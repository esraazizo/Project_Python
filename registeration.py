import re

def registeration():
 while True:
    fname=input("please enter your first name : ")
    lname=input("please enter your last name : ")
    fullname=fname+lname
    if fullname.isspace():
        print(" spaces are not allowed ")
    elif fullname.isalpha():
        regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
        email=input("please enter your email: ")
        if(re.search(regex,email)):
            #print("valid mail")
            password=input("please enter your password : ")
            password_conf=input("please confirm your password : ")
            if (password_conf==password):
                mobile=input("please enter your phonr number:")
                if mobile.isnumeric():
                    print("registeration done successfully ^_^")
                    user_info=(f"{fullname}:{email}:{password}:{mobile} \n")
                else:
                    print("please enter valid phone number")
                    continue
                try:
                    fileobj=open("info.txt","a")
                except Exception as e:
                    print(e)
                else:
                    fileobj.write(user_info)
                    fileobj.close()
                    break
                    

            else:
                print("not matching passwords")
                continue
                    
        else:
            print("please enter valid email")
            continue

    else:
        print("please enter strings only")
        continue

#registeration()