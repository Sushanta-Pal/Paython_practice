uname="Sushanta Pal"
PIN=1437
i=0
name =eval(input("Enter User name"))
if(name==uname):
    while( i <3):
        pin=eval(input("Enter correct password"))
        if(pin == PIN):
            print("Loged in")
            i=3
        else:
            i +=1
else:
    print("Incorrect Password")

