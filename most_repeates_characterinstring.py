str=input("enter string:")
repeated={}
for char in str:
    if char in repeated:
        repeated[char]+= 1
    else:
        repeated[char]= 1
most_repeated=max(repeated,key=repeated.get)
print(f"The most repeated character is '{most_repeated}'")
