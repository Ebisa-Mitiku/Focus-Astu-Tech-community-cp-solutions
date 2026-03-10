n=int(input())
d={}
for i in range(n):
    t=1
    x=input()
    if(x not in d):
        d[x]=1
        print("OK")
    else:
        new=x+str(d[x])
        d[new]=1
        print(new)
        d[x]+=1


