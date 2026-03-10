class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if(i not in d):
                d[i]=1
            else:
                d[i]+=1
        t=list(d.values())
        t.sort(reverse="True")
        l=set()
        for i in range(k):
            for key in d:
                if(d[key]==t[i]):
                    l.add(key)
        return(list(l))
            
            
       
        
