t=int(input())
while t>0:
    n=int(input())
    count=0
    while n>0:
        if n%2==1:
            count+=1
        n=int(n/2)
    if count==1:
        print("YES")
    else:
        print("NO")
    t-=1
