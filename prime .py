n=int(input())
if n==1:
    print("neither prime nor composite")
else:
    c=0
    for i in range(2,n+1):
        if n%i==0:
            c=c+1
        if c>1:
            print("not prime")
        else:
            print("prime")
