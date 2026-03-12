n, m = map(int, input().split())
sell = list(map(int, input().split()))
buy = list(map(int, input().split()))
sell.sort()
buy.sort()
total=[]
if(max(buy)<min(sell)):
    print(max(buy)+1)
else:
    for i in range(n):
        count=0
        for j in buy:
            if(sell[i]<=j):
                count=count+1
        total.append([i+1,count])

    for i in range(n):
        if(total[i][0]>=total[i][1]):
            x=i=1
            break
    print(sell[x])



