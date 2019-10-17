ttt=int(input())
while ttt > 0:
    n = int(input())
    S = list(map(int, input().split()))
    E = list(map(int, input().split()))
    se = []
    for idx in range(len(S)):
        se.append((S[idx], E[idx], idx))
    
    se.sort(key = lambda x:x[1])
    i = 0
    count = 1
    #s = str(se[i][2]+1)+" "
    print(se[i][2]+1, end=' ')
    for j in range(1,n):
        if se[j][0] >= se[i][1]:
            count += 1
            i = j
            print(se[i][2]+1, end=' ')
    print()
    t -= 1
    
