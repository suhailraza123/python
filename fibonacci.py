print("Fibonacci sequence using for loop")
num=int(input("Enter length of series :"))
first=0
second=1
print("{}\n{}".format(first,second))
for val in range(num-2):
        third=first+second
        print(third)
        first=second
        second=third
        
