num=eval(input("Enter a number"))
tam=num
rev=0
while tam>0:
    rem = tam%10
    rev = rev *10 +rem
    tam = tam //10
if(rev > num):
    print("reversed number is grater")
elif(rev == num):
    print("reversed number is Equal")
else:
    print("reversed number is small")