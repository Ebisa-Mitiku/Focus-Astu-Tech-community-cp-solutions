n=int(input())
count=0
for i in range(n):
    x=0
    a,b,c=map(int,input().split())
    if(a==1):
        x=x+1
    if(b==1):
        x=x+1
    if(c==1):
        x=x+1
    if(x>=2):
        count=count+1
print(count)
