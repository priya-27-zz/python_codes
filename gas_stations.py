n,k=map(int,input().split())
x=list(map(int,input().split()))
fuel=k
for i in range(1,n+1):
    fuel=fuel-x[i-1]
    if((fuel)<1):
        ans=i
        break
print(ans)     
