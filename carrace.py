word=input()
t=int(input())
ans=[]
for _ in range(t):
	a,b=map(input().split())
	b=int(b)
	n=len(word)
	if(a=='L'):
		temp=word[b:]+word[:b]
	else:
	    temp=word[(n-b):]+word[:(n-b)]
	ans.append(temp[0])
print(ans)	    	