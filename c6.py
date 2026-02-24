d=eval(input("Enter a dictionary: "))
res={k:d[k] for k in d if d[k]>=60}
print(res)