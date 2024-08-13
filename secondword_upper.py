a=input("Enter a string: ").split()
if len(a)>=2:
    second_word=a[1].upper()
    print("The second word in uppercase is:", second_word)
else:
    print("The string does not have a second word.")
