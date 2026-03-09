n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(n):
    if l[i]>k:
        l[i]=2
    else:
        l[i]=1
print(sum(l))
