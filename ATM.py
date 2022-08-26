password= 6263
i=0
for i in range(3):    
    password=int(input("enter  password"))
    if password== 6263:
        print("wellcome")
        break
    
    elif password== 3626:
            print("The police were informed")
            break
    elif password!=6263:
       print("password is not correct, try again")
        

else:
    print("your account has been locked")      
     