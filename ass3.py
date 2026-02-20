tam=eval(input("Enter a number"))
while tam>9:
    num=tam
    sum=0
    while num >0:
        rem = num%10
        sum += rem
        num = num //10
    tam=sum
print(tam)