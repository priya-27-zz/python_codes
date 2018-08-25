word=input()
t=int(input())
ans=[]
for _ in range(t):
    a,b=(input().split())
    b=int(b)
    n=len(word)
    temp=[]
    temp=word
    if(a=='L'):
        temp=temp[b:]+temp[:b]
    else:
        temp=temp[(n-b):]+temp[:(n-b)]
    ans.append(temp[0])
    #print(ans)
answer="".join(ans)
    #print(answer)
op='NO'
    #anagram search
for ind in range(len(word)-t+1):
    per=word[ind:ind+t]
    x=sorted(per)
    y=sorted(answer)
    if x==y:
        op='YES'
print(op)
