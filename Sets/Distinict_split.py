t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    prefix = [0]*n
    suffix = [0]*n
    seen=set()
    for i in range(n):
        seen.add(s[i])
        prefix[i]=len(seen)
    seen=set()
    for i in range(n-1,-1,-1):
        seen.add(s[i])
        suffix[i]=len(seen)
    ans=0
    for i in range(n-1):
        ans=max(ans, prefix[i]+suffix[i+1])
    print(ans)




