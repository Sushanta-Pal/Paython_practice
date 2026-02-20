num=eval(input("Enter a number"))
tam=num
rev=0
while tam>0:
    rem = tam%10
    rev = rev *10 +rem
    tam = tam //10
if(rev == num):
    print("Palindrome")
else:
    print("Not Palindrome")