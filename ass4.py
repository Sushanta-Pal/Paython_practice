
def checkEvenodd(tam,op):
    res=0
    while tam>0:
        rem = tam%10
        if(rem%2 ==op):
            res +=1
        tam = tam //10
    return res


tam=eval(input("Enter a number"))

print("Even = ",checkEvenodd(tam,0))
print("Odd = ",checkEvenodd(tam,1))
