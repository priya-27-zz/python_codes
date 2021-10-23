t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    se=[]
    for idx in range(n):
        se.append((a[idx],b[idx],idx))
    se.sort(key=lambda x:x[1])
    i=0
    counterMy=1
    for j in range(1,n):
        if(se[j][0]>=se[i][1]):
            counterMy+=1
            i=j
    print(counterMy)
