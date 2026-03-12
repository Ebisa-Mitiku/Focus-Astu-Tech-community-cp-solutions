n=int(input())
l=list(map(int,input().split()))
q=int(input())
for i in range(q):
    s=list(map(int,input().split()))
    if(len(s)==2):
        print(l[s[1]-1])
    else:
        l[s[1]-1]=s[2]
