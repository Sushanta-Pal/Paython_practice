tam=eval(input("Enter a number"))
res=0
num=eval(input("Enter that specific digit"))
while tam>0:
    rem = tam%10
    if(rem == num):
        res+=1
    tam = tam //10
print(res)