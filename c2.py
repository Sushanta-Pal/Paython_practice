sen=input("Enter a sentence: ")
ls=sen.split()
res=[word for word in ls if word[0].lower() in 'aeiou']
