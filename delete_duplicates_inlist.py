lis=list(map(int,input("Enter list elements").split()))
print("The original list is : "+str(lis))
lis = list(set(lis))
print("The list after removing duplicates : "+str(lis))
